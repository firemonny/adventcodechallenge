import re
filename = "puzzle3.txt"
content = None
with open(filename) as f:
    content = f.readlines()
newContent = []
for line in content:
    lineArray = re.split("#| @ |,|:|x|\n",line)
    lineArray.pop(0)
    lineArray.pop(len(lineArray)-1)
    print(lineArray)
    newContent.append(lineArray) 

# Create the 1000 * 1000 array
square = []
for heigh in range(0,1000):
    row = []
    for width in range(0,1000):
        row.append(0)
    square.append(row)

for eachSize in newContent:
    x = int(eachSize[1])
    y = int(eachSize[2])
    dx = int(eachSize[3])
    dy = int(eachSize[4])
    for rowIndex, rowItem in enumerate(square):
        if (rowIndex >= y -1) or (rowIndex <= y+dy-1): 
            for columnIndex, columnItem in enumerate(rowItem):
                if (columnIndex >= x -1) or (columnIndex <= x+dx-1):
                    square[rowIndex][columnIndex] = square[rowIndex][columnIndex] +1 

print(square[0])
        