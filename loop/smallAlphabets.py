print("printing all alphabets from a-z")
initialASCIIValue=int(input())
finalASCIIValue=int(input())
while(initialASCIIValue>0):
    print(chr(initialASCIIValue))
    initialASCIIValue=initialASCIIValue+1
    if(initialASCIIValue==finalASCIIValue):
        break
