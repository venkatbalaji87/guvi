inputNumber=int(input())
productNumber=1
while(inputNumber>0):
    digits=inputNumber%10
    productNumber=productNumber*digits
    inputNumber=inputNumber//10
print(productNumber)
