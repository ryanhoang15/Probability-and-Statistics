# value of the children in the class
# n = 10
n = 50
# total number of children in the class
total = 4 * n
# the number of time to run the experiment
experiment = 100000
# to keep track if there is equal
# distribution of boys and girls
# being selected
equalNumber = 0
# this loop is looping
# through the
# experiment 100,000 times
for i in range(experiment):
    group = []
    peopleCount = 0
    equalBoyCount = 0
    equalGirlCount = 0

    # selecting 2n students at random and
    # checking to see if there is no duplicate
    # children being added to the variable group
    while peopleCount < (2 * n):
        randPeople = random.randint(1, total)
        if randPeople not in group:
            group.append(randPeople)
            peopleCount = peopleCount + 1

    # these 2 for loops is checking to see how many
    # boys and girls that were selected at random
    for j in range(1, (2*n)+1):
        if j in group:
            equalBoyCount = equalBoyCount + 1

    for k in range((2*n)+1, total+1):
        if k in group:
            equalGirlCount = equalGirlCount + 1

    # checking to see if an equal number of boys and
    # girls were selected or not
    if equalBoyCount == equalGirlCount:
        equalNumber = equalNumber + 1

# displaying the result
print(equalNumber / experiment)
