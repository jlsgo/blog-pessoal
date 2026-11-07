# blog-pessoal

Blog simples em Flask para registrar estudos de tecnologia. Os posts são escritos em Markdown,
guardados num banco SQL e listados do mais novo para o mais antigo, com tema escuro.

## Funcionalidades

- Lista de posts na página inicial e página própria para cada post (`/post/<slug>`)
- Conteúdo em Markdown, convertido para HTML na exibição
- Categoria por post e URL gerada a partir do título (`python-slugify`)
- Formulário em `/admin` para publicar

## Stack

Python 3, Flask 2.3, Flask-SQLAlchemy, Markdown e python-dotenv. SQLite por padrão; outro banco
pela variável `DATABASE_URL`.

## Executar

```bash
python3 -m venv .venv && . .venv/bin/activate
pip install -r requirements.txt
python3 app.py            # http://localhost:5000
```

Configuração opcional num `.env`:

```env
SECRET_KEY=troque-esta-chave
DATABASE_URL=sqlite:///blog.db
```

O banco é criado na primeira execução.

## Estado atual

- `/admin` ainda não tem login (o Flask-Login está nas dependências, mas não foi ligado). Rode
  apenas localmente até isso existir.
- A rota `/about` aponta para um template (`about.html`) que ainda não foi criado.
- `app.py` sobe em modo debug; para publicar, use um servidor WSGI (por exemplo, Gunicorn).

## Licença

MIT.
