import random

def howManyUntil(stopNum):
    times = 1
    i = random.randrange(0,99)
    while i != stopNum:
        times += 1
        #print(i)
        i = random.randrange(0,99)
    print('---------------------found-----------------------------')
    return times

# define howManyUntil function

# call it to test it out
# to test it you may want to make a smaller version that generates random numbers from 0 to 10
# and prints out the random numbers....

howManyUntil(22)

