inputNumber=int(input("Enter the Number : "))
if(inputNumber>1):
    for i in range(2,inputNumber):
        if((inputNumber%i) == 0):
            print(inputNumber,"is not prime number")
            break
    else:
        print(inputNumber, "is prime number")
    
