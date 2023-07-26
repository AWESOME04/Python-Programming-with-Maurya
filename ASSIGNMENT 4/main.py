# Python101task4- Assignment 4

# Evans Acheampong

# Question 1
# Program that takes a list of integers and returns the sum of the integers.

def sum_of_list(numbers):
    total = 0
    for number in numbers:
        total += number
    return total

# example usage
print(sum_of_list([1, 2, 3, 4, 5])) # output: 15


print("")


# Question 2

# Program that takes a list of strings and returns the list in uppercase


def to_upper_case(strings):
    return [string.upper() for string in strings]

# example usage
print(to_upper_case(["hello", "world"]))

# ALTERNATIVELY
# str_list = list(input("Enter a list of strings: ").upper().split())
#
# print(str_list)

print("")


# Question 3

# Program that takes a list of numbers and returns the list with only even numbers

def even_numbers(numbers):
    return [number for number in numbers if number % 2 == 0]

# example usage
print(even_numbers([1, 2, 3, 4, 5])) # output: [2, 4]

print("")


# Question 4

# Program that takes a list of words and returns the longest word in the list

def longest_word(words):
    return sorted(words, key=len, reverse=True)[0]

# example usage
print(longest_word(["hello", "world", "python"])) # output: "python"

print("")


# Question 5

# Program that takes a list of integers and returns the smallest integer
def smallest_integer(numbers):
    return sorted(numbers)[0]

# example usage
print(smallest_integer([1, 2, 3, 4, 5])) # output: 1

print("")

# Question 6

# Program that takes a list of integers and returns True if the list is sorted in ascending order, False otherwise

def is_sorted(lst):
    return lst == sorted(lst)

print(is_sorted([1, 2, 3, 4, 5])) # True
print(is_sorted([5, 4, 3, 2, 1])) # False

print("")

# Question 7

# Program that takes a list of integers and returns the integers in ascending order

def sort_list(lst):
    return sorted(lst)

print(sort_list([3, 2, 1, 4, 5])) # [1, 2, 3, 4, 5]

print("")

# Question 8

# Program that returns the index at which the string is found in the list, or -1 if the string is not in the list

def find_string(lst, string):
    try:
        return lst.index(string)
    except ValueError:
        return -1

string_list = ["apple", "banana", "cherry"]
print(find_string(string_list, "banana")) # Output: 1
print(find_string(string_list, "orange")) # Output: -1

print("")

# Question 9

# Program that takes a list of integers and returns the average of the integers.

def find_average(numbers):
    return sum(numbers) / len(numbers)

numbers = [1, 2, 3, 4, 5]
print(find_average(numbers)) # Output: 3.0

print("")

# Question 10

# Program that takes a list of strings and returns a new list with all strings that have a length of at least 5 characters.

def filter_strings(lst):
    return [x for x in lst if len(x) >= 5]

string_list = ["apple", "banana", "cherry", "date"]
print(filter_strings(string_list)) # Output: ["banana", "cherry"]

print("")

# Question 11

# Program that takes a list of integers and returns the median value

def find_median(numbers):
    numbers.sort()
    if len(numbers) % 2 == 0:
        middle = len(numbers) // 2
        return (numbers[middle - 1] + numbers[middle]) / 2
    else:
        middle = len(numbers) // 2
        return numbers[middle]

print("")


# Question 12

# Program that takes a list of integers and returns the range (the difference between the largest and smallest integers)
def find_range(numbers):
    return max(numbers) - min(numbers)

numbers = [1, 2, 3, 4, 5]
print(find_range(numbers)) # Output: 4

print("")


# Question 13

# Program that takes a list of strings and returns a new list with all strings that start with the letter 'a'
def filter_strings(lst):
    return [x for x in lst if x.startswith('a')]

string_list = ["apple", "banana", "cherry", "date"]
print(filter_strings(string_list)) # Output: ["apple"]

print("")


# Question 14

# Program that takes a list of integers and returns a new list with the first and last elements swapped.
def swap_first_last(lst):
    lst[0], lst[-1] = lst[-1], lst[0]
    return lst

numbers = [1, 2, 3, 4, 5]
print(swap_first_last(numbers)) # Output: [5, 2, 3, 4, 1]


print("")


# Question 15

# Program that takes a list of integers and returns True if the list contains any duplicates, False otherwise.
def has_duplicates(lst):
    return len(lst) != len(set(lst))

numbers = [1, 2, 3, 4, 5]
print(has_duplicates(numbers)) # Output: False

numbers = [1, 2, 3, 4, 5, 3]
print(has_duplicates(numbers)) # Output: True


print("")


# Question 16

# Program that takes a list of integers and returns a new list with all duplicates removed.
def remove_duplicates(lst):
    return list(set(lst))

numbers = [1, 2, 3, 4, 5, 3, 2]
print(remove_duplicates(numbers)) # Output: [1, 2, 3, 4, 5]

print("")


# Question 17
# Program that takes a list of strings and returns a new list with all strings that are palindromes.
def find_palindrome(lst):
    return [x for x in lst if x == x[::-1]]

string_list = ["madam", "banana", "level", "radar"]
print(find_palindrome(string_list)) # Output: ["madam", "level", "radar"]


print("")


# Question 18
# Program that takes a list of integers and returns the product of all the integers
def find_product(lst):
    product = 1
    for x in lst:
        product *= x
    return product

print("")

# Question 19
# Program that takes a list of strings and returns a new list with all strings reversed.
def reverse_strings(lst):
    return [x[::-1] for x in lst]

string_list = ["hello", "world", "python"]
print(reverse_strings(string_list)) # Output: ["olleh", "dlrow", "nohtyp"]


print("")

# Question 20
# Program that takes a list of integers and returns the sum of the integers that are divisible by 3.
def sum_divisible_by_3(lst):
    return sum([x for x in lst if x % 3 == 0])

numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9]
print(sum_divisible_by_3(numbers)) # Output: 18


print("")

# Question 21
# Program that takes a list of strings and returns the longest string that is a palindrome.
def longest_palindrome(lst):
    palindromes = [x for x in lst if x == x[::-1]]
    palindromes.sort(key = len, reverse = True)
    return palindromes[0] if palindromes else None

string_list = ["madam", "banana", "level", "radar", "noon", "civic"]
print(longest_palindrome(string_list)) # Output: "madam"


print("")

# Question 22
# Program that takes a list of integers and returns the mode
from statistics import mode
def find_mode(lst):
    return mode(lst)

numbers = [1, 2, 2, 3, 4, 4, 4, 5]
print(find_mode(numbers)) # Output: 4

print("")


# Question 23
# program that takes a list of integers and returns a new list with only the prime numbers.
def prime_numbers(lst):
    primes = []
    for num in lst:
        if num > 1:
            for i in range(2,num):
                if (num % i) == 0:
                    break
            else:
                primes.append(num)
    return primes

numbers = [1,2,3,4,5,6,7,8,9,10]
print(prime_numbers(numbers)) # Output: [2, 3, 5, 7]

print("")

# Question 24
# Program that takes a list of strings and returns a new list with all strings sorted alphabetically.

def sort_strings(lst):
    return sorted(lst)

string_list = ["apple", "banana", "cherry", "date"]
print(sort_strings(string_list)) # Output: ["apple", "banana", "cherry", "date"]

print("")


# Question 25
# Program that takes a list of integers and returns the sum of the squares of the integers.

def squaresum(n):
    # Iterate i from 1
    # and n finding
    # square of i and
    # add to sum.
    sm = 0
    for i in range(1, n + 1):
        sm = sm + (i * i)

    return sm


# Driven Program
n = 4
print(squaresum(n))


print("")


# Question 26
# Program that takes a list of strings and returns a new list with all strings that contain the letter 'e'.
def filter_strings(strings):
    return [s for s in strings if 'e' in s]

print("")


# Question 27
# Program that takes a list of integers and returns a new list with only the odd numbers.

def filter_odd_numbers(numbers):
    return [n for n in numbers if n % 2 != 0]
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
print(filter_odd_numbers(numbers))

print("")

# Question 28
# Program that takes a list of strings and returns the shortest string in the list.

def shortest_string(strings):
    return min(strings, key=len)
strings = ["hello", "world", "goodbye", "python"]
print(shortest_string(strings))

print("")


# Question 29
# Program that takes a list of integers and returns the sum of the absolute values of the integers.

def sum_absolute_values(numbers):
    return sum(map(abs, numbers))
numbers = [-1, 2, -3, 4, -5, 6]
print(sum_absolute_values(numbers))

print("")


# Question 30
# Program that takes a list of integers and returns a new list with the integers in reverse order.

def reverse_list(numbers):
    return numbers[::-1]
numbers = [1, 2, 3, 4, 5, 6]
print(reverse_list(numbers))









