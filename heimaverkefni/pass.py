"""invalid = 0
valid = 0

while True:
    password= input("Enter a new password: ")
    if password == 'q':
        break
    length = False
    lower = False
    upper = False
    number = False
    if len(password)>=6 and len(password)<=20 :
        length=True
        for letter in password:
            if letter.isupper():
                upper=True
            elif letter.islower():
                lower=True
            elif letter.isdigit():
                number=True
        if not lower:
            print("At least one lower case letter needed")
        if not upper:
            print("At least one upper case letter needed")
        if not number:
            print("At least one number needed")
    else:
        print("Invalid length")
    if length and lower and upper and number:
        valid += 1
        print("Valid password of length {}".format(len(password)))
    else:
        invalid += 1

print("You tried {} passwords, {} valid, {} invalid".format(invalid+valid,valid,invalid))"""




