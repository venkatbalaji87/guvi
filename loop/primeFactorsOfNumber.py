inputNumber=int(input())
print("Prime Factors of Number are ")
for i in range(1,inputNumber+1):
    if(inputNumber%i==0):
        print(i)
