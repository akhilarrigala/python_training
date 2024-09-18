
import sys

list = sys.argv
states = []
capitals = []
for i in range(1,len(list)):
    temp = list[i].split(' ')
    states.append(temp[0])
    capitals.append(temp[1])

print(f'States are : {states}')
print(f'Captials are : {capitals}')