# API de Notas - notes-python

API RESTful desenvolvida em Python com Flask para gerenciar notas. Este projeto fornece endpoints para operações de CRUD (Criar, Ler, Atualizar e Deletar) em um banco de dados PostgreSQL.

## ⚙️ Configuração do Projeto

Siga os passos abaixo para configurar e executar o projeto localmente.

### **Pré-requisitos**

  - Python 3.8+
  - `pip` (gerenciador de pacotes do Python)
  - Um servidor de banco de dados PostgreSQL em execução.

### **Instalação**

1.  **Clone o repositório:**

    ```bash
    git clone https://github.com/DouglasTeyh/notes-python.git
    cd notes-python
    ```

2.  **Crie e ative um ambiente virtual:**

    ```bash
    # Para Windows
    python -m venv venv
    .\venv\Scripts\activate

    # Para macOS/Linux
    python3 -m venv venv
    source venv/bin/activate
    ```

3.  **Instale as dependências:**

    ```bash
    pip install -r requirements.txt
    ```

4.  **Configure as variáveis de ambiente:**
    Crie um arquivo chamado `.env` na raiz do projeto e adicione a URL de conexão do seu banco de dados PostgreSQL.

    **Arquivo `.env`:**

    ```
    DB_URL=postgresql://USUARIO:SENHA@HOST:PORTA/NOME_DO_BANCO
    ```

    Substitua `USUARIO`, `SENHA`, `HOST`, `PORTA` e `NOME_DO_BANCO` com as suas credenciais.

### **Executando a Aplicação**

Com o ambiente virtual ativado e o arquivo `.env` configurado, execute o comando abaixo para iniciar o servidor. As tabelas do banco de dados serão criadas automaticamente na primeira execução.

```bash
flask run
```

O servidor estará disponível em `http://127.0.0.1:5000`.

-----

## 📖 Documentação da API

A URL base para todos os endpoints é `/notes`.

### **Modelo de Dados: `Note`**

O objeto `Note` possui a seguinte estrutura:

| Atributo     | Tipo       | Descrição                                 |
| :----------- | :----------| :---------------------------------------- |
| `id`         | integer    | Identificador único da nota.              |
| `title`      | string     | Título da nota (máx. 128 caracteres).     |
| `message`    | string     | Conteúdo da nota (máx. 2048 caracteres).  |
| `created_at` | timestamp  | Data e hora de criação (formato ISO 8601). |
| `updated_at` | timestamp  | Data e hora da última atualização (ISO 8601). |

<br>

### **Endpoints**

#### 1\. Criar Nota

Cria uma nova nota.

  - **Método:** `POST`
  - **Endpoint:** `/notes/`
  - **Corpo da Requisição (JSON):**
    ```json
    {
      "title": "Minha Primeira Nota",
      "message": "Este é o conteúdo da minha primeira nota."
    }
    ```
  - **Resposta de Sucesso (201 Created):**
    ```json
    {
      "id": 1,
      "title": "Minha Primeira Nota",
      "message": "Este é o conteúdo da minha primeira nota.",
      "created_at": "2025-07-28T09:30:00.123456-03:00",
      "updated_at": "2025-07-28T09:30:00.123456-03:00"
    }
    ```
  - **Resposta de Erro (400 Bad Request):**
    ```json
    {
      "Error": "Mensagem de erro detalhando o problema."
    }
    ```

-----

#### 2\. Buscar Nota por ID

Busca uma nota específica pelo seu `id`.

  - **Método:** `GET`
  - **Endpoint:** `/notes/<id_nota>`
  - **Resposta de Sucesso (200 OK):**
    ```json
    {
      "id": 1,
      "title": "Minha Primeira Nota",
      "message": "Este é o conteúdo da minha primeira nota.",
      "created_at": "2025-07-28T09:30:00.123456-03:00",
      "updated_at": "2025-07-28T09:30:00.123456-03:00"
    }
    ```
  - **Resposta de Erro (400 Bad Request):**
    ```json
    {
      "Error": "Nota com o ID: 1 não foi encontrada."
    }
    ```

-----

#### 3\. Editar Nota

Atualiza o título e/ou a mensagem de uma nota existente.

  - **Método:** `PUT`
  - **Endpoint:** `/notes/<id_nota>`
  - **Corpo da Requisição (JSON):**
    ```json
    {
      "title": "Título da Nota Atualizado",
      "message": "Conteúdo atualizado."
    }
    ```
  - **Resposta de Sucesso (200 OK):** Retorna o objeto da nota atualizada.
    ```json
    {
      "id": 1,
      "title": "Título da Nota Atualizado",
      "message": "Conteúdo atualizado.",
      "created_at": "2025-07-28T09:30:00.123456-03:00",
      "updated_at": "2025-07-28T09:35:10.789012-03:00"
    }
    ```
  - **Resposta de Erro (400 Bad Request):**
    ```json
    {
      "Error": "Nota com o ID: 1 não foi encontrada."
    }
    ```

-----

#### 4\. Excluir Nota

Exclui uma nota específica pelo seu `id`.

  - **Método:** `DELETE`
  - **Endpoint:** `/notes/<id_nota>`
  - **Resposta de Sucesso (200 OK):**
    ```json
    {
      "message": "Nota excluída com sucesso."
    }
    ```
  - **Resposta de Erro (400 Bad Request):**
    ```json
    {
      "Error": "Nota com o ID: 1 não foi encontrada."
    }
    ```
