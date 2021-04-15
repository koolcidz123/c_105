import csv
import math

with open("data.csv", newline='') as f:
    reader = csv.reader(f)
    fileData = list(reader)
# fileData.pop()
print (fileData)
fileData = fileData[0]

def mean(data) :
    # print (data)
    total =0
    n = len(data)
    for x in data:
        # print(data[x])
        total = total + int(x)
    mean = total / n
    # print(mean)
    return mean

squaredList = []
for number in fileData:
    a = int(number) - mean(fileData)
    a = a**2
    squaredList.append(a)

sub = 0
for i in squaredList:
    sub = sub + i

result = sub/(len(fileData)-1)

result = math.sqrt(result)
print(result)