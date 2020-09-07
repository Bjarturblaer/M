print("Welcome to car rentals!")

like_to_continue = input("Would you like to continue (y/n)? ")
while like_to_continue ==  "y":
    code = input("Customer code (b or d): ")
    number_days = int(input("Number of days: "))
    
    if code =="b":
        budget_base_charge = 40
        base_charge_b = int(number_days)*int(budget_base_charge)
    elif code =="d":
        daily_base_charge = 60
        base_charge_d = int(number_days)*int(daily_base_charge)
    odometer_at_start = int(input("Odometer reading at the start: "))
    odometer_at_end = int(input("Odometer reading at the end: "))

    Miles_driven = int(odometer_at_end)-int(odometer_at_start)
    print("Miles driven:",(Miles_driven))
    if code == "b":
        mileage_charge = (int(Miles_driven)*0.25)
        Amount_due = round(((base_charge_b)+mileage_charge),1)
        print("Amount due: ",(Amount_due))
    
    elif code == "d":
        if Miles_driven/number_days < 100:
            Amount_due = 60*number_days
        else:
            extra_miles_driven = Miles_driven - (100*number_days)
            Amount_due = (60*number_days) + 0.25* extra_miles_driven
            print("Amount due: ",(Amount_due))
    
    like_to_continue = input("Would you like to continue (y/n)? ")


        
    
   
  



















