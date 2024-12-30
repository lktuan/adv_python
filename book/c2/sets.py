docs = [
    "the cat is under the table",
    "the dog is under the table",
    "cats and dogs smell roses",
    "Carla eats an apple",
]

# Building an index using sets
index = {}
for i, doc in enumerate(docs):
    # We iterate over each term in the document
    for word in doc.split():
        # We build a set containing the indices
        # where the term appears
        if word not in index:
            index[word] = {i}
        else:
            index[word].add(i)
# Querying the documents containing both "cat" and "table"
print(index["cat"].intersection(index["table"]))
