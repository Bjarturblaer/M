"""a_str = input("Input a string: ")
count = 0
count_2 = 0
for i in a_str:
    if i.isupper():
        count = count + 1
    if i.islower():
        count_2 = count_2 + 1

print(count_2)
print(count)"""


"""a_str = float(input("Input a float: "))
justified_string = a_str.rjust(12)

print(round(justified_string,2))"""

"""a_str = input("Input a string: ")
words = 0
  
for i in range(len(a_str)):
    if a_str[index] == " ":
        words = words + 1
num_letters = len(a_str) - a_str.count(" ") - a_str.count(',') - a_str.count('.') - a_str.count('-')
result = 'No. of letters: {}, no. of words: {"}'.format(num_letters,words)
print(result)"""
# printing result  


 parts = name.split()
    initials = [part[0].upper() for part in parts[:-1]]
    return '.'.join(initials + [parts[-1]])


if __name__ == '__main__':
    name = input("Please enter your name?\n>")
    initial = initial_of_name(name)
    print("The initial of your name is {0}.".format(initial))



