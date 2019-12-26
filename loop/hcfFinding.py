firstNumber=int(input("Enter the first value : "))
secondNumber=int(input("Enter the second value : "))
if(firstNumber>secondNumber):
    smallerValue=secondNumber
else:
    smallerValue=firstNumber
for i in range(1,smallerValue+1):
    if((firstNumber%i==0) and (secondNumber%i==0)):
        value=i
print("HCF of both value is : ",value)
