from bs4 import BeautifulSoup
from nltk.corpus import stopwords
import nltk
import re

nltk.download("stopwords")


def html_para_texto_limpo(html, idioma="portuguese"):

    soup = BeautifulSoup(html, "html.parser")
    for tag in soup(["script", "style", "noscript"]):
        tag.extract()
    texto = soup.get_text(separator=" ")
    texto = re.sub(r"\s+", " ", texto).strip()
    palavras = texto.split()
    stop_words = set(stopwords.words(idioma))
    palavras_filtradas = [p for p in palavras if p.lower() not in stop_words]
    texto_limpo = " ".join(palavras_filtradas)
    texto_limpo = texto_limpo.replace(",", "").replace(".", "")



    return texto_limpo[:100]
