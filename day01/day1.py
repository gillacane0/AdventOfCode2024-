import numpy as np

file = open("input.txt","r")
input = file.read()
file.close()

#PART ONE

left = []
right = []

list  = input.split("\n")
deleted = list.pop()

for element in list:
    element = element.split()
    left = np.append(left,int(element[0]))
    right = np.append(right,int(element[1]))

leftSorted = np.sort(left)
rightSorted = np.sort(right)

results = np.sum(np.abs(np.subtract(leftSorted,rightSorted)))
print("TOTAL DISTANCE IS ", results)


#PART TWO

similarityScore = 0
for i in leftSorted:
    similarityScore += ( (rightSorted==i).sum() * i )


print("THE SIMILARITY SCORE IS ",similarityScore)


