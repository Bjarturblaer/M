
#dæmi 1
"""def find_max(a,b): 
      
    if a >= b: 
        return a 
    else: 
        return b 

first = int(input("Enter first number: "))
second = int(input("Enter second number: "))

print("Maximum: ", find_max(first, second))"""

#dæmi 2

# Your function definition goes here
"""def count_case(s):
    d={"upper":0, "lower":0}
    for c in s:
        if c.upper():
           d["upper"]+=1
        elif c.lower():
           d["lower"]+=1
        else:
           pass

user_input = input("Enter a string: ")

# Call the function here

print("Upper case count: ", upper)
print("Lower case count: ", lower)"""



"""def count_case(): 
    UpperCount = 0 
    LowerCount = 0
    user_input = input("Enter a string: ")
    for letter in word:
        if letter == upper 
            UpperCount = UpperCount + 1
            return UpperCount
        else:
            LowerCount = LowerCount + 1
            return LowerCount"""

#print(count_case())
#print("Upper case count: ", upper)
#print("Lower case count: ", lower)



"""def count_case(sentence):
upper = 0
lower = 0
for i in sentence:
if i >='A' and i <= 'Z':
upper += 1
elif i >= 'a' and i <= 'z':
lower += 1
print("Upper case: " + (pper))
print("Lower case: " + str(lower))"""


"""def count_case(str):
    for x in str:
        if x.isupper():
            upper_count+=1
        else:
            lower+=1
# Your function definition goes here

user_input = input("Enter a string: ")
upper=0
lower=0
# Call the function here

print("Upper case count: ", upper)
print("Lower case count: ", lower)"""

"""def count_case(string):
   upper = 0
   lower = 0
   for i in range(len(string)):
      if (ord(string[i]) >= 97 and
         ord(string[i]) <= 122):
         lower += 1
      elif (ord(string[i]) >= 65 and
         ord(string[i]) <= 90):
         upper += 1
   print('Lower case characters = '+str(lower))
   print('Upper case characters = '+str(upper))
# Driver Code
string = 'TutorialsPoint'
count_case(string)"""

"""def count_case(string):
   upper = 0
   lower = 0
   for i in range(len(string)):
      if (ord(string[i]) >= 97 and
         ord(string[i]) <= 122):
         lower += 1
      elif (ord(string[i]) >= 65 and
         ord(string[i]) <= 90):
         upper += 1
# Your function definition goes here

user_input = input("Enter a string: ")

# Call the function here
count_case(user_input)

print("Upper case count: ", upper)
print("Lower case count: ", lower)"""

"""def count_case(str):
    upper=0
    lower=0
    for x in str:
        if x.isupper():
           upper+=1
        elif x.islower():
           lower+=1
        else:
            pass

    print ("Upper case count: ", upper)
    print ("Lower case count: ", lower)
user_input = input("Enter a string: ")
count_case(user_input)"""



# Program to check if a number is prime or not

num = 2

# To take input from the user
#num = int(input("Enter a number: "))

# prime numbers are greater than 1
"""if num > 1:
   # check for factors
   for i in range(2,num):
       if (num % i) == 0:
           print(num,"is not a prime number")
           print(i,"times",num//i,"is",num)
           break
   else:
       print(num,"is a prime")
       
# if input number is less than
# or equal to 1, it is not prime
else:
   print(num,"is not a prime")"""

#'apa'
#"apa"
#"""""""
fibo = int(input("Input the length of Fibonacci sequence (n>=1): "))

# Your function definition goes here
n1, n2 = 0, 1
count = 0


if fibo <= 0:
   print("Please enter a positive integer")
elif fibo == 1:
   print("Fibonacci sequence upto",fibo,":")
   print(n1)
else:
   print("Fibonacci sequence:")
   while count < fibo:
      
       nth = n1 + n2
      
       n1 = n2
       n2 = nth
       count += 1 
       print(n1)
  

  


# Call your function here        


