def response(phrase: str):
    if phrase.isupper() and phrase.endswith('?'):
        return "Calm down, I know what I'm doing!"
    if phrase.isupper():
        return 'Whoa, chill out!'
    elif phrase.strip().endswith('?'):
        return 'Sure.'
    elif phrase.strip() == '':
        return 'Fine. Be that way!'
    else:
        return 'Whatever.'
