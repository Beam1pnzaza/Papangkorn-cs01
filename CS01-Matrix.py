import numpy as np 
Array = []
Loop =int(input("Enter Your loop : "))
while(Loop%3 != 0):
    print('Please Enter Again')
    Loop = int(input("Enter yoour loop : "))
print("Enter Your Array: ")
for i in range(Loop):
    Array += [int(input(""))]
NewArray = np.asarray(Array)
NewArrayNumpy = NewArray.reshape(int(Loop/3),3)
print(NewArrayNumpy)
