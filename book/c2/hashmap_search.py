docs = [
    "the cat is under the table",
    "the dog is under the table",
    "cats and dogs smell roses",
    "Carla eats an apple",
]

# using list conprehension
matches = [doc for doc in docs if "table" in doc]

# building an inverted index
index = {}
for i, doc in enumerate(docs):
    # we iterate over each term of the document
    for word in doc.split():
        # we build a list containing the indices
        # where the term appears
        if word not in index:
            index[word] = [i]
        else:
            index[word].append(i)

results = index["table"]
result_documents = [docs[i] for i in results]
