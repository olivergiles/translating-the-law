from transformers import pipeline

def test():
    test = pipeline("question-answering", model="/models/questions-pretrained")
    ARTICLE = "My name is Oliver and I love in London"
    QUESTION = "What is my name?"
    input = {
        "question": QUESTION,
        "context": ARTICLE
    }
    return test(input)

if __name__ == "__main__":
    print(test())