def is_valid(isbn):
    isbn = list(isbn.replace('-', ''))

    if len(isbn) != 10:
        return False

    if isbn[-1].upper() == 'X':
        isbn[-1] = '10'

    total = 0

    for i in range(10):
        try:
            total += int(isbn[i])*(10-i)
        except:
            return False

    return total % 11 == 0