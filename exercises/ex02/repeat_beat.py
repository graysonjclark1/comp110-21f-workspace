"""Repeating a beat in a loop."""

__author__ = "730481947"


# Begin your solution here...
repeat_beat: str = input("What beat do you want to repeat? ")
number_of_beats: int = int(input("How many times do you want to repeat it? "))
i: int = 0
if number_of_beats <= 0:
    print("No beat...")
else:
    while i < number_of_beats:
        string: str = ""
        while i < number_of_beats:
            string = string + repeat_beat + " "
            i: int = i + 1 
        print(string)
        i: int = i + 1
        