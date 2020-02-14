def is_pangram(sentence: str):
    alphabet = 'abcdefhijklmnopqrstuvwxz'
    alphabetupper = alphabet.upper()
    for i in range(len(alphabet)):
        if not alphabet[i] in sentence and not alphabetupper[i] in sentence:
            return False
    return True