print("Importing libraries")
import os
import string

import nltk
import requests
from dotenv import load_dotenv
from nltk.corpus import stopwords
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.metrics.pairwise import cosine_similarity

import Database
import text_filter

load_dotenv()


def preprocess_text(text):
    print("Preprocessing text")
    stop_words = set(stopwords.words("portuguese"))
    try:
        text = text.lower()
        text = "".join([char for char in text if char not in string.punctuation])
        words = text.split()
        words = [word for word in words if word not in stop_words]
        return " ".join(words)
    except Exception:
        pass


def body(article_body):
    article_body = article_body.lower()
    word_count = len(article_body.split(" "))
    total_score = 0
    print("Downloading stopwords...")
    nltk.download("stopwords")
    print("Collecting the first lines of the news body")
    query_excerpt = article_body
    if word_count >= 50:
        query_excerpt = query_excerpt[:50]
    print("Preparing the news body")
    api_key = os.getenv('GOOGLE_API_KEY')
    search_engine_id = os.getenv('GOOGLE_SEARCH_ENGINE_ID')
    if not api_key or not search_engine_id:
        return 'Configure GOOGLE_API_KEY and GOOGLE_SEARCH_ENGINE_ID before running the analysis.'
    query = query_excerpt.replace(" ", "+")
    search_url = f'https://www.googleapis.com/customsearch/v1?q={query}+-site:agenciabrasil.ebc.com.br+-site:*.instagram.com&key={api_key}&cx={search_engine_id}'
    print(search_url)
    print("Done")
    response = requests.get(search_url, timeout=5)
    print("Done")
    data = response.json()
    similarity_results = []
    analyzed_urls = []
    for item in data.get('items', []):
        try:
            analyzed_urls.append(item['link'])
            news_text = requests.get(item['link'], timeout=5).text
            news_text = text_filter.html_to_clean_text(news_text)
            news_words = set(news_text.split())
            final_text = ""
            for word in news_words:
                final_text = f"{final_text} {word}"
            news_text = final_text.lower()
        except Exception:
            print("An error occurred")
            pass
        print("Checking similarity")
        print("Processing data...")
        text_1 = preprocess_text(news_text)
        text_2 = preprocess_text(article_body)
        vector = CountVectorizer().fit_transform([text_1, text_2])

        similarity = cosine_similarity(vector[0], vector[1])[0][0] * 100
        print(f"Similarity: {similarity:.2f}%")
        similarity_value = float(f"{similarity:.2f}")
        similarity_results.append(f"{similarity:.2f}")
        print(similarity_value)
        total_score += similarity_value
    try:
        Database.save_in_db(f"INSERT INTO `science_fair_results` (`ID`, `Info`, `CreatedAt`, `Result`, `URL1`, `URL2`, `URL3`, `URL4`, `URL5`) VALUES (NULL, '{news_text}', current_timestamp(), '{total_score}', '{analyzed_urls[0]}', '{analyzed_urls[1]}', '{analyzed_urls[2]}', '{analyzed_urls[3]}', '{analyzed_urls[4]}');")
    except Exception:
        print("ERROR WHILE SAVING TO THE DATABASE")
    report = f"FINAL REPORT:<br><br>Number of collected pages: 5<br>Analyzed URLs: {analyzed_urls[0]}'  -  Similarity: {similarity_results[0]}'<br>{analyzed_urls[1]}  -  Similarity: {similarity_results[1]}<br>{analyzed_urls[2]}  -  Similarity: {similarity_results[2]}<br>{analyzed_urls[3]}  -  Similarity: {similarity_results[3]}<br>{analyzed_urls[4]}  -  Similarity: {similarity_results[4]}<br>Analysis result: <br><h1 style=\"color: rgb(0, 0, 300);\">{total_score}</h1>"
    return report


def url(article_url):
    print("Requesting URL")
    news_text = requests.get(article_url, timeout=5).text
    news_text = text_filter.html_to_clean_text(news_text)
    return body(news_text)
