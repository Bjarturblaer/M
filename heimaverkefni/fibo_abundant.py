quiz = (input("Input f|a|b (fibonacci, abundant or both): "))

if quiz == "f":
    length = int(input("Input the length of the sequence: "))

    a = 0
    b = 1
    
    
    print("Fibonacci Sequence:")
    print("-------------------")
    print(a)
    print(b)
    for i in range (2,length):
        c = a + b
        a = b
        b = c
        print(c)

elif quiz == "a":
    max_number = int(input("Input the max number to check: "))
    print("Abundant numbers:")
    print("-----------------")
    sum = 0
    max_number +=1  
    for i in range(1, max_number):  
        for j in range(1, int(i)):  
            if (i % j == 0):  
                sum = sum + j  
        if (sum > i):  
            print( i)
         
        sum = 0 
    

elif quiz == "b":
    length = int(input("Input the length of the sequence: "))

    a = 0
    b = 1
    print("Fibonacci Sequence:")
    print("-------------------")
    print(a)
    print(b)
    
    for i in range (2,length):
        c = a + b
        a = b
        b = c
        print(c)

    
    max_number = int(input("Input the max number to check: "))
    print("Abundant numbers: ")
    print("-----------------")
    sum = 0  
    max_number +=1
    for i in range(1, max_number):  
        for j in range(1, int(i)):  
            if (i % j == 0):  
                sum = sum + j  
        if (sum > i):  
            print( i)
    
        sum = 0 
    
    

    
    
    
    
    
    
    
    
    
    
    
    
    
    
    



