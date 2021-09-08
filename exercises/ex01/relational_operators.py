"""Input 2 variables and demonstrate how relational operators work."""
__author__ = "730481947"

left: int = int(input("Left-hand variable: "))
right: int = int(input("Right-hand variable: "))
result_1: bool = left < right
print(str(left) + " < " + str(right) + " is " + str(result_1))
result_2: bool = left >= right
print(str(left) + " >= " + str(right) + " is " + str(result_2))
result_3: bool = left == right
print(str(left) + " == " + str(right) + " is " + str(result_3))
result_4: bool = left != right 
print(str(left) + " != " + str(right) + " is " + str(result_4)) 