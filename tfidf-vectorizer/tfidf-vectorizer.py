import numpy as np
import math

def tfidf_vectorizer(documents):
    # Sorted vocab
    vocab = sorted(set(word for d in documents for word in d.split()))

    N = len(documents)

    # IDF
    idf = []
    for v in vocab:
        doc_count = sum(1 for d in documents if v in d.split())
        idf.append(math.log(N / doc_count))

    # TF-IDF
    tfidf_matrix = []

    for d in documents:
        words = d.split()
        vec = []

        for i, v in enumerate(vocab):
            tf = words.count(v) / len(words)   
            vec.append(tf * idf[i])

        tfidf_matrix.append(vec)

    return np.array(tfidf_matrix), vocab