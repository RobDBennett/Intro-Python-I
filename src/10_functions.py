# Write a function is_even that will return true if the passed-in number is even.

def is_even(x):
    if x % 2 == 0:
        return 'Even!'
    else:
        return 'Odd'

# Read a number from the keyboard
num = input("Enter a number: ")
num = int(num)

# Print out "Even!" if the number is even. Otherwise print "Odd"

is_even(num)