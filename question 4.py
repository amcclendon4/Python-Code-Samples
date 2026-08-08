# Alexandra McClendon
# August 2026
# This program prints messages for numbers divisible by three and five

for num in range(1, 51):
    if num % 3 == 0 and num % 5 == 0:
        print("Divisible by both")
    elif num % 3 == 0:
        print("Divisible by three")
    elif num % 5 == 0:
        print("Divisible by five")
    else:
        print(num)
