# Python101task6- Assignment 6

# Evans Acheampong

# Question 1

def greet(name):
    print("Hello, " + name + "!")

# Call the function with different values of name
greet("John")
greet("Jane")
greet("Bob")

print("")


# Question 2

def add(x, y):
    return x + y

print(add(1, 2)) # Output: 3
print(add(3, 4)) # Output: 7
print(add(-1, -2)) # Output: -3

print("")


# Question 3

def is_even(x):
    if x % 2 == 0:
        return True
    else:
        return False

print(is_even(2)) # Output: True
print(is_even(3)) # Output: False
print(is_even(0)) # Output: True

print("")


# Question 4

def sum_all(*args):
    return sum(args)


print(sum_all(1, 2, 3)) # Output: 6
print(sum_all(4, 5, 6, 7)) # Output: 22
print(sum_all(1, 2, 3, -4, -5)) # Output: -3


print("")


# Question 5

def greet_all(names):
    for name in names:
        print("Hello, " + name + "!")

greet_all(["John", "Mary", "Bob"])
# Output: Hello, John!
#         Hello, Mary!
#         Hello, Bob!

greet_all(["Alice", "Bob"])
# Output: Hello, Alice!
#         Hello, Bob!

greet_all(["Mike"])
# Output: Hello, Mike!


print("")


# Question 6

def average(values):
    return sum(values) / len(values)

print(average([1, 2, 3])) # Output: 2.0
print(average([4, 5, 6, 7])) # Output: 5.5
print(average([1, 2, 3, -4, -5])) # Output: -0.4


print("")


# Question 7

def count_vowels(string):
    vowels = "aeiouAEIOU"
    return sum(c in vowels for c in string)

# Test the function
print(count_vowels("hello")) # 2
print(count_vowels("world")) # 1
print(count_vowels("This is a sentence")) # 4


print("")


# Question 8

def reverse(string):
    return string[::-1]

# Test the function
print(reverse("hello")) # "olleh"
print(reverse("world")) # "dlrow"
print(reverse("This is a sentence")) # "ecnetnis a si sihT"

print("")


# Question 9

def sort(values):
    return sorted(values)

# Test the function
print(sort([3,1,2])) # [1,2,3]
print(sort([-1,5,3,-2])) # [-2,-1,3,5]
print(sort([3.14,2.718,1.618])) # [1.618, 2.718, 3.14]


print("")


# Question 10

def is_palindrome(string):
    return string == string[::-1]

# Test the function
print(is_palindrome("hello")) # False
print(is_palindrome("madam")) # True
print(is_palindrome("racecar")) # True

print("")


# Question 11

def maximum(values):
    return max(values)

# Test the function
numbers = [1, 2, 3, 4, 5, 6]
print(maximum(numbers)) # 6

numbers2 = [1, 3, 2, 4, 5, 6]
print(maximum(numbers2)) # 6

numbers3 = [6, 5, 4, 3, 2, 1]
print(maximum(numbers3)) # 6

print("")


# Question 12

def minimum(values):
    return min(values)

# Test the function
numbers = [1, 2, 3, 4, 5, 6]
print(minimum(numbers)) # 1

numbers2 = [1, 3, 2, 4, 5, 6]
print(minimum(numbers2)) # 1

numbers3 = [6, 5, 4, 3, 2, 1]
print(minimum(numbers3)) # 1

print("")


# Question 13

def count(values, target):
    return values.count(target)

# Test the function
print(count([1,2,3,4,5], 2)) # 1
print(count([1,2,3,4,5,2,2], 2)) # 3
print(count([-1,-2,-3,-4,-5], -2)) # 1

print("")


# Question 14

def find(values, target):
    try:
        return values.index(target)
    except ValueError:
        return None

# Test the function
print(find([1,2,3,4,5], 2)) # 1
print(find([1,2,3,4,5,2,2], 6)) # None
print(find([-1,-2,-3,-4,-5], -2)) # 1

print("")


# Question 15

def remove(values, target):
    while target in values:
        values.remove(target)

# Test the function
numbers = [1, 2, 3, 4, 2, 5, 2, 6]
remove(numbers, 2)
print(numbers) # [1, 3, 4, 5, 6]

numbers2 = [1, 2, 3, 4, 2, 5, 2, 6]
remove(numbers2, 7)
print(numbers2) # [1, 2, 3, 4, 2, 5, 2, 6]

numbers3 = [1, 2, 3, 4, 2, 5, 2, 6]
remove(numbers3, 1)
print(numbers3) # [2, 3, 4, 2, 5, 2, 6]

print("")


# Question 16

def is_sorted(values):
    return values == sorted(values)

# Test the function
numbers = [1, 2, 3, 4, 5, 6]
print(is_sorted(numbers)) # True

numbers2 = [1, 3, 2, 4, 5, 6]
print(is_sorted(numbers2)) # False

numbers3 = [6, 5, 4, 3, 2, 1]
print(is_sorted(numbers3)) # False


# Question 17

def is_anagram(string1, string2):
    return sorted(string1) == sorted(string2)

# Test the function
print(is_anagram('listen', 'silent')) # True
print(is_anagram('listen', 'silents')) # False
print(is_anagram('listen', 'listen')) # True
print(is_anagram('listen', 'silen')) # False

print("")


# Question 18

def fizzbuzz(n):
    for i in range(1, n+1):
        if i % 3 == 0 and i % 5 == 0:
            print("FizzBuzz")
        elif i % 3 == 0:
            print("Fizz")
        elif i % 5 == 0:
            print("Buzz")
        else:
            print(i)

# Test the function
fizzbuzz(20)


# Question 19

def factorial(n):
    if n == 0:
        return 1
    else:
        return n * factorial(n-1)

# Test the function
print(factorial(5)) # 120
print(factorial(0)) # 1
print(factorial(1)) # 1
print(factorial(4)) # 24

print("")


# Question 20

def fibonacci(n):
    if n == 0:
        return []
    elif n == 1:
        return [1]
    elif n == 2:
        return [1, 1]
    else:
        fib = [1, 1]
        for i in range(2, n):
            fib.append(fib[i-1] + fib[i-2])
        return fib

# Test the function
print(fibonacci(5)) # [1, 1, 2, 3, 5]
print(fibonacci(0)) # []
print(fibonacci(1)) # [1]
print(fibonacci(10)) # [1, 1, 2, 3, 5, 8, 13, 21, 34, 55]

print("")

