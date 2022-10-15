# this python code will read a text file and find derogatory statements
import constant

# get the text in a variable
with open("test.txt") as txt:
    text = txt.readlines()

# TODO: as of currently, the phrases will be separated using periods, commas and sentence conjunctions
# for now, I will implement the splitting using constant variables from another python file
for i in constant.split:
    phrases = text.split(i)
    text = phrases

