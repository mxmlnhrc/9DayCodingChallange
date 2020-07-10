import random
import time
from os import system

words_easy = ['hello', 'my', 'you', 'we', 'look', 'view', 'abc']
words_medium = ['I', 'except', 'mountain', 'rock', 'week', 'wealth']
words_hard = ['exercise', 'look up', 'car dealer', 'my life']
words_used = []


class lose(Exception):
    pass


def easy():
    random.shuffle(words_easy)
    print('*Easy Stage beginn...\nIf your ready type: go')
    userin = str(input())
    userin = userin.lower()
    print('')
    if userin == 'go':
        for i in range(random.randint(2, len(words_easy))):
            word = random.choice(words_easy)
            print(word)
            usertype = str(input())
            if usertype == word:
                print('')
                continue
            else:
                print("It was wrong!")
                print("You reached Easy Stage")
                raise lose


def easymed():
    random.shuffle(words_easy)
    random.shuffle(words_medium)
    words = []
    for j in range(0, random.randint(3, 6)):
        words.append(random.choice(words_easy))
        words.append(random.choice(words_medium))

    random.shuffle(words)

    print('')
    for i in range(random.randint(3, len(words))):
        word = random.choice(words)
        print(word)
        usertype = str(input())
        if usertype == word:
            print('')
            continue
        else:
            print("It was wrong!")
            print("You reached Easy-Medium stage")
            raise lose


def medium():
    random.shuffle(words_medium)
    for i in range(random.randint(2, len(words_medium))):
        word = random.choice(words_medium)
        print(word)
        usertype = str(input())
        if usertype == word:
            print('')
            continue
        else:
            print("It was wrong!")
            print("You reached Medium Stage")
            raise lose


def medhard():
    random.shuffle(words_hard)
    random.shuffle(words_medium)
    words = []
    for j in range(0, random.randint(3, 6)):
        words.append(random.choice(words_hard))
        words.append(random.choice(words_medium))

    random.shuffle(words)

    print('')
    for i in range(random.randint(3, len(words))):
        word = random.choice(words)
        print(word)
        usertype = str(input())
        if usertype == word:
            print('')
            continue
        else:
            print("It was wrong!")
            print("You reached Medium-Hard stage")
            raise lose


def hard():
    random.shuffle(words_hard)
    for i in range(random.randint(2, len(words_hard))):
        word = random.choice(words_hard)
        print(word)
        usertype = str(input())
        if usertype == word:
            print('')
            continue
        else:
            print("It was wrong!")
            print("You reached Hard Stage")
            raise lose


try:
    while True:
        easy()
        easymed()
        medium()
        medhard()
        hard()

except lose:
    pass