# Author: Alexandra McClendon
# Course: CSS300
# Module 4 Lab Activity
# Description: Debugging corrections for this Python program.
# This program prints authors and the year they died.

# Create a collection of these authors and
# the year they kicked the bucket;
# print the collection in the following format:
# Charles Dickens died in 1870.

authors = {
    "Charles Dickens": 1870,
    "William Thackeray": 1863,
    "Anthony Trollope": 1882,
    "Gerard Manley Hopkins": 1889
}

for author, date in authors.items():
    print(author + " died in " + str(date) + ".")
