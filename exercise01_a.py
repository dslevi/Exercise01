import random 

num = random.randint(1, 100)

name = raw_input("What is your name? ")
tries = 0

def isNumber(num):
    for x in num:
        # testing the ascii value of each char in num
        # to ensure it's a number
        if ord(x) > chr("9") or ord(x) < chr("0"):
            return False
    return True

while True:
    guess = raw_input("What number do you guess? ")
    if isNumber(guess):
        guess = int(guess)
        tries += 1
        if guess < num:
            print "Your number is too low."
        elif guess > num:
            print "Your number is too high."
        else:
            print "Congratulations, %s. You guessed the number in %d tries." % (name, tries)
            break
    else:
        print "Please input a valid number."
