def is_valid(isbn: str):
    number = 0
    isbn = isbn.replace('-', '')
    if len(isbn) < 10:
        return False
    for i in range(10):
        try:
            number += int(isbn[i] * (10-i))
        except: 
            return False
    return number % 11 == 0
