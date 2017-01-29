#SECTION 2 - FUNCTIONS (20PTS TOTAL)
import math
import random
'''
#PROBLEM 1 (Length of String - 3pts)
# Make a function which asks the user to enter a string, then prints the length of that string.
# You will need to use the input() function.
# Make a call to that function
print("Problem #1")
def length():
    user = input("Write a string and the function will print the length of the string: ")
    print(len(user))

length()
print()
# PROBLEM 2 (Pythagorean theorem - 4pts)
# The Pythagorean theorem states that of a right triangle, the square of the
# length of the diagonal side is equal to the sum of the squares of the lengths
# of the other two sides (or a^2 + b^2 = c^2).
# Write a program that asks the user for the lengths of the two sides that meet at a right angle.
# Then calculate the length of the third side, and display it in a nicely formatted way.
# You may ignore the fact that the user can enter negative or zero lengths for the sides.
print("Problem #2")

def pythag():
    a = input("Enter the length of one leg of a right triangle: ")
    b = input("Enter the length of another leg of the triangle: ")
    c = (((int(a)**2) + (int(b)**2)) ** 0.5)
    c = round(c , 2)
    print("The third side length is:" , c)

pythag()
print()


# PROBLEM 3 (Biggest, smallest, average - 4pts)
# Make a function to ask the user to enter three numbers.
# Then print the largest, the smallest, and their average, rounded to 2 decimals.
# Display the answers in a "nicely" formatted way.
# Make a call to your function.
print("Problem #3")

def bigsmallavg():
    a = input("Enter a number: ")
    b = input("Enter a different number: ")
    c = input("Enter a different number: ")
    a = int(a)
    b = int(b)
    c = int(c)
    #
    if a > b and a > c:
        print(a, "is the biggest")
    if b > a and b > c:
        print(b, "is the biggest")
    if c > a and c > b:
        print(c, "is the biggest")
    #
    if a < b and a < c:
        print(a, "is the smallest")
    if b < a and b < c:
        print(b, "is the smallest")
    if c < a and c < b:
        print(c, "is the smallest")
    #
    average = round(((a + b + c )/ 3), 1)
    print("Average =", average )

bigsmallavg()
print()
'''

# PROBLEM 4 (e to the... - 3pts)
# Calculate the value of e (from the math library) to the power of -1, 0, 1, 2, and 3.
# display the results, with 5 decimals, in a nicely formatted manner.
print("Problem #4")

def e(x):
    result = ((math.e) ** x)
    result = round(result, 5)
    print(result)

e(-1)
e(0)
e(1)
e(2)
e(3)
print()


# PROBLEM 5 (Random int - 3pts)
# Generate a random integer between 1 and 10 (1 and 10 both included),
# but only use the random() function (randrange is not allowed here)
print("Problem #5")

integer = int(random.random())
integer = (integer * 10) + 1
print(integer)
print()

# PROBLEM 6 (add me, multiply me - 3pts)
# Make a function which takes in two integers and RETURNS their sum AND their product.
print("Problem #6")

def add_mult(a, b):
    return a + b, a * b

add_mult(3,2)

