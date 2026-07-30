# Author: Alexandra McClendon
# Course: CSS300
# Module 4 Lab Activity
# Description: Debugging corrections for this Python program.
This program checks a year and prints whether its in the past, present, or future.

# A time traveler has suddenly appeared in your classroom!

# Create a variable representing the traveler's
# year of origin and greet our strange visitor with a different message
# depending on when he is from.

year = int(input("Greetings! What is your year of origin? "))

if year < 1900:
    print("Woah, that's the past!")
elif year >= 1900 and year <= 2020:
    print("That's totally the present!")
else:
    print("Far out, that's the future!")
1
