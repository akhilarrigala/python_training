import csv
import numpy as np

data = [] # Normal or ordinary list

with open('fruits_csv.csv', 'r') as csvfile:
    file_reader = csv.reader(csvfile, delimiter = ',')
    for row in file_reader:
        data.append(row)

npdata = np.array(data)  # convert the ordinary list of lists to a NumPy array which is 1D

print(len(npdata), '\n', type(npdata))
print('Shape: ', npdata.shape)
print('Datatype: ', npdata.dtype.type)
np.save(open('data2.npy', 'wb'), npdata) #We are saving the np array into a file with extension .npy

for element in data:
    print(element)