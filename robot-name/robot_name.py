import random
from datetime import datetime

class Robot:
    def make_name(self):
        return random.choice("ABCDEFGHIJKLMNOPQRSTUVWXYZ") + random.choice("ABCDEFGHIJKLMNOPQRSTUVWXYZ") + str(random.randrange(100, 999))
    def __init__(self):
        random.seed(datetime.now())
        self.name = self.make_name()
        print(self.name)

    def reset(self):
        self.name = self.make_name()