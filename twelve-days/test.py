def recite(start_verse: int, end_verse: int):
    ret = []
    ret.append("On the first day of Christmas my true love gave to me: ")
    ret[0] += "a Partridge in a Pear Tree."
    print(ret)
    return (ret)

if __name__ == "__main__":
    recite(1, 1)