startNumber=int(input())
inputNumber=int(input())
for num in range(startNumber,inputNumber + 1):
   order = len(str(num))
   sum = 0
   temp = num
   while temp > 0:
       digit = temp % 10
       sum += digit ** order
       temp
   if num == sum:
       print(num)
