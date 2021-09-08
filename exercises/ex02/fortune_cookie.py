"""Program that outputs one of at least four random, good fortunes."""

__author__ = "730481947"

# The randint function is imported from the random library so that
# you are able to generate integers at random.
# 
# Documentation: https://docs.python.org/3/library/random.html#random.randint
#
# For example, consider the function call expression: randint(1, 100)
# It will evaluate to an int value >= 1 and <= 100. 
from random import randint


# Begin your solution here...
print("Your fortune cookie says...")
random_number: int = randint(1, 4)
if random_number == 1:
    print("You will make a 100 on your next Comp 110 quiz")
else:
    if random_number == 2:
        print("UNC will the national championship in football and basketball")
    else:
        if random_number == 3:
            print("You will be relieved of all your stress")
        else:
            if random_number == 4:
                print("You will have the confidence to talk to new people")

print("Now, go spread positive vibes!")