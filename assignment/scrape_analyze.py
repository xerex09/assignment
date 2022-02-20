from collections import Counter, OrderedDict
word_list = open("corpus.txt", "r").read().split()
word_dict = Counter(word_list)