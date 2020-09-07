loop=True
while loop:
    print("""
1. Find and replace
2. Find and remove
3. Remove unnecessary spaces
4. Encode
5. Decode
Q. Quit
    """)
    val=input("Enter one of the following:")
    if val == "1":
        strengur=input("Please enter a string: ")
        finna=input("Please enter a substring to find:")
        skipta=input("Please enter a substring to replace with: ")
        if finna not in strengur:
            print("Invalid Input!")
        else:
            print(strengur.replace(finna, skipta))

    elif val == "2":
        strengur=input("Please enter a string: ")
        finna=input("Please enter a substring to remove:")
        if finna not in strengur:
            print("Invalid Input!")
        else:
            print(strengur.replace(finna, ""))
    elif val == "3":
        strengur=input("Please enter a string: ")
        import re
        strengur2=strengur.strip()
        strengur3=strengur2.replace(" .", ".")
        print(re.sub('\s+', ' ', strengur3))
    elif val == "4":
        stringName = input("Please enter a string: ").strip()
        print (' '.join(str(ord(c)) for c in stringName))
    elif val == "5":
        templist = []
        number = input("Please enter an ASCII number here: ")
        userList = number.split()
        templist.append(userList)
        print(userList)
        print(''.join(chr(i) for i in userList2))
    elif val == "Q":
        loop = False
    else:
        print("Invalid Input!")
         
    
