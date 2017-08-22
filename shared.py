from enum import Enum, auto

class Relation(Enum):
    neutral = auto(),
    friend = auto(),
    enemy = auto()

class memberdata:
    def __init__(self, name, rela = None, nick = None):
        self.name = name
        self.relationship = rela
        self.nickname = nick

    def __str__(self):
        return "{0}, '{1}'. Prefers {2} ".format(self.name, self.relationship, self.nickname)
