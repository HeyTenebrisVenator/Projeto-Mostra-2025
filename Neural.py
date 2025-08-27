print("Importando bibliotecas")
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.metrics.pairwise import cosine_similarity
import nltk
from nltk.corpus import stopwords
import string

print("Setando variáveis")
texto1 = "O gato está dormindo no sofá da sala."
texto2 = "Um gato dorme tranquilamente no sofá."

print("Fazendo Download das stopwords...")
nltk.download("stopwords")

print("Feito!")
def preprocessar(texto):
    print("Realizando pré-processamento")
    stop_words = set(stopwords.words("portuguese"))
    texto = texto.lower()
    texto = "".join([c for c in texto if c not in string.punctuation])
    palavras = texto.split()
    palavras = [p for p in palavras if p not in stop_words]
    return " ".join(palavras)



print("Processando dados...")
texto1 = preprocessar(texto1)
texto2 = preprocessar(texto2)
vetor = CountVectorizer().fit_transform([texto1, texto2])

similaridade = cosine_similarity(vetor[0], vetor[1])[0][0] * 100

print(f"Similaridade: {similaridade:.2f}%")