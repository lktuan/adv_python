from utils import print_scaling

if __name__ == "__main__":
    print_scaling("collection.pop()", setup="collection = list(range({N}))")
    print_scaling("collection.pop(0)", setup="collection = list(range({N}))")
    print_scaling("collection.append(1)", setup="collection = list(range({N}))")
    print_scaling("collection.insert(0, 1)", setup="collection = list(range({N}))")
    print_scaling("collection.insert(5000, 1)", setup="collection = list(range({N}))")
