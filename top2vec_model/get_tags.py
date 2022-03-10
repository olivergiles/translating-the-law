from top2vec import Top2Vec

def get_tag(lst_str):
    model_ttl = Top2Vec.load("model_deep_L")
    res = model_ttl.search_topics(keywords = lst_str, num_topics=1)
    return list(res[0][0][:3])


if __name__ == "__main__":
    get_tag(["murder"])
