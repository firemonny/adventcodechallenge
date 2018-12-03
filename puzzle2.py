filename = "puzzle2.txt"
content = None


def separateCount(word):
    separateArray = {}
    for character in word:
        if character in separateArray:
            separateArray[character] = separateArray[character] + 1
        else:
            separateArray[character] = 1
    return separateArray


with open(filename) as f:
    content = f.readlines()

threeTime = 0
twoTime = 0

for eachWord in content:
    eachWordDict = separateCount(eachWord)
    addtwo = False
    addThree = False
    for key, value in eachWordDict.items():
        if value == 2:
            addtwo = True
        elif value == 3:
            addThree = True
    if addtwo:
        twoTime = twoTime + 1
    if addThree:
        threeTime = threeTime + 1

result = twoTime * threeTime
print(result)


TotalDict = {}
# Part 2
for index in range(0, len(content)):
    wordDict = {}
    for word in content:
        if(content[index] != word):
            currentWord = content[index]
            numDifferent = 0
            for charIndex in range(0, len(word)-1):
                if(currentWord[charIndex] != word[charIndex]):
                    numDifferent = numDifferent + 1
            wordDict[word] = numDifferent
        TotalDict[content[index]] = wordDict
startValue = 1
for key, value in TotalDict.items():
    for secondKey, secondVal in value.items():
        if secondVal == startValue:
            print(key)
            print(secondKey)
