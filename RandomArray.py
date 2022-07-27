import random

N = int(input("Enter the number of random numbers you want: "))
ResultArray =[]
for i in range(N):
    RandomNum = random.randint(0,1000)
    while RandomNum in ResultArray:
        RandomNum = random.randint(0, 1000)
    ResultArray.append(RandomNum)
    i+=1        
print(ResultArray)