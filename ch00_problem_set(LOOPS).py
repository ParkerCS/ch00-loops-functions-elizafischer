# 17/22
# LOOPS (22pts TOTAL)
import random

# PROBLEM 1 (Fibonacci - 4pts)
## The Fibonacci sequence is a sequence of numbers that starts with 1, followed by 1 again.
# Every next number is the sum of the two previous numbers.
# I.e., the sequence starts with 1, 1, 2, 3, 5, 8, 13, 21,...
# Write a program that calculates and prints the Fibonacci sequence
# until the numbers get higher than 1000.
print("Problem #1")
prev = 0
current = 1
new = 1

while new < 1000:
    new = current + prev
    prev = current
    current =  new
    print(str(new) + ",", end= "")



print("") 
# PROBLEM 2 (Number Guessing Game - 6pts)
# Write a program that takes a random integer between 1 and 1000
# The program then asks the user to guess the number.
# After every guess, the program will say either “Lower”
# if the number it took is lower, “Higher” if the number it took is higher,
# and “You guessed it!” if the number it took is equal to the number
# It might be wise, for testing purposes, to also display the number that the
# program randomly picks, until you are sure that the program works correctly
print("Problem #2")

number = random.randrange(0,1001)
#print(number)

user = input("There is a number between 1 and 1,000. Can you guess it? Type your guess: ")
user = int(user)

if user > 1000:
    print("Sorry, that number is out of the range. Guess again!")
if user < 1:
    print("Sorry, that number is out of the range. Guess again!")

if user > number:
    print("The number was lower :( ")
    print("")
if user < number:
    print("The number was higher than that :( ")
    print("")
if user == number:
    print("You guessed the number correctly!")
    print("")

# Lee - This needs to go in a loop to make it a "game".  (-2)

# PROBLEM 3 (Dice Hi-Low - 6pts) ****
# You roll five six-sided dice, one by one.
# How big is the probability that the value of each die is greater than or equal to the value of the previous die that you rolled?
# For example, the sequence “1, 1, 4, 4, 6” is a success, but “1, 1, 4, 3, 6” is not.
# Determine the probability of success using a simulation of a large number of trials.
print("Problem #3")

sucesses = 0
total = 1000
failed = 0
for i in range(total):
    #roll = []
    roll = 0
    for o in range(1, 6):
        dice_roll = (random.randrange(1,7))
        #roll.append(dice_roll)
        #print(roll)
        if dice_roll >= roll:
            roll = dice_roll
            continue
            #sucesses += 1
        else:
            break
            #failed += 1
    else:
        sucesses += 1

print("The probability that the value of each roll is greater than or equal to the previous is:", ((sucesses) / (total)) * 100, "percent")
# I have been working at this for a while and am not completely sure why it does not work

# Lee - See solution, check against version control history to see what the changes are.  Some of it made sense, and I think you were on the right track (-3)

print("")
# PROBLEM 4 (Number Puzzler - 6pts)
# A, B, C, and D are all different digits.
# The number DCBA is equal to 4 times the number ABCD.
# What are the digits?
# Note: to make ABCD and DCBA conventional numbers, neither A nor D can be zero.
# Use a quadruple-nested loop to solve.
print("Problem #4")

for a in range(10):
    for b in range(10):
        for c in range(10):
            for d in range(10):
                if int(str(d) + str(c) + str(b) + str(a)) == 4 * int(str(a) + str(b) + str(c) + str(d)) and a!= 0 and d != 0:
                    print("A = " + str(a) + ", B = " + str(b) + ", C = " + str(c) + ", and D = " + str(d))