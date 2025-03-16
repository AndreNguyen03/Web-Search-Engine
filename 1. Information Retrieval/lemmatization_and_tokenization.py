import nltk
from nltk.stem import WordNetLemmatizer
nltk.download('punkt_tab')
nltk.download('wordnet')

# Tokenization
sentence = "The bats were hanging by their feet"
tokenization_words = nltk.word_tokenize(sentence)

print(f"Tokenized sentence = {tokenization_words}")

lemmatizer = WordNetLemmatizer()

lemmatized_words = [lemmatizer.lemmatize(word) for word in tokenization_words]

print(f"Lemmatized words = {lemmatized_words}")