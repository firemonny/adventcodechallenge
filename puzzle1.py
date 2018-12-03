filename = "puzzle1.txt"

a = 0

content = None

with open(filename) as f:
    content = f.readlines()

for number in content:
    if number[0] == '+':
        a = a + int(number[1:])
    else:
        a = a - int(number[1:])

answer = None
b = 0
stack = [0]
start = True
while True:
    for number in content:
        if number[0] == '+':
            b = b + int(number[1:])
            if b in stack:
                print(b)
                start = False
                break
            stack.append(b)
        else:
            b = b - int(number[1:])
            if b in stack:
                print(b)
                start = False
                break
            stack.append(b)
    if start == False:
        break