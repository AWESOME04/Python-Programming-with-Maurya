# Python101task3- Assignment 3

# Evans Acheampong

# Question 1

# Function to remove vowels from a string

def vowel_remover(string):
    vowels = ['a', 'e', 'i', 'o', 'u']
    result = [vowel for vowel in string if vowel.lower() not in vowels]
    result = ''.join(result)
    print(result)


# Program Test
string = "Python Program to remove vowels"
vowel_remover(string)

print("")

# Question 2

# Function to remove constants from a string

def const_remover(string):
    vowels = ['a', 'e', 'i', 'o', 'u']
    result = [vowel for vowel in string if vowel.lower() in vowels]
    result = ''.join(result)
    print(result)


# Program Test
string = "Python Program to remove vowels"
const_remover(string)

print("")

# Question 3

# Function to remove punctuations

def punc_remover(string):
    puncts = ['!', ',', ';', ':', '.', '""', '?', '(', ')', '-', '[]', '{}', '/', '<', '>']
    result = [punct for punct in string if punct not in puncts]
    result = ''.join(result)
    print(result)


# Program Test
string = "This is a python function. It is meant to remove, (punctuations)!."
punc_remover(string)

print("")

# Question 4

# Function to remove digits
def digit_remover(string):
    new_string = ''.join((x for x in string if not x.isdigit()))
    print(new_string)


# Program Test
string = "54321 Hello World 123456"
digit_remover(string)

print("")

# Question 5

# Function to remove whitespaces
def whitespace_remover(string):
    new_string = ''.join(string.split())
    print(new_string)


# Program Test
string = ' hello  apple  '
whitespace_remover(string)

print("")

# Question 6

# Function to reverse characters in a string

def reversed_string(string):
    result = ""
    for char in string:
        result = char + result
    return result


# Program Test
text = "This is Python Programming!"
print(reversed_string(text))

print("")

# Question 7

# Function to check for palindrome

def palindrome(s):
    s = s.replace(' ',
                  '')  # This replaces all spaces ' ' with no space ''. (Fixes issues with strings that have spaces)
    return s == s[::-1]  # Check through slicing


# Program Test
print(palindrome('nurses run'))

print("")

# Question 8

# Function that reverses words in a string

def word_reverse(text):
    return ' '.join(text.split()[::-1])


# Program Test

print(word_reverse("This is Python"))

print("")

# Question 9

# Function to Capitalize words in a string

def word_capitalize(text):
    return text.title()


# Program Test
print(word_capitalize("welcome to python programming"))

print("")

# Question 10

# Function to Make words lowercased in a string

def word_lowercased(text):
    return text.lower()


# Program Test
print(word_lowercased("WELCOME TO PYTHON PROGRAMMING"))

print("")

# Question 11

# Function to Make words uppercased in a string

def word_uppercased(text):
    return text.upper()


# Program Test
print(word_uppercased("welcome to python programming"))

print("")


# Question 12

# Function to determine frequency of string characters

def check_freqs(x):
    return {c: x.count(c) for c in set(x)}


print(check_freqs("ThisisPythonCode"))

print("")

# Question 13

# Function to remove duplicate characters

def unique_list(lst):
    # Also possible to use list(set())
    x = []
    for a in lst:
        if a not in x:
            x.append(a)
    return x

# Program Test
print(unique_list(["Good", "Good", "Nice", "Bad", "Nice"]))

print("")

# Question 14

# Function to remove a specific character

def remove_char(s, c):
    counts = s.count(c)
    s = list(s)
    while counts:
        s.remove(c)
        counts -= 1
    s = ''.join(s)

    print(s)


# Program Test
if __name__ == '__main__':
    s = "This is Python Programming"
    remove_char(s, 'P')

print("")

# Question 15

# Function that capitalizes the first  character

def word_capitalize(text):
    return text.title()


# Program Test
print(word_capitalize("welcome to python programming"))

print("")

# Question 16

# Function to capitalize last letter of each word in a string

def last_word_cap(str):
    # lambda function for capitalizing the first and last letter of words in the string
    return ' '.join(map(lambda s: s[:-1] + s[-1].upper(), s.split()))


# Program Test
s = "This is python programming"
print("String before Capilization:", s)
print("String after Capilization:", last_word_cap(str))

print("")


# Question 17

# Function that capitalizes te first and last characters of a string

def word_cap(str):
    # lambda function for capitalizing the first and last letter of words in the string
    return ' '.join(map(lambda s: s[:-1] + s[-1].upper(), s.title().split()))


# Program Test
s = "This is python programming"
print("String before Capilization:", s)
print("String after Capilization:", word_cap(str))

print("")

# Question 18

# Function to sort words in a string alphabetically

def sort_string(str):
    return ''.join(sorted(str))

# Program Test
str = 'programming'
print(sort_string(str))

print("")

# Question 19

# Function to sort words in a string in reverse alphabetical order

def sort_string(str):
    return ''.join(sorted(str, reverse=True))

# Program Test
str = 'programming'
print(sort_string(str))

print("")

# Question 20

# Function to capitalize the longest word in the string

def cap_longest_word(words_list):
    word_len = []
    for n in words_list:
        word_len.append((len(n), n))
    word_len.sort()
    return word_len[-1][0], word_len[-1][1]

# Program Test
result = cap_longest_word(["this", "is", "python", "programming"])
print("Capitalized Longest word: ", result[1].capitalize())

print("")

# Question 21

# Function to capitalize the shortest word in the string

def cap_shortest_word(words_list):
    word_len = []
    for n in words_list:
        word_len.append((len(n), n))
    word_len.sort(reverse=True)
    return word_len[-1][0], word_len[-1][1]

# Program Test
result = cap_shortest_word(["this", "is", "python", "programming"])
print("Capitalized Shortest word: ", result[1].capitalize())


print("")

# Question 22

# Function to remove the longest word in the string

def remove_long_words_gen(items):
    max_len = 0
    cache = []
    for item in items:
        size = len(item)
        if size > max_len:
            # this item is now the longest item
            max_len = size
            # anything previously seen can be yielded and purged from the cache
            yield from (cached for _, cached in cache)
            cache = [(size, item)]
        else:
            # this item might be smaller than the max item,
            # but cannot be yielded yet to preserve the collection's order
            cache.append((size, item))
            # and now cleanup
    for size, item in cache:
        if size != max_len:
                yield item
def remove_long_words(items):
    return list(remove_long_words_gen(items))

# Program Test
stri = ["one", "two", "threee"]
print(remove_long_words(stri))


print("")


# Question 23

# Function to remove the shortest word in the string

def remove_short_words(list_):
    max_length = min(len(word) for word in list_)
    return [word for word in list_ if len(word) > max_length]

# Program Test
test = ["good", "as", "coding"]
print(remove_short_words(test))

print("")


# Question 24

# Function to replace all occurrences of character c1 with character c2

def replaceCharacter(input, c1, c2):
    input = list(str)
    for i in range(0, len(str)):
        if (input[i] == c1):
            input[i] = c2

        # Print the string
        print(input[i], end="")

# Program Test
str = "Python"
c1 = 'o'
c2 = 'a'
replaceCharacter(str, c1, c2);


print("")


# Question 25

# Function to replace all occurrences of word with another word
def replacer(data, word, replace_str):
    info = data.split(word)
    replace_str.join(info)


print("")


# Question 26

# Function to sort words in a string by their lengths
def printArraystring(string, n):
    for i in range(n):
        print(string[i], end = " ")

# Function to Sort the array of string according to lengths. This function implements Insertion Sort.
def sort(s, n):
    for i in range(1, n):
        temp = s[i]

        # Insert s[j] at its correct position
        j = i - 1
        while j >= 0 and len(temp) < len(s[j]):
            s[j + 1] = s[j]
            j -= 1

        s[j + 1] = temp

# Program Test
if __name__ == "__main__":
    arr = ["Programming?", "this", "Python", "Is"]
    n = len(arr)

    # Function to perform sorting
    sort(arr, n)

    # Calling the function to print result
    printArraystring(arr, n)


print("")

# Question 27

# Function to sort words in a string by their lengths in reverse order

def Sorting(lst):
    lst2 = sorted(lst, key=len, reverse=True)
    return lst2


# Program Test
lst = ["Programming?", "this", "Python", "Is"]
print(Sorting(lst))


print("")


# Question 28

# Function to sort the words in alphabetical order with vowels before constants
class Solution:
   def solve(self, s):
      vowels = 'aeiou'
      k = ''
      t = ''
      for c in s:
         if c in vowels :
            k = k + c
         else :
            t = t + c
            k = ''.join(sorted(k))
            t = ''.join(sorted(t))
      return k + t

# Program Test
ob = Solution()
print(ob.solve("helloworld"))


print("")


# Question 29

# Function to sort the words in alphabetical order with constants before vowels

class Solution:
   def solve(self, s):
      vowels = 'aeiou'
      k = ''
      t = ''
      for c in s:
         if c in vowels :
            t = t + c
         else :
            k = k + c
            k = ''.join(sorted(k))
            t = ''.join(sorted(t))
      return k + t

# Program Test
ob = Solution()
print(ob.solve("helloworld"))


print("")


# Question 30

# Function to sort the words in alphabetical order with punctuations before letters

class Solution:
   def solve(self, s):
      puncts = ['!', ',', ';', ':', '.', '""', '?', '(', ')', '-', '[]', '{}', '/', '<', '>']
      k = ''
      t = ''
      for c in s:
         if c in puncts:
            k = k + c
         else :
            t = t + c
            k = ''.join(sorted(k))
            t = ''.join(sorted(t))
      return k + t

# Program Test
ob = Solution()
print(ob.solve("hello!!,.;wor1ld12345"))

