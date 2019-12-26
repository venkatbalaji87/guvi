firstNumber=int(input("Enter the first value : "))
secondNumber=int(input("Enter the second value : "))
if(firstNumber>secondNumber):
    greater=firstNumber
else:
    greater=secondNumber
while(True):
    if(greater%firstNumber==0 and greater%secondNumber==0):
        value=greater
        break
    greater=greater+1
print("LCM of both value is : ",value)
