import random

turns = 12

master = []
for x in range(4):
    master.append(random.randint(1, 4))

name = raw_input("What's your name? ")

print "Hello %s, welcome to mastermind!" % name
print """Mastermind is a code-breaking game.
    You will try to guess the pattern in both order and number.
    You get 12 turns to guess the sequence of 4 numbers, 
    each ranging from 1 to 4.
    Enter your guess in order, one number at a time.
    
    If your number AND placement both matche the master sequence,
    an "O" will be displayed.
    If only your number OR placement is correct,
    a "X" will be displayed.
    If your number and placement is incorrect,
    a "-" will be displayed.

    Good luck!
    """
print master

for tries in range(turns):
    print "Attempt: %d" % (tries + 1)
    attempt = []

    for place in range(4):
        num = int(raw_input("> "))
        if num == master[place]:
            attempt.append("O")
        else:
            for x in range(4):
                if num == master[x]:
                    attempt.append("X")
                    break
            else:
                attempt.append("-")
    print attempt
    
    right = 0
    for x in attempt:
        if x == "O":
            right += 1

    if right == 4:
        print "Congratulations! You have won!"
        break
    if tries == (turns - 1):
        print "Sorry you lost. Try again?"


