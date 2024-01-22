import random
import time


class Dice:
    def __init__(self):
        random.seed(time.time())

    def roll(self):
        return random.randint(1, 6)
