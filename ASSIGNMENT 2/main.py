# WHILE LOOP SOLUTIONS
# Name: Evans Acheampong
# Student ID: PWM22117

# Question 1 a
# First 10 Even Numbers

# To calculate sum of the following series

while num <= 20:
    print(num)
    num += 2

print("")


# Question 1 b
# First ten Odd Numbers

f = 1

while(f <= 10):
    print(2 * f - 1)
    f = f + 1

print("")


# Question 1 c
# First 10 Natural Numbers

j = 1
while j <= 10:
    print(j)
    j += 1

print("")

# Question 1 d
# First 10 Whole Numbers

k = 0
while k <= 9:
    print(k)
    k += 1

print("")


# Question 2
# First 10 integers and their squares

o = 1
while o <= 10:
    # To print First 10 Integers and their squares (Integer, Corresponding square):
    print(o, o*o)
    o += 1


print("")


# Question 3
# Printing the series 10, 20, 30..... .....300
l = 10
while l <= 300:
    print(l)
    l += 10

print("")


# Question 4
# While loop statement to print the series 105, 98, 91....7

m = 105
while m >= 7:
    print(m)
    m -= 7


print("")


# Question 5
# First 10 Natural Numbers in reverse

p = 10

while(p >= 1):
    print(p)
    p -= 1

print("")

# Question 6
# Program to print sum of first 10 Natural Numbers

sum = 0
for num in range(0, 11, 1):
    sum += num
print("SUM of first ten natural numbers is: ", sum )


print("")


# Question 7
# Program to print sum of first 10 Even Numbers

sums = 0
for nums in range(0, 21, 2):
    sums += nums
print("SUM of first ten even numbers is: ", sums )


print("")


# Question 8
# Program to print table of a number entered from a user

number = int(input("Enter the number for it's multiplication table: \n"))
count = 1
i = 1
# We are using while loop for iterating the multiplication 10 times
print("The Multiplication Table of: ", number)
while count <= 10:
    number = number * 1
    print(number, "x", i, "=", number * count)
    count += 1
    i += 1


print("")


# Question 9
# program to print all even numbers between two numbers (exclusive to both numbers)

a = int(input("Enter first exclusive number: \n"))

b = int(input("Enter second exclusive number: \n"))

# using while loop

num = a + 2

while num < b:
    if(num % 2 == 0):
        print("{0}".format(num))
    num = num + 1


print("")

# Question 10
# Program to check whether a number is prime or not

flag = 0
h = int(input('Enter whole number to check : \n'))
c = 2
while c <= (h/2):
    if (h % c) == 0:
        flag = 1
        break
    c += 1
if h == 1:
    print('1 is neither prime nor composite')
elif flag == 0:
    print(h, ' is a prime number.')
elif flag == 1:
    print(h, ' is not a prime number.')


print("")

# Question 11
# Program to find the sum of the digits of a number

Q =int(input("Enter a number:"))
tot=0
while(Q > 0):
    dig = Q % 10
    tot = tot + dig
    Q = Q // 10
print("The total sum of digits is:",tot)

print("")


# Question 12
# Program to find the product of the digits of a number

# Take input from user
num_2 = int(input("Enter a number: \n"))

temp = num_2

product = 1

while(temp != 0):

    product = product * (temp % 10);

    # Remove last digit from temp.
    temp = int(temp / 10)

print("\nProduct of all digits in", num_2, ":", product)



print("")

# Question 13
# Program to reverse the number from a user

num_4 = int(input("Enter the numbers to be reversed!: \n"))
reversed_num = 0

while num_4 != 0:
    digit = num_4 % 10
    reversed_num = reversed_num * 10 + digit
    num_4 //= 10

print("Reversed Number: " + str(reversed_num))


print("")


# Question 14
# Program to display the number names of the digits of a number entered by user

num_5 = input("Enter the numbers: \n")

print("The length of the numbers is: ", len(str(num_5)))


print("")

# Question 15
# program to print the Fibonacci series till terms

num_8 = int(input("Enter the nth value: "))
A = 0
B = 1
SUM = 0
print("Fibonacci Series : ", end = " ")
while(SUM <= num_8):
     print(SUM, end = " ")
     A = B
     B = SUM
     SUM = A + B


print("")


# Question 16
# program to print the factorial of a number accepted from user
num_7 = int(input("Enter a number: \n"))

factorial = 1
if num_7 < 0:
    print("Factorial does not exist for negative numbers")
elif num_7 == 0:
    print("The factorial of 0 is 1")
else:
    for E in range(1, num + 1):
        factorial = factorial * E
    print("The factorial of ", num, "is ", factorial)


# To calculate sum of the following series
num = int(input("Enter any value of n: \n"))

tot = tot([a * (a + 1) / 2 for a in range(1, num + 1)])
print("The sum of the series is ", tot)

print("")

n = int(input("Enter value of n: "))

sum = sum([i*(i+1)/2 for i in range(1, n+1)])
print(sum)


# Question 17
# Program to check if the number is an Armstrong number or not

# take input from the user
num_6 = int(input("Enter a number: "))

# initialize sum
Sum = 0

# find the sum of the cube of each digit
temps = num_6
while temps > 0:
   digit = temps % 10
   Sum += digit ** 3
   temps //= 10

# display the result
if num_6 == Sum:
   print(num_6, "is an Armstrong number")
else:
   print(num_6, "is not an Armstrong number")









