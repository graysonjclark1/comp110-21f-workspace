word = "Hello"
letter = "h"
print(len(word))
cou: int = 0
i = 0 
if letter.lower() == word[i]:
    cou = cou + 1
else:
    if letter.upper() == word[i]:
        cou = cou + 1
letter = "e"
i = 1
if letter.lower() == word[i]:
    cou = cou + 1
else:
    if letter.upper() == word[i]:
        cou = cou + 1
letter = "l"
i = 2
if letter.lower() == word[i]:
    cou = cou + 1
else:
    if letter.upper() == word[i]:
        cou = cou + 1
i = 3
if letter.lower() == word[i]:
    cou = cou + 1
else:
    if letter.upper() == word[i]:
        cou = cou + 1
letter = "o"
i = 4
if letter.lower() == word[i]:
    cou = cou + 1
else:
    if letter.upper() == word[i]:
        cou = cou + 1
print(cou)
i = 0

letter: str = input("What letter do you want to search for?: ")
word: str = input("Enter a word: ")
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
