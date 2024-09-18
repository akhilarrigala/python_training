# Print second smallest digit in a number

input_num = int(input('Enter a number:'))
list = []

while(input_num>0):
    rem = input_num % 10
    list.append(rem)
    input_num = input_num // 10

list.sort()
print(list[1])