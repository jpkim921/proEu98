import math

# initial letter code from problem.
letterDict = {
    "C": "1",
    "A": "2",
    "R": "9",
    "E": "6"
}
# 3,4,5,7,8


def importWords():
    with open(r"p098_words.txt", "r") as f:
        for text in f:
            text = text.replace('"', '')

    return text.split(',')


# find Anagrams
def findAnagrams():
    anaArr = []
    for i in range(len(words)):
        j = i
        for j in range(len(words)):

            if (words[i] == words[j] or words[i] == words[j][::-1]):
                continue

            if ''.join(sorted(words[i])) == ''.join(sorted(words[j])):
                anaArr.append([words[i], words[j]])
    return anaArr


# # map word to digits
def mapWordToDigits(word):
    # remaining digits that were not assigned
    remaining = "34578"

    digits = ""
    for i in range(len(word)):
        if letterDict.get(word[i]):
            digits += letterDict[word[i]]
        else:
            letterDict[word[i]] = remaining[-1]
            remaining = remaining[:-1]
            digits += letterDict[word[i]]
    return int(digits)


def returnHighestSq(anaArr):
    maxSq = 1
    maxWord = ''
    for pair in anaArr:
        # find the max word to go with the digit
        if mapWordToDigits(pair[0]) > mapWordToDigits(pair[1]):
            maxWord = pair[0]
        else:
            maxWord = pair[1]
        # higherNum = max(mapWordToDigits(pair[0]), mapWordToDigits(pair[1]))
        # sqNum = math.sqrt(higherNum)
    
        sqNum = math.sqrt(mapWordToDigits(maxWord))

        if sqNum % 2 == 0 and sqNum > maxSq:
            maxSq = sqNum
    return [int(maxSq), maxWord]


words = importWords()
anaArr = findAnagrams()
print(returnHighestSq(anaArr)[0])
    
       
    



# # # # create a dictionary of arrays separated by string length
# # def createWordDictByLength():
# #     wordDict = {}
# #     for word in anaArr:
# #         if len(word) <= 3: continue

# #         if wordDict.get(len(word)):
# #             wordDict[len(word)].append(word)
# #         else:
# #             wordDict[len(word)] = []
# #             wordDict[len(word)].append(word)
# #     return wordDict


# # wordDict = createWordDictByLength()
# # print(wordDict)
