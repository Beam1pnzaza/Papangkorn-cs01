L=int(input("คะแนนเก็บ:"))
M=int(input("คะแนนสอบกลางภาค:"))
V=int(input("คะแนนสอบปลายภาค:"))

O=L+M+V
if 80 <= O <= 100:
        print ('Grade: A')
elif 75 <= O <=79:
        print ('Grade: B+')
elif 70 <= O <= 74:
        print ('Grade: B')
elif 65 <= O <= 69:
        print ('Grade: C+')
elif 60 <= O <= 64:
        print ('Grade: C')
elif 55 <= O <= 59:
        print ('Grade: D+')
elif 50 <= O <= 54:
        print ('Grade: D')
elif 0 <= O <= 49:
        print ('Grade: F')
else:
        print('number between 0 - 100')