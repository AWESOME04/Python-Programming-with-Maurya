# Python101task1- Assignment 1

# Question 1

num = int(input("Enter any value of n: \n"))

tot = sum([a * (a + 1) / 2 for a in range(1, num + 1)])
print("The sum of the series is ", tot)
num = 2


joke = input("Why does the cow cross the road?: ")

if joke == "":
    print("Because it was moooving!")


print("")
# Question 2


a = 5
b = a * 2
c = b - 1

list = [a, b, c]
for item in list:
    print(item)

# Alternative Method
# print(a)
# print(b)
# print(c)


print("")
# Question 3

a = 5
b = a * 2
c = b - 1
print(str(a) + "@" + str(b) + "@" + str(c))


print("")
# Question 4
radius = int(input("Enter the radius of the circle: \n"))

area_of_circle = 3.142 * radius ** 2

print("Area of the circle is " + str(area_of_circle) + " square units")


print("")
# Question 5
Maths_mark = int(input("Enter your Maths mark: \n"))

English_mark = int(input("Enter your English mark: \n"))

Physics_mark = int(input("Enter your Physics mark: \n"))

Chemistry_mark = int(input("Enter your Chemistry mark: \n"))

French_math = int(input("Enter your French mark: \n"))

Number_of_subjects = 5

Sum = Maths_mark + English_mark + Physics_mark + Chemistry_mark + French_math

Average = Sum / Number_of_subjects

print(str(Average) + " is the average of the 5 subjects")


print("")
# Question 6

height_in_cm = int(input("Enter your height(in cm): \n"))

height_in_ft = height_in_cm * 12

print("Your height in feet is " + str(height_in_ft))

height_in_inches = height_in_cm * 2.54

print("Your height in inches is " + str(height_in_inches))


print("")
# Question 7

number = int(input("Enter a number: \n"))

k = int(input("Enter an exponent: \n"))

print(number ** 2, number ** 3, number ** k)


print("")
# Question 8

triangle_height = int(input("Enter the height of the traingle: \n"))

triangle_base = int(input("Enter the base of the traingle: \n"))

triangle_area = 0.5 * triangle_base * triangle_height

print("The Area of the triangle is " + str(triangle_area) + " square units")


print("")
# Question 9

# Reading Principle amount, rate and time
principle = float(input("Enter amount: \n"))
time = float(input("Enter time: \n"))
rate = float(input("Enter rate: \n"))

# Calculation
simple_interest = (principle *time *rate /100)
compound_interest = principle * ( (1+rate/100)**time - 1)

# Displaying result
print("Simle interest is : %f " % (simple_interest))
print("compound interest is: %f" % (compound_interest))


# Question 10

num = int(input("Enter a number: \n"))

print("First five multiples of", num,"are")
print(num, num * 2,num * 3,num * 4, num * 5)



print("")
# Question 11

name = str(input("Enter your name: \n"))

Class = input("Enter your class: \n")

age_of_student = int(input("Enter your age: \n"))

# Printing the details in the same line
print(name, Class, age_of_student)

print("")
print("")

# Printing the details on different lines
# print(name,"\n", Class,"\n",age_of_student)

# Alternative
List_of_details = [name, Class, age_of_student]
for detail in List_of_details:
    print(detail)


print("")

# Question 12

digit = int(input("Enter a single digit (in range of 1-7): \n"))

factorial = digit * (digit + 1) * (digit + 2)

if digit in range(8):
    print(factorial)
else:
    print("Digit must be in range of 1-7!")


print("")

# Question 13

x = int(input("Enter first number: \n"))
y = int(input("Enter second number: \n"))
z = int(input("Enter third number: \n"))

# Swapping the variables
x, y = x+y, y+z

print(x, y)



