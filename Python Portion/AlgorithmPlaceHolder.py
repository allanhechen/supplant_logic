import constant

with open("test.txt") as txt:
   text = txt.readlines()

from typing import List


def algor():
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
                enum += 1
            str = ""

            ListOfOthers[enum] = item

        
            enum += 1
    ListOfWords[enum] = str
    for item in ListOfWords:
        if constant.blacklist.get(ListOfWords[item]) != None:
            ListOfWords[item] = constant.Replacement[ListOfWords[item]]

    enum = 0
    str = ""
    while enum != len(ListOfOthers) + len(ListOfWords):
        if enum in ListOfOthers:
            str += ListOfOthers[enum]
        else:
            str += ListOfWords[enum]
        enum += 1
