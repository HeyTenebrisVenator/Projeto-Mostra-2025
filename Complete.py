print("Importando bibliotecas")
import requests
import filtrador
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.metrics.pairwise import cosine_similarity
import nltk
from nltk.corpus import stopwords
import string

def preprocessar(texto):
    print("Realizando pré-processamento")
    stop_words = set(stopwords.words("portuguese"))
    try:
        texto = texto.lower()
        texto = "".join([c for c in texto if c not in string.punctuation])
        palavras = texto.split()
        palavras = [p for p in palavras if p not in stop_words]
        return " ".join(palavras)
    except:
        pass





def body(corpo):
    corpo = corpo.lower()
    tamanho = corpo.split(" ")
    tamanho = len(tamanho)
    total_calculo = 0
    print("Fazendo Download das stopwords...")
    nltk.download("stopwords")
    print("Coletando primeiras linhas do corpo da notícia")
    part_1 = corpo
    if tamanho >= 50:
        part_1 = part_1[:50]
    print("definindo corpo da notícia")
    API_KEY = '#API OCULTA#'
    SEARCH_ENGINE_ID = '30854cad23c464de8'
    query = part_1.replace(" ","+")
    url = f'https://www.googleapis.com/customsearch/v1?q={query}+-site:agenciabrasil.ebc.com.br+-site:*.instagram.com&key={API_KEY}&cx={SEARCH_ENGINE_ID}'
    print(url)
    print("Feito")
    response = requests.get(url, timeout=5)
    print("Feito")
    data = response.json()
    lista_verificada = []
    lista_urls = []
    for item in data.get('items', []):
        try:
            lista_urls.append(item['link'])
            noticia = requests.get(item['link'], timeout=5).text
            noticia = filtrador.html_para_texto_limpo(noticia)
            noticia = noticia.split()
            noticia = set(noticia)
            final = ""
            for dados in noticia:
                final = f"{final} {dados}"
            noticia = final.lower()
        except:
            print("Houve algum erro")
            pass
        print("Verificando semelhança")
        print("Processando dados...")
        texto1 = preprocessar(noticia)
        texto2 = preprocessar(corpo)
        vetor = CountVectorizer().fit_transform([texto1, texto2])

        similaridade = cosine_similarity(vetor[0], vetor[1])[0][0] * 100
        print(f"Similaridade: {similaridade:.2f}%")
        sim = float(f"{similaridade:.2f}")
        lista_verificada.append(f"{similaridade:.2f}")
        print(sim)
        total_calculo += sim 
    report = f"REPORT FINAL:<br><br>Número de páginas coletadas: 5<br>URLs analisadas: {lista_urls[0]}'  -  Similaridade: {lista_verificada[0]}'<br>{lista_urls[1]}  -  Similaridade: {lista_verificada[1]}<br>{lista_urls[2]}  -  Similaridade: {lista_verificada[2]}<br>{lista_urls[3]}  -  Similaridade: {lista_verificada[3]}<br>{lista_urls[4]}  -  Similaridade: {lista_verificada[4]}<br>Resultado da análise: <br><h1 style=\"color: rgb(0, 0, 300);\">{total_calculo}"
    return report
def url(url):
    print("Requisitando URL")
    noticia = requests.get(url, timeout=5).text
    noticia = filtrador.html_para_texto_limpo(noticia)

    body(noticia)
