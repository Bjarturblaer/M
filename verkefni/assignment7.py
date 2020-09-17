"""def max_of_three(first, second, third): 

    if first >= second and first >= third: 
        max_num = first
  
    elif (second >= first) and (second >= third): 
        max_num = second 
    else: 
        max_num = third 
          
    return max_num 
  
first = int(input("Enter first number: "))
second = int(input("Enter second number: "))
third = int(input("Enter third number: "))
maximum = max_of_three(first,second,third)

print("Maximum:", maximum)"""

"""def is_prime(a):
    if a == 2:
        return True
    else:
        for i in range(2,a):
            if n % i == 0:
                return False
        return True

for j in range (2, max_num+1):
    if is_prime(j) == False:
        print(j, "is not a prime")
    elif is_prime(j) == True:
        print(j, "is a prime")"""

"""def isPalindrome(in_str): 
    return in_str == in_str[::-1] 
  
  

in_str = input("Enter a string: ")
ans = isPalindrome(in_str) 
  
if ans:
    print('"'+in_str+'"'" is a palindrome.") 
else: 
    print('"'+in_str+'"'" is not a palindrome.") """
date_str = input("Enter a date: ")
def valid_date(date_str):
    day_count_for_month = [0, 31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
    if year%4==0 and (year%100 != 0 or year%400==0):
        day_count_for_month[2] = 29
    return (1 <= month <= 12 and 1 <= day <= day_count_for_month[month])

if valid_date(date_str):
    print("Date is valid")
else:
    print("Date is invalid")




  
