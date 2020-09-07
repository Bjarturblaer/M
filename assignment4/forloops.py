#i = 0
#while i<5:
 #   print(i, end=' ')
  #  i += 1
#pri#nt("Lykkjan er búin")
"""the_range = range(6)
for i in the_range:
    print(i, end= ' ')

for k in the_range:
    print(k, end = ' ')"""

"""for i in range(1,11):
    print(i, end= ' ')"""

"""start = 5
how_many_you_want = 4
end = start + how_many_you_want
the_range = range(start, end)
for i in the_range:
    print(i, end=' ')
print()"""



"""max_days = int(input("Input max number of days: "))
target = int(input("Input dollar target: "))
days_when_amount_acquired = 0 
a = 0
amount = 1
for i in range(0,max_days+1):
    if a<target:
        days_when_amount_acquired +=1
        a = a + amount
        else:
            break
        amount= amount * 2
else:
    days_when_amount_acquired = 0 """

# Fill in the missing code
#for i in range(0,max_days+1):
    #while i < target:
       # i = i*i
    #for j in range(0,target+1):
       # j = j*j

        #print('Days needed:',i)



max_num = int(input("Input maximum number: "))
sum = 0

for i in range(1,max_num):
    sum = max_num***3
    print(sum)
