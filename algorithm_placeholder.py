# import constant variables
import constant

# algorithm
def algor(data):
    
    ListOfWords = {}
    ListOfOthers = {}
    result = ""
    enum = 0

    for item in data:
        if item.isalpha():
            result += item.lower()
        else:
            if result != "":
                ListOfWords[enum] = result
                enum += 1
            result = ""

            ListOfOthers[enum] = item

        
            enum += 1
    ListOfWords[enum] = result
    for item in ListOfWords:
        if constant.blacklist.get(ListOfWords[item]) != None:
            ListOfWords[item] = constant.Replacement[ListOfWords[item]]

    enum = 0
    result = ""
    while enum != len(ListOfOthers) + len(ListOfWords):
        if enum in ListOfOthers:
            result += ListOfOthers[enum]
        else:
            result += ListOfWords[enum]
        enum += 1

    return result
