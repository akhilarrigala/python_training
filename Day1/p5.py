# Read a number from the user and print the lucky digit of the user where the lucky digit is found by finding the sum of digits of the given number and repeat the alogrithm until single digir number is arrived.

def sum_of_digits(num):
    sum = 0
    while num != 0:
        rem = num % 10
        sum = sum + rem
        num = num // 10
    return sum

input_num = int(input('Enter a number:'))
while(input_num > 9):
    input_num = sum_of_digits(input_num)
print('Lucky number is ',input_num)

