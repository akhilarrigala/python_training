# Print math table of a number for upto multiples of 20

input_num = int(input('Enter a number:'))
for i in range(1, 21):
    # print('%d X %2d = %3d'%(input_num, i, input_num * i))  -2d right side, -02d fill remaining spaces with 0's
    print(f'{input_num} X {i:2} = {(input_num*i):3}')