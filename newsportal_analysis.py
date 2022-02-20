from collections import Counter

word_list = open("titles.txt", "r", encoding="utf-8").read().split()
word_dict = Counter(word_list)

stop_word_list = open("stop-word.txt", "r", encoding="utf-8").read().split()
stop_word_dict = Counter(stop_word_list)

c = {k:v for k,v in word_dict.items() if k not in stop_word_dict}
top_counts = Counter(c).most_common()[:22]
print(top_counts)