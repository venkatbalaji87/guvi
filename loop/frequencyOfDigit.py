def findFrequency(inputNumber,frequencyDigit):
    count=0
    while(inputNumber>0):        
        if(inputNumber%10 == frequencyDigit):
            count=count+1
        inputNumber=int(inputNumber/10)
    return count
inputNumber=int(input("Enter the inputNumber : "))
frequencyDigit=int(input("Enter the frequencyDigit :"))
print("Count of FrequencyDigit is : ",findFrequency(inputNumber,frequencyDigit))


