class Luhn:
    def __init__(self, card_num: str):
        self.card_num = card_num

    def valid(self):
        if self.card_num[0] == " ":
            return False
        print(self.card_num.replace(' ', ''))
        try:
            int(self.card_num.replace(' ', ''))
        except:
            return False
        self.card_num = self.card_num.replace(' ', '')
        val = sum([sum(map(int,str(int(v)*2))) if self.card_num%2 else int(v) for self.card_num,v in enumerate(self.card_num)])
        print(int(val))
        if val % 10 == 0:
            return True
        else:
            return False