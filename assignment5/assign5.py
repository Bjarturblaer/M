num_int = int(input("Input a number: "))    # Do not change this line
# Fill in the missing code
listi = []
while num_int > -1:
    num_int = int(input("Input a number: "))
    listi.append(num_int)
max_int = max(listi)    
print("The maximum is", max_int)




"""n = int(input("Enter the length of the sequence: "))
n1=1
n2=2
n3=3
if n == 1:
    print(n1)
elif n == 2:
    print(n1,n2)
elif n == 3:
    print(n1,n2,n3)
else:
    print(n1,n2,n3,end=" ")
    for i in range(4,n+1):
        n4=n1+n2+n3
        print(n4, end=" ")
        n1=n2
        n2=n3
        n3=n4"""