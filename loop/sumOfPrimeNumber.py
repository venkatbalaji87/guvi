initialValue=int(input("Enter the Number : "))
inputNumber=int(input("Enter the Number : "))
sumValue=0
for number in range(initialValue,inputNumber+1):
    if(number>1):
        for i in range(2,number):
            if((number%i) == 0):
                break
        else:
            sumValue=sumValue+number
print(sumValue)
