import random
import math

def anagram_new (word):
    initialword = word
    combinations = math.factorial(len(data))
    count = 1
    myanagram = ""
    print("Total possible combinations are:", combinations)
    index = 0
    while count <= combinations:
        print("now at combination:", count)
        myanagram = myanagram + anagram_gen(initialword, index)
        index = index + 1
        count = count + 1
    return myanagram

def anagram_gen(word, index):
    count = 1
    ls_word = word
    wordlen = len(word)
    li_index = index
    ls_anagram = ""
    while count <= wordlen:
        ls_anagram = ls_anagram + ls_word[li_index]
        if len(ls_anagram)< wordlen:
            if li_index == (wordlen - 1):
                li_index = 0
            elif li_index < (wordlen - 1):
                li_index = li_index + 1
        count = count + 1
    return ls_anagram
                

def anagram(word):
    maxlen = len(word)-1
    count = 0
    norepeat = ""
    newword = ""
    print(maxlen, "/",count,"/",norepeat,"/",word)
    while (len(newword)- 1) <= maxlen:
        anacntr = random.randint(0,maxlen)
        print("anacntr",anacntr)
        print ("norepeat", norepeat.find(str(anacntr)))
        if norepeat.find(str(anacntr))== -1 :
            newword = newword + word[anacntr]
            norepeat = norepeat +"'"+str(anacntr) + "',"
        #count = count +1
            print ("len:",len(newword))
            print("new word", newword)
    return newword

def get_inputdata ():
    input_data =  input('Please enter a valid string')

    return input_data
#**********************************

data = get_inputdata()
anagram_new(data)
