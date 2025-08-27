import requests

url = "https://www.bbc.com/portuguese/articles/cj6y0ypw98po"
html = requests.get(url).text

# salvar como html
try:
    open("data_" + url.replace("https://", "").replace("http://", "").split("/")[0] + ".html", "a", encoding='utf-8').write(html)
except Exception as e:
    print("Houve algum erro...\nInformações: " + e)
# salvar como txt
open("data_" + url.replace("https://", "").replace("http://", "").split("/")[0] + ".txt", "a", encoding='utf-8').write(html)
