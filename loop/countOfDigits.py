digit=int(input("Enter the number : "))
temp=digit
count=0
while(temp>0):
    temp=temp//10
    count=count+1
print("Number of digits in number is  :", count)
