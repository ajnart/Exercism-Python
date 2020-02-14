def is_valid(isbn: str):
    res = [int(i) for i in isbn.split() if i.isdigit()] 
    print(res)


    # if (x[0] * 10 + x[1] * 9 + x[2] * 8 + x[3] * 7 + x[4] * 6 + x[5] * 5 + x[6] * 4 + x[7] * 3 + x[8] * 2 + x[9] * 1) % 11 == 0:
    #     return True
    # else:
    #     return False
