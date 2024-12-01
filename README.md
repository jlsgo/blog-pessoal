# Blog Pessoal - Documentação

Um blog minimalista e elegante desenvolvido com Flask, projetado para documentar minha jornada de aprendizado em tecnologia, com foco especial em Sistemas para Internet, cloud computing e análise de dados.

![Python Version](https://img.shields.io/badge/python-3.x-blue.svg)
![Flask Version](https://img.shields.io/badge/flask-2.x-green.svg)
![License](https://img.shields.io/badge/license-MIT-blue.svg)

## Índice

- [Visão Geral](#visão-geral)
- [Funcionalidades](#funcionalidades)
- [Tecnologias](#tecnologias)
- [Arquitetura](#arquitetura)
- [Instalação](#instalação)
- [Configuração](#configuração)
- [Uso](#uso)
- [Deployment](#deployment)
- [Contribuição](#contribuição)
- [Licença](#licença)

## Visão Geral

Este blog foi desenvolvido como uma plataforma pessoal para compartilhar conhecimentos e experiências na área de tecnologia. Com um design minimalista e tema escuro, o blog oferece uma experiência de leitura agradável e moderna.

### Destaques do Projeto

- Interface limpa e minimalista
- Tema escuro com acentos em roxo e verde
- Suporte completo a Markdown
- Sistema de categorização de posts
- Design responsivo
- Interface administrativa intuitiva

## Funcionalidades

### Core
- Sistema de blog com posts em Markdown
- Categorização de conteúdo
- Interface administrativa para gestão de posts
- Visualização de posts individuais
- Listagem de posts com paginação

### Design
- Tema escuro moderno
- Layout responsivo
- Tipografia otimizada para leitura
- Animações suaves
- Ícones intuitivos

### Técnicas
- URLs amigáveis (slugs)
- Otimização para SEO
- Cache de consultas
- Proteção contra CSRF
- Sanitização de input

## Tecnologias

### Backend
- Python 3.x
- Flask 2.x
- SQLAlchemy
- Flask-Login
- Python-Markdown

### Frontend
- HTML5
- CSS3
- JavaScript
- Font Awesome Icons

### Banco de Dados
- SQLite (Desenvolvimento)
- PostgreSQL (Produção)

### Ferramentas de Desenvolvimento
- Git
- Visual Studio Code
- Python venv

## Arquitetura

```
blog-pessoal/
├── app.py                 # Aplicação principal Flask
├── requirements.txt       # Dependências do projeto
├── instance/             # Dados da instância (banco de dados)
├── static/               # Arquivos estáticos
│   └── css/
│       └── style.css     # Estilos CSS
└── templates/            # Templates Jinja2
    ├── admin.html        # Interface administrativa
    ├── base.html         # Template base
    ├── index.html        # Página inicial
    └── post.html         # Visualização de post
```

## Instalação

1. Clone o repositório
```bash
git clone https://github.com/jlsgo/blog-pessoal.git
cd blog-pessoal
```

2. Crie e ative o ambiente virtual
```bash
# Criar ambiente virtual
python -m venv venv

# Ativar (Linux/Mac)
source venv/bin/activate

# Ativar (Windows)
.\venv\Scripts\activate
```

3. Instale as dependências
```bash
pip install -r requirements.txt
```

## Configuração

### Variáveis de Ambiente
Crie um arquivo `.env` na raiz do projeto:

```env
FLASK_APP=app.py
FLASK_ENV=development
SECRET_KEY=sua-chave-secreta-aqui
DATABASE_URL=sqlite:///blog.db
```

### Banco de Dados
O banco de dados será criado automaticamente na primeira execução.

## Uso

1. Execute o servidor de desenvolvimento
```bash
python app.py
```

2. Acesse o blog
- Frontend: http://localhost:5000
- Admin: http://localhost:5000/admin

### Criando Posts

1. Acesse a interface administrativa
2. Preencha os campos:
   - Título
   - Categoria
   - Conteúdo (suporta Markdown)
3. Clique em "Publicar"

## Deployment

### Preparação
1. Atualize as dependências de produção
2. Configure as variáveis de ambiente
3. Configure o banco de dados PostgreSQL

### Raspberry Pi (Debian)

1. Instale as dependências do sistema
```bash
sudo apt-get update
sudo apt-get install -y python3-pip python3-venv nginx
```

2. Configure o Nginx
```nginx
server {
    listen 80;
    server_name seu-dominio.com;

    location / {
        proxy_pass http://localhost:8000;
        proxy_set_header Host $host;
        proxy_set_header X-Real-IP $remote_addr;
    }
}
```

3. Execute com Gunicorn
```bash
gunicorn -w 4 -b 127.0.0.1:8000 app:app
```

## Contribuição

Contribuições são bem-vindas! Por favor, siga estes passos:

1. Faça um Fork do projeto
2. Crie uma branch para sua feature (`git checkout -b feature/AmazingFeature`)
3. Commit suas mudanças (`git commit -m 'Add some AmazingFeature'`)
4. Push para a branch (`git push origin feature/AmazingFeature`)
5. Abra um Pull Request

## Licença

Este projeto está sob a licença MIT - veja o arquivo [LICENSE](LICENSE) para detalhes.

## Contato

Seu Nome - [@seu_twitter](https://twitter.com/seu_twitter) - seu.email@exemplo.com

Link do Projeto: [https://github.com/jlsgo/blog-pessoal](https://github.com/jlsgo/blog-pessoal)
