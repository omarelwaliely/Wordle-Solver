# Dictionary
import math


def solveOne(olddict,word,result):
    safeLetters = {}
    dictionary = olddict
    oldlength = len(olddict)
    for i in range(0, 5):
        if (result[i] == 'g' or result[i] == 'y'):
            if (word[i] not in safeLetters or safeLetters[word[i]] ==0):
                safeLetters[word[i]]=1
            else:
                safeLetters[word[i]]+=1
    for i in range(0, 5):
        if (result[i] == 'g'):
            dictionary = [w for w in dictionary if (not word[i] != w[i])]
        elif (result[i] == 'y'):
            dictionary = [w for w in dictionary if (not(word[i] == w[i] or word[i] not in w))]
        elif (result[i] == 'b'):
            if (word[i] not in safeLetters):
                dictionary = [w for w in dictionary if (not (word[i] in w and word[i] not in safeLetters))]
            elif (word[i] in safeLetters):
                dictionary = [w for w in dictionary  if(w.count(word[i]) <= safeLetters.get(word[i], 0))]
    p = len(dictionary)/oldlength

    if(p ==0):
        return 0
    information = p*math.log2(1/p)
    return information
def getAllInformation(dict):
    colorMap = {0:"g",1:"y",2:"b"}
    maximum = -1
    selectedIndex = 0
    for index,word in enumerate(dict):
        wordinfo =0
        for i in range(0,3):
            for j in range (0,3):
                for k in range (0,3):
                    for l in range (0,3):
                        for m in range (0,3):
                            findResult = colorMap[i]+colorMap[j]+colorMap[k]+colorMap[l]+colorMap[m]
                            wordinfo += solveOne(dict,word,findResult)
        if maximum < wordinfo:
            maximum = wordinfo
            selectedIndex = index
    return dictionary[selectedIndex]





if __name__ == "__main__":

    with (open("processedDictionary.txt", "r")) as f:
        dictionary = f.read().splitlines()
    word = input("Enter first word: ").lower()
    safeLetters = {}
    while(True):
        print(word)
        result = input("Enter result (g,y,b) as string: ")
        if(result == 'ggggg'):
            print("good job cheater")
            break
        for i in range(0, 5):
            if (result[i] == 'g' or result[i] == 'y'):
                if (word[i] not in safeLetters or safeLetters[word[i]] ==0):
                    safeLetters[word[i]]=1
                else:
                    safeLetters[word[i]]+=1
        for i in range(0, 5):
            if(result == "ggggg"):
                print("good job cheater")
            if (result[i] == 'g'):
                dictionary = [w for w in dictionary if (not word[i] != w[i])]
            elif (result[i] == 'y'):
                dictionary = [w for w in dictionary if (not(word[i] == w[i] or word[i] not in w))]
            elif (result[i] == 'b'):
                if (word[i] not in safeLetters):
                    dictionary = [w for w in dictionary if (not (word[i] in w and word[i] not in safeLetters))]
                elif (word[i] in safeLetters):
                    dictionary = [w for w in dictionary  if(w.count(word[i]) <= safeLetters.get(word[i], 0))]
        safeLetters = {key: 0 for key in safeLetters}
        print(dictionary)
        word = getAllInformation(dictionary)
    #print(solveOne(dictionary,"crane","gbggg"))
