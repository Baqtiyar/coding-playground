#Understanding break in loops


av = 10

x = int(input("How many candies do you want?"))

i =1 
while i<=x:

    if i>av:
        print("out of stock")
        break

    print("Candy", i)
    i +=1

print("get lost")