# print these pattern 
####     #
###      ##
##       ###
#        ####

# Multiple ways to do it
i=1 
while i<=4:
    if i==1:
        print("#")
    if i==2:
        print("#","#")
    if i==3:
        print("#","#","#")
    if i==4:
        print("#","#","#","#")
    i +=1

# While Loop
i=1
while i<=4:
    j=1
    while j<=i:
        print("#", end=" ")
        j +=1
    i +=1
    print()
    
# For loop
for i in range(1,5):
    for j in range(4, i - 1, -1):
        print("#", end=" ")
    print()




