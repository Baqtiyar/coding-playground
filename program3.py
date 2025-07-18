#write a program to print odd number till 20 

count=0 
num =1

while count < 10:
    if num% 2 != 0:
        print(num)
        count +=1
    num +=1