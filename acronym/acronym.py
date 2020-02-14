def abbreviate(words: str):
    wl = []
    ret = ""
    for word in words.replace('-', ' ').replace('_', '').replace(',', '').split():
        wl.append(word)
    for word in wl:
        ret += (word[0].upper())
    return(ret)


