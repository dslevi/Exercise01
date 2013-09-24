import random

num = random.randint(1, 100)
tries = 0

name = raw_input("Howdy, what's your name? ")
print "%s, I'm thinking of a number between 1 and 100.  Try to guess my number." % name

while True:
    guess = raw_input("Your guess? ")
    if guess.isdigit():
        guess = int(guess)
        tries += 1
        if guess > num:
            print "Your guess is too high, try again."
        elif guess < num:
            print "Your guess is too low, try again."
        else:
            if tries == 1:
                print "Well done, %s! You found my number in 1 try!" % name
            else:
                print "Well done, %s! You found my number in %d tries!" % (name, tries)
            break
    else:
        print "Please enter a positive, whole integer between 1 and 100."

