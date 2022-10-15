import Utilities

# this python code will read a text file and find derogatory statements

from typing import List
import constant

# get the text in a variable
with open("test.txt") as txt:
   text = txt.readlines()

# for now, I will implement the splitting using constant variables from another python file
# TODO: implement more constant split variables as needed
"""textchange = 
textchange = list(textchange.split(" "))

# firstly look for specific derogatory words that are blatantly bad to say, these are hard coded
# TODO: implement more words to glassary
for i in phrases:
    """

ListOfWords = {}
ListOfOthers = {}
str = ""
enum = 0

for item in text:
    if item.isalpha():
        str += item.lower()
    else:
        if str != "":
            ListOfWords[enum] = str
            str = ""
        else:
            ListOfOthers[enum] = item;      
    enum += 1

for item in ListOfWords:
    if constant.blacklist.get(ListOfWords[item]) != None:
        ListOfWords[item] = constant.synonym[ListOfWords[item]]


