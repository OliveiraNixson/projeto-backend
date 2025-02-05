# projeto-backend
Projeto para o processo seletivo do lapisco
# Library API

## Descrição
A API RESTful foi desenvolvida com Django e Django REST Framework para gerenciar livros, autores e usuários. Permite a criação, leitura, atualização e remoção (CRUD) de registros.

## Tecnologias Utilizadas
- Python
- Django
- Django REST Framework
- PostgreSQL (ou SQLite para desenvolvimento)
- Docker (Meus conhecimentos precarios em docker não permitiram dizer se funciona ou não.

## Instalação e Configuração

### 1. Clonar o repositório
```bash
meu git
```

### 2. Criar e ativar um ambiente virtual
```bash
python -m venv venv
venv\Scripts\activate  # Windows
```

### 3. Instalar dependências
```bash
pip install -r requirements.txt
```

### 4. Configurar o banco de dados
No arquivo `settings.py`, configure as credenciais do PostgreSQL ou utilize SQLite para testes:
```python
DATABASES = {
    'default': {
        'ENGINE': os.environ.get('DB_DRIVER', 'django.db.backends.postgresql'),
        'NAME': os.environ.get('PG_DB', 'postgres'),
        'USER': os.environ.get('PG_USER', 'postgres'),
        'PASSWORD': os.environ.get('PG_PASSWORD', 'postgres'),
        'HOST': os.environ.get('PG_HOST', 'localhost'),
        'PORT': os.environ.get('PG_PORT', '5432'),
    }
```

### 5. Executar migrações e iniciar o servidor
```bash
python manage.py migrate
python manage.py runserver
```
A API deveria ficar disponível em `http://127.0.0.1:8000/`

## Endpoints da API

### **Autores**
- `GET /authors/` - Lista todos os autores
- `POST /authors/` - Cria um novo autor
- `GET /authors/{id}/` - Retorna detalhes de um autor
- `PUT /authors/{id}/` - Atualiza um autor
- `DELETE /authors/{id}/` - Remove um autor

### **Livros**
- `GET /books/` - Lista todos os livros
- `POST /books/` - Cria um novo livro
- `GET /books/{id}/` - Retorna detalhes de um livro
- `PUT /books/{id}/` - Atualiza um livro
- `DELETE /books/{id}/` - Remove um livro

### **Usuários**
- `GET /users/` - Lista todos os usuários
- `GET /users/{id}/` - Retorna detalhes de um usuário
- `POST /users/` - Adiciona um novo usuário
- `PUT /users/{id}/` - Atualiza um usuário
- `DELETE /users/{id}/` - Remove um usuário

## Docker
Para rodar a aplicação via Docker, utilize os comandos:
```bash
docker-compose up --build
Em tese deveria ser assim, mas tive 1001 erros tentando fazer isso. Quase quebrei meu computador de madrugada.
```
Isso irá iniciar a API junto ao banco de dados PostgreSQL em contêineres.

## Testes
Para rodar os testes automatizados:
```bash
python manage.py test
```

## Licença
Este projeto está licenciado sob a **MIT License**.

