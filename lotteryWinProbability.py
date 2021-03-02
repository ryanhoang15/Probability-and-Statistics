import random

# the number of time to run the experiment
experiment = 1000000
# to keep track the number of wins
winCount = 0
# to access the number drawn array indices
index = 0

# this loop is looping through the
# experiment 1,000,000 times
for i in range(experiment):
    numChosen = []
    numDrawn = []
    chosenCount = 0
    drawnCount = 0

    # these 2 while loops is selecting 4 random number each
    # and checking to see if there is any duplicate
    # before being added to the variable
    # numChosen and numDrawn
    while chosenCount < 4:
        randChosen = random.randint(1, 20)
        if randChosen not in numChosen:
            numChosen.append(randChosen)
            chosenCount = chosenCount + 1

    while drawnCount < 4:
        randDrawn = random.randint(1, 20)
        if randDrawn not in numDrawn:
            numDrawn.append(randDrawn)
            drawnCount = drawnCount + 1

    # checking if the 4 number from the
    # variable numDrawn matches the 4 number
    # in the variable numChosen
    if numDrawn[index] in numChosen:
        if numDrawn[index + 1] in numChosen:
            if numDrawn[index + 2] in numChosen:
                if numDrawn[index + 3] in numChosen:
                    winCount = winCount + 1

# display the result
print(winCount / experiment)
