import math

import csv
with open('C:\Projects\PRO-C105-Introduction_to_Standard_Deviation\data.csv', newline='') as f:
    reader = csv.reader(f)
    file_data = list(reader)

data = file_data[0]

def mean(data):
    n= len(data)
    total =0
    for x in data:
        total += int(x)

    mean = total / n
    return mean

square_list = []
for num in data:
    value = int(num) - mean(data)
    value = value * value
    square_list.append(value)

sum = 0
for s in square_list:
    sum += s

print(sum)

result = sum / (len(data)-1)
std_deviation = math.sqrt(result)
print(std_deviation)

