inputNumber=int(input())
sumNumber=0
while(inputNumber>0):
    digits=inputNumber%10
    sumNumber=sumNumber+digits
    inputNumber=inputNumber//10
print(sumNumber)
