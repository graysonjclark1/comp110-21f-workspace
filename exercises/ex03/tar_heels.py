"""An exercise in remainders and boolean logic."""

__author__ = "730481947"


# Begin your solution here...
integer: int = int(input("Enter an int: "))
message: str = ""
if integer % 2 == 0: 
    message = message + "TAR"
    if integer % 7 == 0:
        message = message + "HEELS"
else:
    if integer % 7 == 0:
        message = message + "HEELS"
    else:
        message = message + "CAROLINA"

print(message)