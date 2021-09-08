"""Counting letters in a string."""

__author__ = "730481947"


# Begin your solution here...
letter: str = input("What letter do you want to search for?: ")
word: str = input("Enter a word: ")
i = 0 
while i < len(word):
    num = 0
    while i < len(word):
        if letter == letter.lower():
            if letter == word[i]:
                num = num + 1
        else:
            if letter == letter.upper():
                if letter == word[i]:
                    num = num + 1
        i = i + 1
    print("Count: " + str(num))
    i = i + 1

    