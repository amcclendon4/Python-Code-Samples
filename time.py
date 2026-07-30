current_time_str = input("What is the current time (in hours 0-23)? ")
wait_time_str = input("How many hours do you want to wait? ")

currentTimeInt = int(current_time_str)
waitTimeInt = int(wait_time_str)

finalTimeInt = (currentTimeInt + waitTimeInt) % 24
print(finalTimeInt)
