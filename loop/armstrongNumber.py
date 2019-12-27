inputNumber=int(input())
sumNumber=0
temp=inputNumber
while(temp>0):
    digits=temp%10
    sumNumber=sumNumber+(digits*3)
    temp
if(sumNumber==inputNumber):
    print(inputNumber,"is Armstrong Number")
else:
    print(inputNumber,"is not Armstrong Number")
