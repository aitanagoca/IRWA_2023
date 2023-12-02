from collections import defaultdict, Counter
from array import array
import math
import numpy as np
from numpy import linalg as la
import collections
from myapp.search.load_corpus import build_terms

def create_index_tfidf(documents):
    index = defaultdict(list)
    tf = defaultdict(list)
    df = Counter()
    idf = defaultdict(float)

    total_documents = len(documents)

    for document_id, document in documents.items():
        pp_tt = ' '.join(document.preprocessed_tweet)
        terms = build_terms(pp_tt)

        unique_terms = set(terms)
        term_positions = {term: [document_id, np.array([pos for pos, t in enumerate(terms) if t == term], 'I')] for term in unique_terms}

        doc_length = sum(len(posting[1]) for posting in term_positions.values())
        doc_length_sqrt = math.sqrt(doc_length)

        for term, posting in term_positions.items():
            tf_value = np.round(len(posting[1]) / doc_length_sqrt, 4)
            tf[term].append(tf_value)
            df[term] += 1
            index[term].append(posting)

    for term in df:
        idf[term] = np.round(np.log(total_documents / df[term]), 4)

    return index, tf, df, idf

def rank_documents(terms, docs, index, idf, tf):
    """
    Perform the ranking of the results of a search based on the tf-idf weights

    Argument:
    terms -- list of query terms
    docs -- list of documents, to rank, matching the query
    index -- inverted index data structure
    idf -- inverted document frequencies
    tf -- term frequencies
    title_index -- mapping between page id and page title

    Returns:
    Print the list of ranked documents
    """

    doc_vectors = defaultdict(lambda: [0] * len(terms))
    query_vector = [0] * len(terms)

    query_terms_count = collections.Counter(terms)

    query_norm = la.norm(list(query_terms_count.values()))

    for termIndex, term in enumerate(terms):
        if term not in index:
            continue

        query_vector[termIndex]=(query_terms_count[term] / query_norm) * idf[term]

        for doc_index, (doc, postings) in enumerate(index[term]):
            if doc in docs:
                doc_vectors[doc][termIndex] = tf[term][doc_index] * idf[term]

    doc_scores=[[np.dot(curDocVec, query_vector), doc] for doc, curDocVec in doc_vectors.items() ]
    doc_scores.sort(reverse=True)

    return doc_scores

def search_tf_idf(query, index, idf, tf):
    """
    output is the list of documents that contain any of the query terms.
    So, we will get the list of documents for each query term, and take the union of them.
    """
    query = build_terms(query)
    docs = set()
    for term in query:
        try:
            # store in term_docs the ids of the docs that contain "term"
            term_docs=[posting[0] for posting in index[term]]

            # docs = docs Union term_docs
            docs = docs.union(set(term_docs))
        except:
            #term is not in index
            pass
    docs = list(docs)
    doc_scores = rank_documents(query, docs, index, idf, tf)
    return doc_scores

def search_in_corpus(query, corpus):
    # 1. create create_tfidf_index
    index, tf, df, idf = create_index_tfidf(corpus)

    # 2. apply ranking
    doc_scores = search_tf_idf(query, index, idf, tf)
    
    return doc_scores 
