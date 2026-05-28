# Detector de Fake News — Mostra Científica 2025

Projeto desenvolvido para a Mostra Científica escolar de 2025, premiado em **1º lugar** na escola. A proposta foi criar um protótipo web capaz de apoiar a verificação de notícias em português, comparando o texto informado com resultados encontrados na web e calculando uma pontuação de similaridade.

> **Status:** protótipo acadêmico/educacional. O resultado não deve ser usado como veredito automático de verdade ou mentira; ele serve como apoio inicial para investigação e leitura crítica.

## Objetivo

O projeto busca demonstrar, de forma prática, como técnicas simples de processamento de linguagem natural podem ajudar no combate à desinformação. A aplicação recebe uma URL ou um texto/título, coleta conteúdos relacionados, limpa os textos e calcula o quanto eles se parecem.

## Funcionalidades

- Interface web simples em HTML, CSS e JavaScript.
- API em Flask para receber consultas por URL ou texto.
- Coleta de páginas relacionadas usando Google Custom Search.
- Extração e limpeza de texto HTML com BeautifulSoup e NLTK.
- Remoção de stopwords em português.
- Vetorização textual com `CountVectorizer`.
- Cálculo de similaridade por cosseno com scikit-learn.
- Registro opcional dos resultados em MySQL.

## Como funciona

1. O usuário informa uma URL ou um texto/título pela interface.
2. O backend extrai ou recebe o conteúdo textual.
3. O projeto pesquisa notícias semelhantes usando a API de busca do Google.
4. As páginas retornadas são baixadas e convertidas em texto limpo.
5. O texto original e os textos encontrados passam por pré-processamento.
6. A aplicação calcula a similaridade entre os conteúdos.
7. Um relatório HTML é retornado com URLs analisadas e pontuações.

## Tecnologias utilizadas

- Python
- Flask
- Flask-CORS
- Requests
- BeautifulSoup4
- NLTK
- scikit-learn
- MySQL Connector/Python
- HTML, CSS e JavaScript
- Tailwind CSS via CDN

## Estrutura do repositório

```text
.
├── API.py                         # Servidor Flask e rotas da aplicação
├── Complete.py                    # Pipeline principal de busca, limpeza e similaridade
├── Database.py                    # Integração opcional com banco MySQL local
├── filtrador.py                   # Conversão de HTML para texto limpo
├── Neural.py                      # Experimento isolado de similaridade textual
├── google_requester.py            # Script auxiliar para testar a busca do Google
├── web_downloader.py              # Script auxiliar para baixar páginas HTML
├── Instalador_de_requerimentos.py # Instalador legado usado durante a feira
├── requirements.txt               # Dependências Python recomendadas
├── .env.example                   # Exemplo de variáveis de ambiente
└── Site/                          # Telas HTML e JavaScript do protótipo
```

## Como executar localmente

### 1. Criar e ativar um ambiente virtual

```bash
python -m venv .venv
source .venv/bin/activate
```

No Windows PowerShell:

```powershell
python -m venv .venv
.\.venv\Scripts\Activate.ps1
```

### 2. Instalar dependências

```bash
pip install -r requirements.txt
```

### 3. Configurar variáveis de ambiente

Copie o arquivo de exemplo:

```bash
cp .env.example .env
```

Depois, preencha as credenciais da sua Google Custom Search API:

```env
GOOGLE_API_KEY=sua_chave_google
GOOGLE_SEARCH_ENGINE_ID=seu_search_engine_id
```

A integração com MySQL é opcional. Para ativá-la, configure também:

```env
MYSQL_HOST=127.0.0.1
MYSQL_USER=root
MYSQL_PASSWORD=
MYSQL_DATABASE=Mostra
```

### 4. Rodar a aplicação

```bash
python API.py
```

Por padrão, o servidor sobe em:

```text
http://localhost:80
```

> Em alguns sistemas, a porta `80` exige permissão de administrador. Se necessário, altere a porta em `API.py` para `5000` durante testes locais.

## Endpoints principais

| Rota | Descrição |
| --- | --- |
| `/` | Página inicial |
| `/check` | Tela de escolha entre URL e título/texto |
| `/url` | Formulário para análise por URL |
| `/title` | Formulário para análise por texto/título |
| `/send_url?data=...` | Recebe uma URL, baixa o conteúdo e analisa similaridade |
| `/send_title?data=...` | Recebe texto/título e analisa similaridade |

## Observações importantes

- Este repositório foi organizado para apresentação em currículo/portfólio, mantendo a ideia original do projeto escolar.
- Chaves de API não devem ser versionadas no código. Use variáveis de ambiente ou arquivo `.env` local.
- A pontuação de similaridade não substitui checagem jornalística profissional.
- Alguns scripts são experimentais e foram mantidos para demonstrar o processo de desenvolvimento.

## Possíveis melhorias futuras

- Melhorar tratamento de erros e respostas JSON da API.
- Adicionar testes automatizados.
- Criar uma camada de configuração mais completa.
- Trocar strings SQL montadas manualmente por queries parametrizadas.
- Adicionar Docker para facilitar execução.
- Criar um design responsivo mais consistente.
- Incluir fontes confiáveis e critérios de checagem mais transparentes.

## Autores

- Arthur Witt
- Yuri Sirtoli
- Rafael Becker

## Licença

Este projeto ainda não possui uma licença definida. Antes de reutilizar o código publicamente, recomenda-se adicionar um arquivo `LICENSE` ao repositório.
