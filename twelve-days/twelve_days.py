days = [ 
    "first", "second", "third", "fourth", "fifth", "sixth", 
    "seventh", "eighth", "ninth", "tenth", "eleventh", "twelfth" 
]

gifts = [
    "a Partridge in a Pear Tree.",
    "two Turtle Doves, ",
    "three French Hens, ",
    "four Calling Birds, ",
    "five Gold Rings, ",
    "six Geese-a-Laying, ",
    "seven Swans-a-Swimming, ",
    "eight Maids-a-Milking, ",
    "nine Ladies Dancing, ",
    "ten Lords-a-Leaping, ",
    "eleven Pipers Piping, ",
    "twelve Drummers Drumming, "
]

def verse(i):
    line = "On the {} day of Christmas my true love gave to me: ".format(days[i-1])
    for j in range(i, 0, -1):
        if j == 1 and i != 1:
            line += "and " + gifts[j-1]
        else:
            line += gifts[j-1]
    return line

def recite(start_verse, end_verse):
    return [verse(i) for i in range(start_verse, end_verse+1)]