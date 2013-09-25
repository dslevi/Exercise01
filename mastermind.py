import random

turns = 12
master = []
for x in range(4):
    master.append(random.randint(1, 4))

name = raw_input("What's your name? ")

print "Hello, %s. Welcome to Mastermind!" % name
print """Mastermind is a code-breaking game.
    You have 12 turns to guess a mystery pattern of four numbers.
    Each digit in this sequence ranges from 1 to 4.
    Enter your guess in order, one number at a time.
    
    If your number AND placement both match the master sequence,
    an "O" will be displayed.
    If either your number OR placement is correct,
    a "X" will be displayed.
    If your number and placement are both incorrect,
    a "*" will be displayed.

    Good luck!
    """
    
for tries in range(turns):
    print "Attempt: %d" % (tries + 1)
    attempt = []
    tempMaster = master[:]
	
    for place in range(4):
        num = int(raw_input("> "))
    	if num == master[place]:
            attempt.append("O")
            tempMaster[place] = "O"
        else:
            attempt.append(num)
    
    for y in attempt:
    	if y != "O":
			for z in range(4):
				if y == tempMaster[z]:
					attempt[attempt.index(y)] = "X"
					break
    			else:
    				attempt[attempt.index(y)] = "*"
    
    right = 0
    for x in attempt:
        if x == "O":
            right += 1

    if right == 4:
        print "Congratulations! You have won!"
        break
    if tries == (turns - 1):
        print "Sorry, you lost. :("


