startNumber=int(input("Enter the Start Value : "))
endNumber=int(input("Enter the End Value : "))
sumTest=0
while(startNumber<=endNumber):
    if(startNumber%2!=0):
        sumTest=sumTest+startNumber
    startNumber=startNumber+1
print("Sum of Odd Numbers is:", sumTest)
