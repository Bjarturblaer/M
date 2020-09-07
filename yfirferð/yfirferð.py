# Breytur
# int float str type print + * / // % input
# x = 2
# x += 2  # x+2
# x *= 2 # x = x*2

# name = input("Your name: ")

# print("Your name is "+name)


# # Boolean
# # if true/false ops and& or|

#x = True
#y = False

#if x:
#    print("Yes")
#elif x:
#    print("Yes 2")
#else:
#    print("No")

# == > < >= <= !=

#if x != y:
#    print()

#if 2 > 5:
#    print("Hello")

#if 2 < 5 and x:
#    print("World")

"""a0 = int(input("Input a positive int: "))   # Do not change this line
print(a0)
while a0 !=1:
    if a0 % 2 == 0:
        a0 = int(a0/2)
        print(a0)
    elif a0 % 2 != 0:
        a0 = 3*a0+ 1
        print(a0)"""

#bugdet_base_charge = 40
#daily_base_charge = 60

like_to_continue = input("Would you like to continue (y/n)? ")
while like_to_continue == "y" or like_to_continue == "n":
    if like_to_continue ==  "y":
        code = input("Customer code (b or d): ")

    elif like_to_continue == "n":
        break
        
    if code == "b":
        number_days = input("Number of days: ")
    elif code == "d":
        number_days = input("Number of days: ")
    bugdet_base_charge = 40
    daily_base_charge = 60
    if code =="b":
        base_charge = int(number_days)*int(bugdet_base_charge)
    elif code =="d":
        base_charge = int(number_days)*int(daily_base_charge)
    odometer_at_start = (input("Odometer reading at the start: "))
    odometer_at_end = (input("Odometer reading at the end: "))
    Miles_driven = int(odometer_at_end)-int(odometer_at_start)
    if code == "b":
        mileage_charge = float(Miles_driven*0.25)
    elif code == "d":
        average_miles_per_day = float(Miles_driven))/float(number_days)
    if float(average_miles_per_day) <=100:
        extra_miles_driven = 0
    else:
        extra_miles_driven = float(average_miles_per_day)-100
    mileage_charge = (float(extra_miles_driven)*0.25)*float(number_days)
    Amount_due = float(base_charge) + float(mileage_charge)

    



print("Welcome to car rentals!")
print("Miles driven:",(Miles_driven))
print("Amount due",round(Amount_due))



