# Fake News Detection System — Science Fair 2025

This project was developed for the 2025 School Science Fair, where it was awarded **1st place**. The goal was to create a web-based prototype capable of assisting users in evaluating news credibility by comparing submitted content against related information found online and calculating similarity scores between texts.

> **Disclaimer:** This project is an academic and educational prototype. Its results should not be interpreted as definitive evidence that a news article is true or false. Instead, it is intended to support critical thinking and further investigation.

## Project Overview

Misinformation has become an increasingly significant challenge in the digital age. This project explores how basic Natural Language Processing (NLP) techniques can be applied to assist in the analysis of news articles and online content.

The system accepts either a URL or a text headline, searches for related content on the web, processes the collected information, and calculates similarity metrics between the original submission and external sources.

## Features

* Simple web interface built with HTML, CSS, and JavaScript.
* Flask-based backend API.
* Analysis through either URLs or text headlines.
* Integration with Google Custom Search API for related content retrieval.
* HTML content extraction using BeautifulSoup.
* Portuguese stopword removal using NLTK.
* Text vectorization with CountVectorizer.
* Cosine similarity calculation using scikit-learn.
* Optional MySQL integration for storing analysis results.

## System Workflow

1. The user submits a URL or a news headline.
2. The backend extracts or receives the textual content.
3. The application searches for related articles using Google Custom Search.
4. Retrieved pages are downloaded and converted into clean text.
5. The original content and collected texts undergo preprocessing.
6. Similarity scores are calculated between the documents.
7. An HTML report is generated displaying analyzed sources and similarity results.

## Technologies Used

### Backend

* Python
* Flask
* Flask-CORS
* Requests
* BeautifulSoup4
* NLTK
* scikit-learn
* MySQL Connector/Python

### Frontend

* HTML
* CSS
* JavaScript
* Tailwind CSS (CDN)

## Repository Structure

```text
.
├── API.py                         # Flask server and application routes
├── Complete.py                    # Main similarity analysis pipeline
├── Database.py                    # Optional MySQL integration
├── filtrador.py                   # HTML-to-text processing module
├── Neural.py                      # Experimental text similarity module
├── google_requester.py            # Google Search API testing utility
├── web_downloader.py              # HTML page downloader
├── Instalador_de_requerimentos.py # Legacy dependency installer
├── requirements.txt               # Python dependencies
├── .env.example                   # Environment variables template
└── Site/                          # Frontend pages and assets
```

## Running Locally

### Create a Virtual Environment

```bash
python -m venv .venv
source .venv/bin/activate
```

Windows PowerShell:

```powershell
python -m venv .venv
.\.venv\Scripts\Activate.ps1
```

### Install Dependencies

```bash
pip install -r requirements.txt
```

### Configure Environment Variables

Copy the example file:

```bash
cp .env.example .env
```

Then configure your Google Custom Search credentials:

```env
GOOGLE_API_KEY=your_google_api_key
GOOGLE_SEARCH_ENGINE_ID=your_search_engine_id
```

MySQL support is optional. To enable it, configure:

```env
MYSQL_HOST=127.0.0.1
MYSQL_USER=root
MYSQL_PASSWORD=
MYSQL_DATABASE=Mostra
```

### Start the Application

```bash
python API.py
```

By default, the server runs on:

```text
http://localhost:80
```

Depending on your operating system, port 80 may require administrator privileges. During development, changing the application port to 5000 is recommended.

## Main Endpoints

| Endpoint               | Description                             |
| ---------------------- | --------------------------------------- |
| `/`                    | Home page                               |
| `/check`               | Analysis mode selection                 |
| `/url`                 | URL analysis page                       |
| `/title`               | Text/headline analysis page             |
| `/send_url?data=...`   | Analyzes content from a URL             |
| `/send_title?data=...` | Analyzes content from a text submission |

## Important Notes

* This repository has been reorganized and documented to better showcase the project as part of a portfolio.
* API credentials should never be committed to version control.
* Similarity scores should not be interpreted as proof of authenticity.
* Several auxiliary scripts were intentionally preserved to illustrate the project's development process and experimentation.

## Future Improvements

Potential areas for future development include:

* Improved error handling and API responses.
* Automated testing.
* More robust configuration management.
* Parameterized SQL queries and database security improvements.
* Docker containerization.
* Enhanced responsive design.
* Integration of trusted fact-checking sources.
* More transparent credibility assessment criteria.
* Advanced NLP models and semantic similarity techniques.

## Authors

* Arthur Witt
* Yuri Sirtoli
* Rafael Becker

## Academic Context

This project was originally created as part of a high school science fair initiative and served as an introduction to Natural Language Processing, information retrieval, and web application development. It represents an early exploration of how machine learning and data analysis techniques can be applied to real-world challenges such as misinformation detection.
