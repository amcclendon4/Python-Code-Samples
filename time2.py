# Author: Alexandra McClendon
# Course: CSS300
# Module 4 Lab Activity
# Description: Debugging corrections for this Python program.
# This program calculates when an alarm will go off after waiting a certain number of hours.

str_time = input("What time is it now? ")
str_wait_time = input("What is the number of hours to wait? ")

time = int(str_time)
wait_time = int(str_wait_time)

time_when_alarm_go_off = (time + wait_time) % 24
print(time_when_alarm_go_off)
