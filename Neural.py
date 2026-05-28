print("Importing libraries")
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.metrics.pairwise import cosine_similarity
import nltk
from nltk.corpus import stopwords
import string

print("Setting variables")
text_1 = "The cat is sleeping on the living room sofa."
text_2 = "A cat sleeps peacefully on the sofa."

print("Downloading stopwords...")
nltk.download("stopwords")

print("Done!")
def preprocess_text(text):
    print("Preprocessing text")
    stop_words = set(stopwords.words("english"))
    text = text.lower()
    text = "".join([char for char in text if char not in string.punctuation])
    words = text.split()
    words = [word for word in words if word not in stop_words]
    return " ".join(words)


print("Processing data...")
text_1 = preprocess_text(text_1)
text_2 = preprocess_text(text_2)
vector = CountVectorizer().fit_transform([text_1, text_2])

similarity = cosine_similarity(vector[0], vector[1])[0][0] * 100

print(f"Similarity: {similarity:.2f}%")
