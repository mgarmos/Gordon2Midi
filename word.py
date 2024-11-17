import random
from syllables import A1, A2, A3, A4, A5, B1, B2, B3, B4, B5, B6, B7

# TODO meter to constant

dupleSyllablesChoice = [A1, A2, A3, A4, A5]
tripleSyllablesChoice = [B1, B2, B3, B4, B5, B6, B7]


def __str__(self):
    print('hi')


def getDupleWord():
    return __getWord(2)


def getTripleWord():
    return __getWord(3)


def __getWord(meter):
    word = []
    syllablesChoice = dupleSyllablesChoice if meter == 2 else tripleSyllablesChoice
    for i in range(4):
        syllable = random.choice(syllablesChoice)()
        word.append(syllable)
    return word


def printWord(word):
    pass


def main():
    # dupleWord = getDupleWord()
    # print(dupleWord)
    print(dupleSyllablesChoice)


if __name__ == "__main__":
    main()
