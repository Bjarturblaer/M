"""i = 0
while True:
    if i ==10:
        break
    print(i)
    i += 1
print("Lykkjan er búin")"""

#while True:
 #    the_input = input("Hvað viltu prenta út(skrifaðu q til að hætta): ")
  #   if the_input == 'q':
   #      break
    #print("Þetta er flott " + the_input)
#print#("Bless og takk fyrir")


"""i = 0
a = 20
while i<10 and a > 10:
    print(i)
    print(a)
    i += 1
    a -=2
        #continue
    #print(i)
print("While búið")"""

#if i < 10:
 #   print(i)
#else:
 #   print(-100)
#pr#int("if búið")


"""i = 0
input_str = int(input("Til hvað viltu odda tölur: "))
while i <= input_str:
    if i % 2 != 0:
        print("Tala", i, end= " ")
    i += 1
print()
# 11 string"""

"""input_str = input("Do you want to continue? ")
while i <= input_str:

print()"""


lower_int = int(input('Input lower: ')) # Do not change this line
upper_int = int(input('Input upper: ')) # Do not change this line
step_int = int(input('Input step size: ')) # Do not change this line

# Fill in the missing code below
print(lower_int)
print(upper_int)
print(step_int)
i = 0
while i > step_int:
    if i % 2 !=0:
        print()


for x in range(lower_int,upper_int,step_int):
    print(x)