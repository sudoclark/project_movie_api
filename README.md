# movie-api

API REST em Python para busca de informações de filmes, construída com Flask. Projeto de estudos.

## Tecnologias

- **Python** + **Flask**
- **Redis** — cache do histórico de buscas
- **OMDB API** — fonte dos dados dos filmes
- **pytest** — testes

## Endpoints

| Método | Rota       | Descrição                              |
|--------|------------|----------------------------------------|
| POST   | `/movies`  | Busca informações de um filme pelo nome |
| GET    | `/history` | Retorna o histórico de filmes buscados |

### Body — POST `/movies`

```json
{
  "movie_name": "Inception"
}
```

### Resposta

```json
{
  "title": "Inception",
  "released": "2010",
  "genre": "Action, Adventure, Sci-Fi",
  "director": "Christopher Nolan",
  "synopsis": "...",
  "cast": "Leonardo DiCaprio, ..."
}
```

## Como rodar

**Pré-requisitos:** Python 3.x, Redis rodando localmente.

```bash
# Instale as dependências
pip install -r requirements.txt

# Configure o .env (veja .env.example abaixo)

# Suba a aplicação
python run.py
```

A API estará disponível em `http://localhost:3000`.

## Variáveis de ambiente (.env)

```env
API_KEY=sua_chave_omdb

REDIS_HOST=localhost
REDIS_PORT=6379

# Define se a API retorna dados mockados (true/false)
API_MOCK_ENABLED=false
```

> A chave da OMDB API pode ser obtida em [omdbapi.com](https://www.omdbapi.com/apikey.aspx).
