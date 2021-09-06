A = float(input('keep score:'))
B = float(input('score midexam:'))
C = float(input('score finalexam:'))
D = A + B + C
if(80<=D<=100):
    print('A')
elif(75<=D<=79):
    print('B+')
elif(70<=D<=74):
    print('B')
elif(65<=D<=69):
    print('C+')
elif(60<=D<=64):
    print('C')
elif(55<=D<=59):
    print('D+')
elif(50<=D<=54):
    print('D')
elif(0<=D<=49):
    print('F')
else:
    print('ไม่ได้สอบ')