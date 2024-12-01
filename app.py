from flask import Flask, render_template, request, redirect, url_for, flash
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime
from markdown import markdown
from slugify import slugify
import os
from dotenv import load_dotenv

load_dotenv()

app = Flask(__name__)
app.config['SECRET_KEY'] = os.getenv('SECRET_KEY', 'dev')
app.config['SQLALCHEMY_DATABASE_URI'] = os.getenv('DATABASE_URL', 'sqlite:///blog.db')
db = SQLAlchemy(app)

class Post(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(200), nullable=False)
    slug = db.Column(db.String(200), unique=True, nullable=False)
    content = db.Column(db.Text, nullable=False)
    category = db.Column(db.String(50))
    created_at = db.Column(db.DateTime, nullable=False, default=datetime.utcnow)

    def __repr__(self):
        return f'<Post {self.title}>'

with app.app_context():
    db.create_all()

@app.route('/')
def index():
    posts = Post.query.order_by(Post.created_at.desc()).all()
    return render_template('index.html', posts=posts)

@app.route('/post/<slug>')
def post(slug):
    post = Post.query.filter_by(slug=slug).first_or_404()
    content = markdown(post.content)
    return render_template('post.html', post=post, content=content)

@app.route('/about')
def about():
    return render_template('about.html')

@app.route('/admin', methods=['GET', 'POST'])
def admin():
    if request.method == 'POST':
        title = request.form['title']
        content = request.form['content']
        category = request.form['category']
        slug = slugify(title)
        
        post = Post(title=title, content=content, category=category, slug=slug)
        db.session.add(post)
        db.session.commit()
        
        flash('Post created successfully!', 'success')
        return redirect(url_for('index'))
    
    return render_template('admin.html')

if __name__ == '__main__':
    app.run(host='0.0.0.0', debug=True)
