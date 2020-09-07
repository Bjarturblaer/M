rivalstrength=int(input("What is your rival strength: "))
strength=int(input("What is your strength: "))
hours=float(input("How many hours a day: "))

dagur=0
kilo=strength
if rivalstrength > 0 or strength > 0 or hours > 0:
    while kilo < rivalstrength:
        kilo*=1.25
        dagur+=15
        
aukadagur= dagur//5
dagur=dagur+aukadagur


formula=dagur+1
formula2=dagur*formula
magaæfingar=formula2//2

print("It took",dagur,"day to get stronger than your rival and you took",magaæfingar,"reps")