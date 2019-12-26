initialValue=int(input("Enter the Number : "))
inputNumber=int(input("Enter the Number : "))
for number in range(initialValue,inputNumber+1):
    if(number>1):
        for i in range(2,number):
            if((number%i) == 0):
                print(number,"is not prime number")
                break
        else:
            print(number, "is prime number")
