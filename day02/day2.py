import numpy as np

file = open("input.txt","r")
input = file.read()
file.close()

records = input.split("\n")

def checkSafe(inputTuple):
    if type(inputTuple) == list: inputTuple = tuple(inputTuple)
    increase = None
    for i in range(1, len(inputTuple)):
        diff = int(inputTuple[i]) - int(inputTuple[i-1])
        if abs(diff) > 3 or diff == 0: return False
        elif diff > 0 and increase == None: increase = True
        elif diff <0 and increase == None: increase = False
        elif (diff > 0 and not(increase)) or (diff < 0 and increase): return False
    return True

firstPartSafes = 0
secondPartSafes = 0


for element in records:
    values = element.split()
    if checkSafe(values):
        firstPartSafes +=1
        secondPartSafes +=1

    else:
        for i in range(len(values)):
            newValues = list(values)
            del newValues[i]
            if(checkSafe(newValues)):
                secondPartSafes += 1
                break

print(firstPartSafes)
print(secondPartSafes)


