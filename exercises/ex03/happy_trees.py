"""Drawing forests in a loop."""

__author__ = "730481947"

# The string constant for the pine tree emoji
TREE: str = '\U0001F332'
depth: int = int(input("Depth: "))
i: int = 0
if depth <= 0:
    print("")
else:
    while i < depth: 
        string: str = ""
        j = i + 1
        while j < depth: 
            if j < depth:
                if j == 1:
                    string = string + TREE
            j = j + 1
        print(string)
        i = i + 1