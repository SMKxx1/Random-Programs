import time
import random

def words():
    lines = open('words.txt').read().splitlines()
    word = random.choice(lines)
    return word

def letters(letter,word):
    count = 0
    for i in word:
        if i == letter:
            count += 1
        else:
            pass
    return count

def main():
    word = words()
    chance = len(word) + 5
    while chance != 0:
        print("Starting the game...")
        time.sleep(1)
        print("The length of the word is",len(word))
        time.sleep(1)
        hide = "*"*len(word)
        hide = list(hide)
        user = input("Enter a character: ")
        count = letters(user,word)
        print(count)
        tac = list(word)
        for s in range(0,count+1):
            for i in tac:
                if i == user:
                    loc = tac.index(user)
                    hide[loc] = user
                    tac[loc] = '*'
                    print("hide",hide)
                    print("tac",tac)
                else:
                    pass



main()
