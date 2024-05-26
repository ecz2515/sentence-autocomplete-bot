import nltk
from nltk.corpus import (gutenberg, brown, reuters, inaugural, stopwords, 
                         webtext, nps_chat, movie_reviews)
from nltk.tokenize import word_tokenize
from nltk.stem import WordNetLemmatizer
import re
from collections import defaultdict, Counter
import pickle
from tqdm import tqdm

# Download necessary NLTK resources
nltk.download('gutenberg')
nltk.download('brown')
nltk.download('reuters')
nltk.download('inaugural')
nltk.download('webtext')
nltk.download('nps_chat')
nltk.download('movie_reviews')
nltk.download('punkt')
nltk.download('stopwords')
nltk.download('wordnet')

# Preprocessing function with better cleaning
def preprocess_text(text):
    text = text.lower()
    text = re.sub(r'\d+', '', text)  # Remove digits
    text = re.sub(r'\s+', ' ', text)  # Replace multiple spaces with a single space
    text = re.sub(r'\W', ' ', text)   # Replace all non-word characters with a space
    tokens = word_tokenize(text)
    tokens = [word for word in tokens if word not in stopwords.words('english') and word.isalpha()]
    lemmatizer = WordNetLemmatizer()
    tokens = [lemmatizer.lemmatize(word) for word in tokens]
    return tokens

# Build n-gram model function with progress tracking
def build_ngram_model(tokens, n):
    model = defaultdict(Counter)
    for i in tqdm(range(len(tokens) - n + 1), desc=f"Building {n}-gram model"):
        ngram = tuple(tokens[i:i+n-1])
        next_word = tokens[i+n-1]
        model[ngram][next_word] += 1
    return model

# Function to load and preprocess datasets with progress tracking
def load_and_preprocess_datasets():
    datasets = [
        ('gutenberg', gutenberg),
        ('brown', brown),
        ('reuters', reuters),
        ('inaugural', inaugural),
        ('webtext', webtext),
        ('nps_chat', nps_chat),
        ('movie_reviews', movie_reviews)
    ]
    all_texts = []
    for name, dataset in datasets:
        for fileid in tqdm(dataset.fileids(), desc=f"Loading {name} files"):
            all_texts.append(dataset.raw(fileid))
    return ' '.join(all_texts)

# Function to preprocess the entire text with progress tracking
def preprocess_with_progress(text):
    # Split the text into chunks for progress tracking
    chunk_size = 100000  # Adjust this based on memory and processing capacity
    chunks = [text[i:i + chunk_size] for i in range(0, len(text), chunk_size)]
    tokens = []
    for chunk in tqdm(chunks, desc="Preprocessing text"):
        tokens.extend(preprocess_text(chunk))
    return tokens

# Load and preprocess your dataset here
print("Loading and preprocessing datasets...")
texts = load_and_preprocess_datasets()

print("Preprocessing text...")
tokens = preprocess_with_progress(texts)

# Build bigram and trigram models
print("Building bigram model...")
bigram_model = build_ngram_model(tokens, 2)

print("Building trigram model...")
trigram_model = build_ngram_model(tokens, 3)

# Save models to disk
print("Saving models to disk...")
with open('bigram_model.pkl', 'wb') as f:
    pickle.dump(bigram_model, f)

with open('trigram_model.pkl', 'wb') as f:
    pickle.dump(trigram_model, f)

print("Models have been saved to disk.")
