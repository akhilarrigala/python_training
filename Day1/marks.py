avg_score = int(input('Enter the average score: '))
if(avg_score>=0 and avg_score<50):
    print('Fail')
elif(avg_score>=50 and avg_score<75):
    print('SC')
elif(avg_score>=0 and avg_score<91):
    print('FC')
elif(avg_score>=91 and avg_score<100):
    print('Distiction')
else:
    print('Invalid Input')