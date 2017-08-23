from enum import Enum, auto

class Relation(Enum):
    neutral = auto(),
    friend = auto(),
    enemy = auto()

class memberdata:
    def __init__(self, name, rela = None, nick = None):
        self.name = name
        self.nickname = nick
        self.relationship = None
        if rela is not None:
            for name, member in Relation.__members__.items():
                if rela == name:
                    self.relationship = member
                    break

    def __str__(self):
        return "{0}, '{1}'. Prefers {2} ".format(self.name, self.relationship, self.nickname)
