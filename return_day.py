# Alexandra McClendon
# July 22, 2026
# This program calculates the return day of the week after a trip.

start_day = int(input("Enter the starting day number (0=Sun, 6=Sat): "))
nights = int(input("Enter the number of nights you will stay: "))

return_day = (start_day + nights) % 7
print("You will return on day number", return_day)
