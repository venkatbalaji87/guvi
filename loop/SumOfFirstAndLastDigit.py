def firstDigit(number):
    while(number>=10):
        number=number/10
    return int(number)
def lastDigit(number):
    while(number>0):
        return number%10
number=int(input("Enter the Number : "))
firstDigit(number)
lastDigit(number)
print("Sum of First and last digit is :",(firstDigit(number)+lastDigit(number)))
