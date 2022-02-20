from collections import Counter
import matplotlib.pyplot as plt
from matplotlib.font_manager import FontProperties

word_list = open("titles.txt", "r", encoding="utf-8").read().split()
word_dict = Counter(word_list)
stop_word_list = open("stop-word.txt", "r", encoding="utf-8").read().split()
stop_word_dict = Counter(stop_word_list)
c = {k:v for k,v in word_dict.items() if k not in stop_word_dict}
top_hits = Counter(c).most_common()[:20]
top_words = dict(top_hits)
val_val = top_words.values()
key_val = top_words.keys()  
for i,j in top_hits:
    print(i,"->",j)
ax = plt.subplot()
font_prop = FontProperties(fname='C:\Windows\Fonts\mangal.ttf', size=18)
for label in (ax.get_xticklabels() + ax.get_yticklabels()):
    label.set_fontproperties(font_prop)
    label.set_fontsize(15)  # Size here overrides font_prop
fig= plt.scatter (key_val,val_val)
plt.title("Top words")
plt.grid(True)
plt.show()