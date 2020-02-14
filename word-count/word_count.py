##
## EPITECH PROJECT, 2019
## word-count
## File description:
## word_count.py
##

def count_words(sentence: str):
    sentence = sentence.lower().replace(',', ' ').replace('.', '').replace('_', ' ').replace('\t', ' ').replace("''", "").replace("!!&@$%^&", "").replace(":", "").split()
    all_words = {}
    for words in sentence:
        if words.startswith("'") and words.endswith("'"):
            sentence[sentence.index(words)] = words[1:-1]
            words = words[1:-1]
        all_words[words] = sentence.count(words)
    return(all_words) 

print(count_words("car: carpet as java: javascript!!&@$%^&"))