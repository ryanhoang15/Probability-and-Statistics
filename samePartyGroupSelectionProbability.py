# initialize the list so store the number of people in the groups
partyA = []
partyB = []
partyC = []

# value of the population size
N = 1000

# this is loop is looping through the number
# of people and adding them to the right group
for i in range(1, N + 1):
    if i <= 500:
        partyA.append(i)

    elif 500 < i <= 800:
        partyB.append(i)

    elif 800 < i <= 1000:
        partyC.append(i)

# the number of time to run the experiment
experiment = 100000
# to keep track of which people are in which group
countA = 0
countB = 0
countC = 0
# to access the group's indices
index = 0

# this loop is looping through the
# experiment 100,000 times
for j in range(experiment):
    count = 0
    group = []
    # this while loop is getting 4 random people to
    # add to the variable group and to check if there is
    # no duplicates
    while count < 4:
        randNum = random.randint(1, 1000)
        if randNum not in group:
            group.append(randNum)
            count = count + 1

    # these if and elif is checking the random group
    # selected to see with party they belong too
    if group[index] in partyA and group[index + 1] in partyA and group[index + 2] in partyA and group[index + 3] in partyA:
        countA = countA + 1

    elif group[index] in partyB and group[index + 1] in partyB and group[index + 2] in partyB and group[index + 3] in partyB:
        countB = countB + 1

    elif group[index] in partyC and group[index + 1] in partyC and group[index + 2] in partyC and group[index + 3] in partyC:
        countC = countC + 1

# displaying the result
print("Party A: ", countA / experiment)
print("Party B: ", countB / experiment)
print("Party C: ", countC / experiment)
