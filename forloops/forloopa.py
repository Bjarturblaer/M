"""the_max = int(input("Enter the upper limit: "))
the_sum = 0
extra = 0

for number in range(1, the_max):
    if number%2 == 1:
        the_sum = the_sum + number
    else:
        extra = extra + 1

print(the_sum, extra)"""

"""for i in range(4):
    print("a")
    for j in range(2):
        print("b")"""

"""the_sum = 0
for i in range(0,5):
    if i==2:
        continue
    else:
        the_sum += i

print(the_sum)"""

"""for i in range(6, 0, -2):


    print(i, end=" ")"""


"""length = len(range(1,6))
print(length)"""





"""upto = int(input("Input an int: "))
for i in range(4):
    if upto < 4:
        print(i, end= " ")
        break"""

"""highest = int(input("Input an int: "))
for i in range (1,highest+1):
    if i%3 ==0:
        print(i)"""

"""first = int(input("Input the first integer: "))
second = int(input("Input the second integer: "))
sum= 0
for i in range(1, second+1):
    sum= sum+first
print(sum)"""


ays = int(input("Input number of days "))

while days <= 0:
    days = int(input("Days must be positive, input number of days: "))

# aIncrement = 2        # this line not needed
penny = 1

for day in range(1, days + 1):
    pAmount = int(penny)                      # this line was cleaned up
                                              # because we don't need to manually
                                              # handle day one
    dollars, cents = divmod(pAmount, 100)
    output = '$' + str(dollars) + '.' + str(cents)
    # addAmount = int(2**aIncrement -1)    # this line not needed
    # aIncrement +=1                       # this line not needed
    penny *= 2 
    print("Day " + str(day) + ":", output)






    
