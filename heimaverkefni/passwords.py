wrong = 0
right = 0
MINIMUM_LENGTH = 6
MAXIMUM_LENGTH = 20

while True:
    capital = False
    small = False
    
    number = False
    password_length = False
    new_password = input("Enter a new password: ")
    if new_password == 'q':
        break
    
    if len(new_password)>=MINIMUM_LENGTH and len(new_password)<=MAXIMUM_LENGTH :
        password_length = True

        for letter in new_password:
            if letter.isupper():
                capital = True
            elif letter.islower():
                small = True
            elif letter.isdigit():
                number = True

        if not small:
            print("At least one lower case letter needed")
        if not capital:
            print("At least one upper case letter needed")
        if not number:
             print("At least one number needed")   
    else:
        print("Invalid length")
    if capital and small and number and password_length:
        right += 1
        print("Valid password of length {}".format(len(new_password)))
    else:
        wrong += 1


print("You tried {} passwords, {} valid, {} invalid".format(right+wrong,right,wrong))



