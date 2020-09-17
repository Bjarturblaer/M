dog_age = int(input("Input dog's age: ")) # Do not change this line
begin_human_age = 15
if dog_age == 1:
    print("Human age: ", begin_human_age)
if dog_age == 2:
    human_age=begin_human_age+9
    print("Human age: ",human_age)
    
if dog_age >= 3 and dog_age <= 16:
    human_age_2 = (begin_human_age)+((4*dog_age)+1)
    print("Human age: ",human_age_2)

if dog_age < 1:
    print("Invalid age")

if dog_age > 16:
    print("Invalid age")


    
    





