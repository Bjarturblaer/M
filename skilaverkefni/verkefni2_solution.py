age = int(input("Please enter your age: "))
name = input("Please enter your name: ")
option = int(input("Please choose an option:\n1.School package\n2.Regular package\n3.Flex package\n4.Retirement package\nEnter the number in front of the package you wish to choose: "))

error = ""

if age <= 1 or age > 124:
    error = "Invalid age!"
elif option <= 0 or option > 4:
    error = "Invalid option!"
elif age < 67 and option == 4:
    error = "Invalid! Retirement package only valid for people older than 66."
elif age >= 18 and option == 1:
    error = "Invalid! School package only valid for people younger than 18."

cost = 7000
optionName = ""

if error == "":
    if age >= 18 and age < 67:
        if option == 2:
            optionName = "regular package"  
        elif option == 3:
            cost -= 2000 # cost = cost - 2000
            optionName = "flex package"  

    elif age < 18:
         if option == 1:
             cost -=5000
             optionName = "school package"  
         elif option == 2:
             cost -=500
             optionName = "regular package"
         elif option == 3:
             cost -= 2500
             optionName = "flex package"   

    elif age >= 67:
         if option == 2:
             cost -= 1000
             optionName = "regular package"
         elif option == 3: 
             cost -= 3000
             optionName = "flex package"
         elif option == 4:
             cost -= 4000
             optionName = "retirement package"

    print("Dear "+name+", you have chosen the "+optionName+". Payment for this package is "+str(cost)+"kr.")

else:
    print(error)










