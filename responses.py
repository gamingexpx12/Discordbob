import random
import botdb as db
from shared import Relation

def _getrandom(list_):
    if list_ is None: raise TypeError("NoneType is not an iterable")
    pos = random.randint(0, len(list_) - 1)
    return list_[pos]

#Get relationship with user
def relationwith(member):
    mem = db.findmember(member)
    if mem is not None:
        return mem.relationship

def choosebyrelation(relation, neutral, unknown, friend, enemy):
    if relation == Relation.friend:
        return friend
    elif relation == Relation.enemy:
        return enemy
    elif relation == Relation.neutral:
        return neutral
    else:
        return unknown

def getpraise():
    return _getrandom(praise)

def listening(member):
    rel = relationwith(member)
    responselist = choosebyrelation(rel, listen, listen_unknown, listen_friend, listen_enemy)
    return _getrandom(responselist).format(getname(member))

def getscold():
    return _getrandom(scold)

def getname(member):
    name = str(member)
    botdb.findmember()
    if name in nicknames:
        return nicknames[name]
    else:
        return member.display_name

def setnickname(member, nickname):
    nicknames[str(member)] = nickname

#Relationships
relations = {
'gamingexpx12#8267': Relation.friend,
"Sarim_Cast#6706" : Relation.enemy,
"Sir_Lagalotやった#5602" : Relation.enemy
}

nicknames = {
'gamingexpx12#8267': 'Boss',
"Sarim_Cast#6706" : 'El Presidente',
}

praise = [
"Much obliged",
"I do my best",
"Glad you like it!",
"Thank you, thank you, I'll be here all day"
]
listen = [
"I'm all ears, {0}",
"I'm here, {0}",
"I'm listening, {0}",
]
listen_unknown = [
"Nice to meet you, {0}, what do you need?",
"You look new, {0}, how can i help?",
"I'm listening, {0}",
]
listen_friend = [
"You know I'm listening, {0}",
"You called, {0}?",
"lis-ten-ing~",
"Say the word, {0}"
]
listen_enemy = [
"What do YOU want, {0}?",
"What now, {0}?",
"Get on with it, {0}"
]

scold = [
"Yeah, that was pretty terrible...",
"Not my finest hour..."
]
