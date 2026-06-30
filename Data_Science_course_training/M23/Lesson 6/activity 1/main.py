import pandas as pd
import numpy as np
import nltk
import random
from nltk.tokenize import sent_tokenize
from sklearn.metrics.pairwise import cosine_similarity
import networkx as nx
from termcolor import colored

nltk.download('punkt')
nltk.download('stopwords')

df = pd.read_csv("tennis.csv")

i = random.randint(0, len(df) - 1)
print("Selected article:")
print(df['article_text'][i])
print("\n" + "=" * 80 + "\n")

sentences = []
for s in df['article_text']:
    sentences.append(sent_tokenize(s))
sentences = [y for x in sentences for y in x]

word_embeddings = {}
f = open('glove.6B.300d.txt', encoding='utf-8')
for line in f:
    values = line.split()
    word = values[0]
    coefs = np.asarray(values[1:], dtype='float32')
    word_embeddings[word] = coefs
f.close()

clean_sentences = pd.Series(sentences).str.replace("[^a-zA-Z]", " ")
clean_sentences = [s.lower() for s in clean_sentences]

from nltk.corpus import stopwords
stop_words = stopwords.words('english')

def remove_stopwords(sen):
    return " ".join([w for w in sen if w not in stop_words])

clean_sentences = [remove_stopwords(r.split()) for r in clean_sentences]

sentence_vectors = []
for s in clean_sentences:
    if len(s) != 0:
        v = sum([word_embeddings.get(w, np.zeros((300,))) for w in s.split()]) / (len(s.split()) + 0.001)
    else:
        v = np.zeros((300,))
    sentence_vectors.append(v)

sim_mat = np.zeros([len(sentences), len(sentences)])
for i in range(len(sentences)):
    for j in range(len(sentences)):
        if i != j:
            sim_mat[i][j] = cosine_similarity(
                sentence_vectors[i].reshape(1, 300),
                sentence_vectors[j].reshape(1, 300)
            )[0, 0]

nx_graph = nx.from_numpy_array(sim_mat)
scores = nx.pagerank(nx_graph)

ranked_sentences = sorted(((scores[i], s) for i, s in enumerate(sentences)), reverse=True)

print(colored("ARTICLE:".center(80), 'yellow'))
print(colored(df['article_text'][i], 'blue'))
print()
print(colored("SUMMARY:".center(80), 'green'))
print(colored(ranked_sentences[0][1], 'cyan'))
