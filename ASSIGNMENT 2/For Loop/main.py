# FOR LOOP SOLUTIONS ( Where Appropriate)
# Name: Evans Acheampong
# Student ID: PWM22117

# Question 1a
# First 10 Even Numbers

maximum = 20

for number in range(1, maximum + 1):

    if number % 2 == 0:
        print(number)


print("")

# Question 1 b
# First ten Odd Numbers

maximum = 20

for number in range(1, maximum + 1):

    if number % 2 != 0:
        print(number)

print("")

# Question 1 c
# First 10 Natural Numbers

maximum = 10

for number in range(1, maximum + 1):
    print(number)


print("")

# Question 1 d
# First 10 Whole Numbers

maximum = 10

for number in range(0, maximum + 1):
    print(number)

print("")


# Question 2
# First 10 integers and their squares(Integer, Corresponding square)

for i in range(1, 11):    # it's 11 because it ranges to 11 - 1, so 10
    print(i, i*i)

print("")


# Question 3
# Printing the series 10, 20, 30..... .....300

for i in range(10, 301, 10):
    print(i)

print("")


# Question 4
# For loop statement to print the series 105, 98, 91....7

for i in range(105, 8, -7):
    print(i)

print("")


# Question 5
# First 10 Natural Numbers in reverse

for i in range(10, 0, -1):
    print(i)

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
# We are using for loop for iterating the multiplication 10 times
print("The Multiplication Table of: ", number)
for count in range(1, 11):
    print(number, "x", count, "=", number * count)

print("")


# Question 9
# program to print all even numbers between two numbers (exclusive both numbers)

a = int(input("Enter first exclusive number: \n"))

b = int(input("Enter second exclusive number: \n"))

# Iterating each number in list
for num in range(a+2, b):

    # Checking condition
      if num % 2 == 0:
          print(num)


print("")

# Question 10
# Program to check whether a number is prime or not

# prime numbers are greater than 1, num is the entered number
Num = int(input("Enter a number: \n"))

if Num > 1:
   for i in range(2,Num):
       if (Num % i) == 0:
           print(Num,"is not a prime number")
           break
   else:
        print(Num,"is a prime number")


print("")

# Question 11
# Program to find the sum of the digits of a number

num_0 = input("Enter a number: \n")
add = 0
for n in num_0:
    add = add + int(n)
print(add, "is the sum of the digits of the number")



print("")


# Question 12
# Program to find the product of the digits of a number

Num_1 = input("Enter a number: \n")

mult = 1

for digit in Num_1:
    mult *= int(digit)

print("Product of the digits of the number:", mult)


print("")


# Question 13
# Program to reverse the number from a user using for loop

# take inputs
num_3 = input("Enter the number to be reversed: \n")

# calculate reverse of number
reverse = ''
for i in range(len(num_3), 0, -1):
   reverse += num_3[i-1]

# print reverse of number
print('The reverse number is ', reverse)


print("")



# Question 15
# program to print the Fibonacci series till terms

num_4 = int(input("Enter a number: \n"))
n1, n2 = 0, 1
print("Fibonacci Series:", n1, n2, end=" ")
for i in range(2, num_4):
    n3 = n1 + n2
    n1 = n2
    n2 = n3
    print(n3, end=" ")

print()







