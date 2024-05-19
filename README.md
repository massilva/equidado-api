# Equidado
> Inteligência na diversidade dos dados

Este projeto é responsável por fornecer API e ambiente backoffice para administração do sistema.

## Setup

Instale as dependências:
*caso utilize virtualenv será necessário ativá-lo antes de executar os comandos abaixo*

```bash
pip install -r requirements.txt
```

## Rodando a aplicação

O projeto consulta o [Equidado API](https://equidado-008c032b8ff0.herokuapp.com) e é necessário está autenticado para consumo da API.

**Acessando o admin**:

- GET /admin/ -> retornará a página HTML com o ambiente administrativo, com isso, será possível:
  - gerenciar usuários (Admin, Funcionário e RH)
  - gerenciar características
  - gerenaciar empresa

**Endpoint disponíveis**:

- POST /api/v1/token-auth/ -> obter token de acesso da api a partir do usuário cadastrado (usuário demo: `lucas@equidado.com.br` e senha: `1234equi`);
- GET /api/v1/feedback/ -> retorna todos os feedbacks do usuários;
- POST /api/v1/feedback/ -> salva o feedback;

**Configurando o ambiente**:

O ambiente foi construindo seguindo o [12 fatores](https://12factor.net/pt_br/), dessa forma, antes de subir o ambiente é necessário criar variáveis de ambiente que será utilizadas pelo ambiente para isso, preencha as informações contidas no arquivo `var_env`:

```bash
OPENAI_API_KEY=
SECRET_KEY=django-insecure-n8^x*sth)yq26ow&3%=n0qrpwa%ns^b&iv$#-jkh+txvsmy9j^
DJANGO_SETTINGS_MODULE=integra.settings.development

#DATABASE_ENGINE=django.db.backends.postgresql
#DATABASE_NAME={database utilizado}
#DATABASE_USER={usuário do banco de dados}
#DATABASE_PASSWORD={senha do banco de dados}
#DATABASE_HOST={caminho IP ou domínio de acesso ao banco de dados}
#DATABASE_PORT={porta do banco de dados, padrão 5432}
```

A configuração padrão de desenvolvimento irá utilizar o SQLite3 como banco de dados, caso queira conectar a um banco de dados utilize a configuração de produção e remova o `#` do arquivo e preencha-os.

**obs**: uma atualização prevista é modificar o desenvolvimento para aceitar a conexão via banco de dados.

### Ambiente desenvolvimento

Rodando o projeto em `http://localhost:8000`:

Rode o projeto localmente, na pasta raiz do projeto, execute:

```bash
python manage.py runserver
```

### Ambiente produção

Construa a aplicação para produção:

```bash
python manage.py collectstatic
```

Execute o ambiente gunicorn:

```bash
gunicorn integra.wsgi --log-file -
```
