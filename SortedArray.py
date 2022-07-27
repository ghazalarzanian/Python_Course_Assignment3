ResultArray=[]
N = str()
while N != "end":
    N =input("enter:")
    if N !="end":
        ResultArray.append((N))

for i in range(len(ResultArray)):#convert to int
    ResultArray[i]=int (ResultArray[i])
print(ResultArray)
for i in range(1,len(ResultArray)):
    if (ResultArray[i]<ResultArray[i-1]): 
        print("Not sorted")
        break
    else:
        i+=1
if (i==len(ResultArray)):
    print("Sorted:)))")        
