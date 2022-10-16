# import constant variables
from . import constant

#  Python String Methods Previous Next Python 
#  has a set of built-in methods that you can use on strings. 
#  Note: All string methods returns new values.

def algor(data):

    # string.split but it includes spaces
    def splitAndCap(word):
        hold = []

        for x in word:
            hold.append(x)

        hold[0] = hold[0].capitalize()

        hold = "".join(hold)

        return hold
    # 
    def holdNchange(L,vow):
        word = ""
        if vow == 1:
            L[0] = "an"
        
        for item in L:
            word += item

        return word

    vowels = {'a','e','i','o','u'}
    
    string = ""
    
    # enumerate the position of each word and non alphabet characters in dictionary
    
    enum = 0
    cap = 0


    caphold = {}
    stringhold = {}
    otherhold = {}

    # iterate through the string data
    for char in data:
        # if it is a alphabet
        if char.isalpha():
            # if its a capital then the it will say this word will be capital
            if not char.islower():
                cap = 1
            string += char.lower()

        else:
            # if its not alphabet and its not an empty string like space bar
            if string != "":
                stringhold[enum] = string
                caphold[enum] = cap
                cap = 0
                string = ""
                enum += 1
            otherhold[enum] = char
            enum += 1
    # add the last word
    if string.isalpha():
        stringhold[enum] = string
        caphold[enum] = cap

    result = ""
    enum = 0
    L = []
    vow = 0
    # while the length of both dictionary doesnt exceeed the iterator
    while enum != len(stringhold) + len(otherhold):
        # if this is a string
        if enum in stringhold:
            word = stringhold[enum]
            # if this is the letter a
            if word == 'a':
                vow = 1
                L.append(word)
            # if word is sensitive
            elif word in constant.blacklist:
                currWord = constant.Replacement[word]
                # if this is capital
                if caphold[enum] == 1:
                    currWord = splitAndCap(currWord)
                    if vow == 0:
                        result += currWord
                    else:
                        L.append(currWord)
                        if not currWord[0].lower() in vowels:
                            vow = 0
                        result += holdNchange(L,vow)
                        L = []
                        vow = 0
                else:
                    if vow == 0:
                        result += currWord
                    else:
                        L.append(currWord)
                        if not currWord[0].lower() in vowels:
                            vow = 0
                        result += holdNchange(L,vow)
                        L = []
                        vow = 0
            else:
                if caphold[enum] == 1:
                    word = splitAndCap(word)
                    if vow == 0:
                        result += word
                    else:
                        L.append(word)
                        if not word[0] in vowels:
                            vow = 0
                        result += holdNchange(L,vow)
                        L = []
                        vow = 0
                else:
                    if vow == 0:
                        result += word
                    else:
                        L.append(word)
                        if not word[0] in vowels:
                            vow = 0
                        result += holdNchange(L,vow)
                        L = []
                        vow = 0
        else:
            if vow != 1:
                result += otherhold[enum]
            else:
                L.append(otherhold[enum])
        enum += 1
    return result
