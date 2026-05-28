# Fake News Detector — 2025 Science Fair

This project was built for a 2025 school Science Fair and won **1st place** at the school. The goal was to create a web prototype that supports Portuguese news verification by comparing a submitted text with related web results and calculating a similarity score.

> **Status:** academic/educational prototype. The score should not be treated as an automatic true-or-false verdict; it is intended as a starting point for investigation and critical reading.

## Goal

The project demonstrates how simple natural language processing techniques can help fight misinformation. The application receives a URL or a text/title, collects related content, cleans the text, and calculates how similar the sources are.

## Features

- Simple web interface built with HTML, CSS, and JavaScript.
- Flask API for receiving URL or text queries.
- Related-page collection with Google Custom Search.
- HTML text extraction and cleaning with BeautifulSoup and NLTK.
- Portuguese stopword removal for the analyzed news content.
- Text vectorization with `CountVectorizer`.
- Cosine similarity calculation with scikit-learn.
- Optional result logging in MySQL.

## How it works

1. The user submits a URL or text/title through the interface.
2. The backend extracts or receives the textual content.
3. The project searches for similar news using the Google Custom Search API.
4. Returned pages are downloaded and converted into clean text.
5. The original text and collected texts are preprocessed.
6. The application calculates similarity between the contents.
7. An HTML report is returned with analyzed URLs and similarity scores.

## Technologies

- Python
- Flask
- Flask-CORS
- Requests
- BeautifulSoup4
- NLTK
- scikit-learn
- MySQL Connector/Python
- HTML, CSS, and JavaScript
- Tailwind CSS via CDN

## Repository structure

```text
.
├── API.py                         # Flask server and application routes
├── Complete.py                    # Main search, cleaning, and similarity pipeline
├── Database.py                    # Optional integration with a local MySQL database
├── text_filter.py                 # HTML-to-clean-text conversion helper
├── Neural.py                      # Standalone text similarity experiment
├── google_requester.py            # Helper script for testing Google search requests
├── web_downloader.py              # Helper script for downloading HTML pages
├── requirements_installer.py      # Legacy installer used during the fair
├── requirements.txt               # Recommended Python dependencies
├── .env.example                   # Environment variable example file
└── Site/                          # Prototype HTML screens and JavaScript
```

## Running locally

### 1. Create and activate a virtual environment

```bash
python -m venv .venv
source .venv/bin/activate
```

On Windows PowerShell:

```powershell
python -m venv .venv
.\.venv\Scripts\Activate.ps1
```

### 2. Install dependencies

```bash
pip install -r requirements.txt
```

### 3. Configure environment variables

Copy the example file:

```bash
cp .env.example .env
```

Then fill in your Google Custom Search API credentials:

```env
GOOGLE_API_KEY=your_google_api_key
GOOGLE_SEARCH_ENGINE_ID=your_search_engine_id
```

The MySQL integration is optional. To enable it, also configure:

```env
MYSQL_HOST=127.0.0.1
MYSQL_USER=root
MYSQL_PASSWORD=
MYSQL_DATABASE=ScienceFair
```

### 4. Start the application

```bash
python API.py
```

By default, the server runs at:

```text
http://localhost:80
```

> On some systems, port `80` requires administrator permissions. If needed, change the port in `API.py` to `5000` for local testing.

## Main endpoints

| Route | Description |
| --- | --- |
| `/` | Home page |
| `/check` | Choice screen for URL or text/title analysis |
| `/url` | URL analysis form |
| `/title` | Text/title analysis form |
| `/send_url?data=...` | Receives a URL, downloads its content, and analyzes similarity |
| `/send_title?data=...` | Receives text/title content and analyzes similarity |

## Important notes

- This repository was organized for portfolio/resume presentation while preserving the original school project idea.
- API keys should not be committed to source code. Use environment variables or a local `.env` file.
- The similarity score does not replace professional journalistic fact-checking.
- Some scripts are experimental and were kept to show the development process.

## Future improvements

- Improve API error handling and JSON responses.
- Add automated tests.
- Create a more complete configuration layer.
- Replace manually assembled SQL strings with parameterized queries.
- Add Docker support for easier setup.
- Create a more consistent responsive design.
- Include more transparent trust criteria and reliable source selection.

## Authors

- Arthur Witt
- Yuri Sirtoli
- Rafael Becker

## License

This project does not have a defined license yet. Before publicly reusing the code, consider adding a `LICENSE` file to the repository.
