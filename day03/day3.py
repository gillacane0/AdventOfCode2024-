import re
import numpy as np

file = open("input.txt","r")
input = file.read()
file.close()

partOneSum = 0
partTwoSum = 0


partTwoInput = re.sub(r'\bdo?n\'t\(\).*?do\(\)', '', input, flags=re.DOTALL)
partTwoInput = re.sub(r"(?s)(.*?don't\([^)]*\)).*$", r"\1", partTwoInput)

matches = re.findall(r'mul\((\d{1,3}),(\d{1,3})\)', input)
partTwoMatches = re.findall(r'mul\((\d{1,3}),(\d{1,3})\)', partTwoInput)

for element in matches:
    partOneSum += ( int(element[0]) * int(element[1]) )

for element in partTwoMatches:
    partTwoSum += ( int(element[0]) * int(element[1]) )

print("PART ONE SUM ",partOneSum)
print("PART TWO SUM ",partTwoSum)

