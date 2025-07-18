#write a program to print first 10 positive integer number which is divided by 2 
count = 0
num =1

while count < 5:
    if num%2==0:
        print(num)
        count +=1
    num+=1