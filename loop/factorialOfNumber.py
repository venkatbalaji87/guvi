inputNumber=int(input("Enter the number for factorial : "))
factorial=1
for i in range(1,inputNumber+1):
    factorial=factorial*i
print("The factorial of ", inputNumber,"is : ",factorial)
