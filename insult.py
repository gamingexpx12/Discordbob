import random

def MakeText():
    sent = getrandom(sentences)
    args = {
     "noun" : getrandom(nouns),
     "obj" : getrandom(objects),
     "verb" : getrandom(verbs),
     "place" : getrandom(places),
     "adj" : getrandom(adjectives),
     "relative" : getrandom(relations),
     "compare" : getrandom(compareobjects),
     "person" : getrandom(people),
     "disease" : getrandom(diseases)
     }

    return sent.format(**args)

def getrandom(wlist):
    r = random.randint(0, len(wlist) - 1)
    return wlist[r]

sentences = ["Your {obj} looks like a {adj} {noun}",
             "Your {obj} is the worst {obj} I've ever seen",
             "Your {obj} looks like a {adj} {compare}",
             "Your {obj} looks like it came from {place}",
             "Your {relative}'s {obj} looks straight out of {media}",
             "You look like {person} just stepped on you",
             "You look like you have {disease}, only more {adj}",
             "Are you an actor? Because I think I saw you in transformers",
             "Are you an actor? Because you look like one of the zombies from Shaun of the Dead"]
verbs = ["move", "take", "covet", "eat", "paint", "dance with", "look at",
         "stare intently at"]
adjectives = ["red", "blue", "green", "strange", "odd", "pink-ish", "putrid",
              "cheap", "expensive", "terrible", "dwarven"]
nouns = ["apple", "susage", "house", "bottle", "computer", "time machine",
         "AWP", "Negev", "Twillight fanfic collection", "phone",
         "friend's mother", "batcave", "potato", "job", "hair"]

places = ["Hong Kong", "the moon", "ancient Greece", "Detroit",
          "the 12th century", "Dungeons and Dragons", "your mom's bedroom",
          "the grand canyon", "Dwarf Fortress", "highschool"]
"""Always an IT"""
objects = ["car", "house", "face", "furniture", "chair"]
compareobjects = ["bagpipe", "pile of manure"]
relations = ["father", "sister", "brother", "grandmother", "stepmother", "aunt", "uncle"]
people = ["the Terminator", "the guy from Lost", "Gimli", "Godzilla"]
diseases = ["the black plauge", "HIV", "cholera", "diharrea"]
media = ["the Matrix", "Alien", "LOTR", "Dungeons and Dragons"]

if __name__ == '__main__':
    print(MakeText())
