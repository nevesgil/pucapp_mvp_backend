# ChildsNotes-Backend

Backend do ChildsNotes, uma API construída com Flask, Docker e um banco de dados PostgreSQL.

Esta documentação é referente ao backend do projeto. Para informações sobre o frontend, consulte o repositório [ChildsNotes-Frontend](https://github.com/nevesgil/pucapp_mvp_frontend).


## Índice
- [Introdução](#introdução)
- [Tecnologias](#tecnologias)
- [Instalação](#instalação)
- [Uso](#uso)
  - [Uso do Swagger](#uso-do-swagger)
  - [Uso do Banco de Dados](#uso-do-banco-de-dados)
- [Endpoints](#endpoints)


## Introdução
Este repositório contém o backend para a aplicação ChildsNotes. Ele inclui uma API construída com Flask e um banco de dados PostgreSQL, tudo configurado para rodar com Docker e Docker Compose.

## Tecnologias
- Flask
- PostgreSQL
- Docker
- Docker Compose

OBS: É necessário ter o Docker instalado em sua máquina antes de utilizar a aplicação!!

## Instalação
Para começar a usar o backend do ChildsNotes, siga estes passos:

1. **Clone o repositório:**
   ```sh
   https://github.com/nevesgil/pucapp_mvp_backend.git

2. **Navegue para o repositório**
   ```sh
   cd pucapp_mvp_backend

3. **Construa e inicie os containers**
   ```
   docker-compose up --build

Obs: Ao fim do uso, utilizar o comando ```docker-compose down```

Todas as imagens, dependências e connections estão pré-configuradas.

Após essa etapa, a aplicação pode ser acessada na porta 5000, e o banco na porta 8081.

## Uso

### Uso do Swagger

A documentação da API pode ser diretamente acessada em http://localhost:5000/docs/ enquanto os containers estiverem em funcionamento.

![swagger1](/doc_images/swagger1.png)


### Uso do Banco de Dados

