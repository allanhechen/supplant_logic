# this python code will read a text file and find derogatory statements
import constant

# get the text in a variable
with open("test.txt") as txt:
    text = txt.readlines()

# for now, I will implement the splitting using constant variables from another python file
# TODO: implement more constant split variables as needed
for i in constant.split:
    phrases = text.split(i)
    text = phrases

# firstly look for specific derogatory words that are blatantly bad to say, these are hard coded
# TODO: implement more words to glassary
for i in phrases:
    