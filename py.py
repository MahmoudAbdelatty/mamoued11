import re
from collections import Counter 
stop_words = set(["the","and","or","but","to","of","a","an","in","on","for","with","as","by","at"])

with open('random_paragraphs.txt','r') as file:
    file.read
    words = re.findall(r'\b\w+\b ', file.read()) 

    filtered_words =[word for word in words if word not in stop_words]
    filtered_words

    word_freq= Counter(words)
for word ,freq in word_freq.items():
    print(f'{word}:{freq}')