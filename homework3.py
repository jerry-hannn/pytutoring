########
# Write a program to test whether a number is within a specified range of a specified number.
# Input will be three numbers, the first being the number to test, the second being the lower bound, and the third being the upper bound.
# Example:
#   Input: 5, 1, 10
#   Output: True
# Example:
#   Input: 11, 1, 10
#   Output: False
########


########
# Write a program to test whether a passed letter is a vowel or not.
# Example:
#   Input: a
#   Output: True
# Example:
#   Input: b
#   Output: False
########


########
# Write a program to print the sum of 3 numbers, but if any two numbers are the same, print 0.
# Example:
#   Input: 1, 2, 3
#   Output: 6
# Example:
#   Input: 1, 1, 2
#   Output: 0
########

########
# Challenge!
# Write a program to guess the number between 0 and 100 the user is thinking of using bisection search.
# Enter 'h' to indicate the number is higher. Enter 'l' to indicate the number is lower. Enter 'c' to indicate I guessed correctly.
# Example:
#   Output: Is your secret number 50?
#   Input: h
#   Output: Is your secret number 25?
#   Input: l
#   Output: Is your secret number 37?
#   Input: l
#   Output: Is your secret number 43?
#   Input: h
#   Output: Is your secret number 40?
#   Input: c
#   Output: I guessed the number!
########

max = 100
min = 0
guess = 50
print("Is your secret number 50?")
while True:
    x = input()
    if x == "h":
        min = guess
        guess = min + (max - min) // 2
        print("Is your secret number " + str(guess) + "?")
    elif x == "l":
        max = guess
        guess = min + (max - min) // 2
        print("Is your secret number " + str(guess) + "?")
    elif x == "c":
        print("I guessed the number!")
        break
