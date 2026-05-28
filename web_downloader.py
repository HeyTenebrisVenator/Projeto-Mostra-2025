import requests

url = "https://www.bbc.com/news"
html = requests.get(url).text

# save as HTML
try:
    open("data_" + url.replace("https://", "").replace("http://", "").split("/")[0] + ".html", "a", encoding='utf-8').write(html)
except Exception as e:
    print("An error occurred...\nDetails: " + str(e))
# save as TXT
open("data_" + url.replace("https://", "").replace("http://", "").split("/")[0] + ".txt", "a", encoding='utf-8').write(html)
