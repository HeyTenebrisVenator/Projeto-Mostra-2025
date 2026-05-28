from bs4 import BeautifulSoup
from nltk.corpus import stopwords
import nltk
import re

nltk.download("stopwords")


def html_to_clean_text(html, language="portuguese"):

    soup = BeautifulSoup(html, "html.parser")
    for tag in soup(["script", "style", "noscript"]):
        tag.extract()
    text = soup.get_text(separator=" ")
    text = re.sub(r"\s+", " ", text).strip()
    words = text.split()
    stop_words = set(stopwords.words(language))
    filtered_words = [word for word in words if word.lower() not in stop_words]
    clean_text = " ".join(filtered_words)
    clean_text = clean_text.replace(",", "").replace(".", "")

    return clean_text[:100]
