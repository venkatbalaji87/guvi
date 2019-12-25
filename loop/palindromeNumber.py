inputNumber=(input("Enter the Number : "))
reverseNumber=inputNumber[::-1]
inputConversion=int(inputNumber)
reverseNumberConversion=int(reverseNumber)
if(inputConversion == reverseNumberConversion):
    print("Number is Palindrome")
else:
    print("Number is not an palindrome")
