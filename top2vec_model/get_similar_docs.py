from top2vec import Top2Vec
import pandas as pd

data_with_names = pd.read_csv('data_with_names.csv')

def get_similar_doc(str_str):
    model_ttl = Top2Vec.load('model_deep_L')
    res = list(model_ttl.query_documents(str_str, num_docs=3))[2]
    sim_docs = []
    for i in range(len(res)):
        sim_docs.append(data_with_names['name'][res[i]])
    return sim_docs
