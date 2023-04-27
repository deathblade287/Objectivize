from keybert import KeyBERT
def keywordExtracter(doc):    
    kw_model = KeyBERT()
    keywords = kw_model.extract_keywords(doc, keyphrase_ngram_range=(1, 3))
    keywords_final = []
    for i in range(len(keywords)):
        data_tu = keywords[i]
        if data_tu[1] > 0.3 and "search" not in data_tu[0]:
            keywords_final.append(data_tu[0])
    return keywords_final

if __name__ == '__main__':
    doc = """
            Supervised learning is the machine learning task of learning a function that
            maps an input to an output based on example input-output pairs. It infers a
            function from labeled training data consisting of a set of training examples.
            In supervised learning, each example is a pair consisting of an input object
            (typically a vector) and a desired output value (also called the supervisory signal).
            A supervised learning algorithm analyzes the training data and produces an inferred function,
            which can be used for mapping new examples. An optimal scenario will allow for the
            algorithm to correctly determine the class labels for unseen instances. This requires
            the learning algorithm to generalize from the training data to unseen situations in a
            'reasonable' way (see inductive bias).
        """
    print(keywordExtracter(doc))