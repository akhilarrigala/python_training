import numpy as np

lucky_number = int(input('Try your Luck: '))

a = np.random.randint(0, 10, 1)
computer_number = a[0]
# Creates an numpy array of 3 elements between the range given
if computer_number == lucky_number:
    print('LakhPati')
else:
    print('RoadPati')

