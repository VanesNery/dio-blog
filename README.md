
# 📝 DIOBlog

## 📌 Sobre o projeto

O **DIOBlog** é uma API REST desenvolvida em **Python com Flask**, criada como projeto prático durante minha jornada de estudos na **Digital Innovation One (DIO)**.

O objetivo é aplicar, de forma progressiva, conceitos de desenvolvimento backend, persistência de dados, autenticação, autorização, migrations, testes automatizados e deploy.

Mais do que um projeto de curso, o DIOBlog está sendo utilizado como um **projeto vivo de aprendizado**, evoluindo conforme novos conceitos são estudados e aplicados.

### Fluxo do projeto

```text
Código
   ↓
Git
   ↓
GitHub
   ↓
Banco de dados
   ↓
Migrations
   ↓
Testes
   ↓
Deploy
   ↓
Ambiente de produção
```

---

## 🚀 Tecnologias

### Backend

* 🐍 **Python 3.12+**
* 🌐 **Flask**
* 🗃️ **SQLAlchemy**
* 🔄 **Flask-Migrate**

### Banco de dados

* 🐘 **PostgreSQL** para ambiente de produção
* 🗄️ **SQLite** para desenvolvimento local
* **SQLAlchemy ORM**
* **Flask-Migrate** para gerenciamento das migrations

### Autenticação

* 🔐 **Flask-JWT-Extended**
* Autenticação baseada em JWT
* Estrutura de autorização baseada em roles

### Testes

* 🧪 **Pytest**
* **pytest-mock**
* Testes unitários
* Testes de integração

### Desenvolvimento e deploy

* 📦 **Poetry**
* 🚀 **Gunicorn**
* ☁️ **Render**
* 🐙 **GitHub**

---

## ✨ Funcionalidades

### 👤 Usuários

* [x] Criação de usuários
* [x] Listagem de usuários
* [x] Consulta de usuário por ID
* [x] Atualização de usuário
* [x] Exclusão de usuário

### 📝 Posts

* [x] Criação de posts
* [x] Listagem de posts
* [x] Consulta de post por ID
* [x] Atualização de posts
* [x] Exclusão de posts
* [x] Associação do post ao usuário autor

### 👥 Roles

* [x] Criação de roles
* [x] Listagem de roles
* [ ] Consulta de role por ID
* [ ] Atualização de role
* [ ] Exclusão de role
* [x] Associação de usuários a roles

### 🔐 Autenticação

* [x] Login
* [x] Geração de JWT
* [x] Proteção de endpoints autenticados
* [x] Identificação do usuário autenticado

> 🚧 O projeto continua em desenvolvimento e novas funcionalidades serão adicionadas progressivamente.

---

## 🏗️ Estrutura do projeto

```text
dio-blog/
│
├── migrations/
│   └── ...
│
├── src/
│   ├── controllers/
│   │   ├── auth.py
│   │   ├── post.py
│   │   ├── role.py
│   │   └── user.py
│   │
│   ├── app.py
│   ├── config.py
│   ├── db.py
│   ├── schema.sql
│   ├── utils.py
│   └── wsgi.py
│
├── tests/
│   ├── integration/
│   └── unit/
│
├── .gitignore
├── poetry.lock
├── pyproject.toml
├── render-deploy.sh
└── README.md
```

A aplicação utiliza **Blueprints do Flask** para organizar os diferentes recursos da API, mantendo controllers separados para autenticação, usuários, posts e roles. A aplicação registra esses blueprints durante sua inicialização.

---

## 🗄️ Modelagem

O projeto possui atualmente três entidades principais:

```text
┌──────────────┐
│     Role     │
├──────────────┤
│ id           │
│ name         │
└──────┬───────┘
       │
       │ 1:N
       ▼
┌──────────────┐
│     User     │
├──────────────┤
│ id           │
│ username     │
│ password     │
│ active       │
│ role_id      │
└──────┬───────┘
       │
       │ 1:N
       ▼
┌──────────────┐
│     Post     │
├──────────────┤
│ id           │
│ title        │
│ body         │
│ created      │
│ author_id    │
└──────────────┘
```

Os relacionamentos entre `Role`, `User` e `Post` são definidos utilizando SQLAlchemy ORM.

---

## 🔑 Autenticação

A API utiliza **JWT — JSON Web Token** para autenticação.

Fluxo básico:

```text
Cliente
   │
   │ POST /auth/login
   ▼
┌───────────────┐
│   Flask API   │
└───────┬───────┘
        │
        ├── valida usuário
        │
        └── gera JWT
              │
              ▼
        Access Token
              │
              ▼
      Requisições protegidas
```

A aplicação utiliza `Flask-JWT-Extended` para gerenciamento dos tokens JWT.

---

## 🧪 Testes

O projeto possui uma estrutura separada para testes:

```text
tests/
├── integration/
└── unit/
```

As ferramentas utilizadas são:

* **Pytest**
* **pytest-mock**

A configuração do projeto define `tests` como diretório de testes e utiliza Pytest como framework de execução.

Para executar:

```bash
poetry run pytest
```

---

## 📦 Gerenciamento de dependências

O projeto utiliza **Poetry** para gerenciamento das dependências e configuração do ambiente Python.

Instalação:

```bash
poetry install
```

Execução de comandos:

```bash
poetry run <comando>
```

---

## 💻 Executando localmente

### 1. Clone o repositório

```bash
git clone https://github.com/VanesNery/dio-blog.git
```

### 2. Acesse o projeto

```bash
cd dio-blog
```

### 3. Instale as dependências

```bash
poetry install
```

### 4. Configure as variáveis de ambiente

Exemplo:

```env
DATABASE_URL=postgresql://usuario:senha@localhost:5432/dio_blog
SECRET_KEY=sua-secret-key
JWT_SECRET_KEY=sua-jwt-secret-key
```

Para desenvolvimento local, a aplicação possui **SQLite como configuração padrão**:

```text
sqlite:///dio_blog.sqlite
```

conforme definido na configuração da aplicação.

### 5. Execute as migrations

```bash
poetry run flask --app src.app db upgrade
```

### 6. Execute a aplicação

```bash
poetry run flask --app src.app run
```

A aplicação estará disponível em:

```text
http://127.0.0.1:5000
```

---

## ☁️ Deploy

O projeto foi preparado para deploy utilizando **Render**.

Para execução em produção, o projeto utiliza **Gunicorn** e possui configuração específica para inicialização da aplicação. O `pyproject.toml` também inclui `gunicorn` e `psycopg2-binary` entre as dependências.

### 🟡 Status do deploy

O deploy foi realizado no Render, porém o serviço pode permanecer **suspenso quando não está sendo utilizado**, evitando o consumo desnecessário da franquia disponível.

O código, configuração e processo de deploy permanecem versionados neste repositório.

---

## 📚 Conceitos praticados

Com este projeto estou consolidando conhecimentos em:

* Python
* Flask
* APIs REST
* SQLAlchemy
* ORM
* PostgreSQL
* SQLite
* JWT
* Autenticação
* Autorização
* Roles
* Migrations
* Testes unitários
* Testes de integração
* Git
* GitHub
* Poetry
* Gunicorn
* Deploy
* Organização de aplicações backend

---

## 🔭 Próximos passos

O DIOBlog continuará evoluindo conforme avanço na formação.

### Backlog

* [ ] Finalizar CRUD de roles
* [ ] Melhorar validação dos dados de entrada
* [ ] Melhorar tratamento de erros
* [ ] Implementar hash seguro de senhas
* [ ] Evitar exposição de informações sensíveis nas respostas
* [ ] Ampliar cobertura de testes
* [ ] Melhorar documentação dos endpoints
* [ ] Adicionar documentação OpenAPI / Swagger
* [ ] Evoluir regras de autorização
* [ ] Revisar e melhorar a modelagem
* [ ] Evoluir o processo de deploy
* [ ] Adicionar novas funcionalidades ao blog

---

## 🎯 Objetivo do projeto

O DIOBlog representa uma etapa prática da minha evolução como desenvolvedora backend.

A proposta é continuar transformando o projeto conforme avanço nos estudos, aplicando conceitos de:

**Python → APIs → Banco de Dados → Segurança → Testes → Arquitetura → Deploy**

Dessa forma, o projeto acompanha não apenas a evolução da aplicação, mas também minha evolução técnica como desenvolvedora.

---

## 👩‍💻 Autora

### Vanessa Nery

**Backend Developer | Python | APIs | Microsserviços**

🐙 [GitHub — VanesNery](https://github.com/VanesNery)

---

⭐ Se você gostou do projeto, considere deixar uma estrela no repositório.

> 📌 Projeto em desenvolvimento — novas funcionalidades e melhorias serão adicionadas conforme minha evolução nos estudos.

[1]: https://github.com/VanesNery/dio-blog "GitHub - VanesNery/dio-blog · GitHub"
