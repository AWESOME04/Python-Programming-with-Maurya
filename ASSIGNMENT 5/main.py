# Python101task5- Assignment 5

# Evans Acheampong

# Question 1

def filters_on_key_substring(list_of_dicts, key):
    filtered_list = []
    for d in list_of_dicts:
        new_dict = {k: v for k, v in d.items() if key in k}
        filtered_list.append(new_dict)
    return filtered_list

print("")

# Question 2

def filter_by_key_substring(dictionary, keys):
    filtered_dict = {k: v for k, v in dictionary.items() if any(substring in k for substring in keys)}
    return filtered_dict

print("")

# Question 3

def sum_odd_values(list_of_dicts):
    new_dict = {}
    for d in list_of_dicts:
        for key, value in d.items():
            if value % 2 == 1:
                if key in new_dict:
                    new_dict[key] += value
                else:
                    new_dict[key] = value
    return new_dict

print("")


# Question 4

def filter_by_value(list_of_dicts, value):
    filtered_list = []
    for d in list_of_dicts:
        new_dict = {k: v for k, v in d.items() if v < value}
        filtered_list.append(new_dict)
    return filtered_list

print("")

# Question 5

def filter_by_multiple_of_3(list_of_dicts, key):
    filtered_list = []
    for d in list_of_dicts:
        if key in d:
            if d[key] % 3 == 0:
                filtered_list.append(d)
    return filtered_list

print("")


# Question 6

def filter_by_not_in_dict(list_of_tuples, dictionary):
    filtered_list = [tup for tup in list_of_tuples if tup[0] not in dictionary.keys()]
    return filtered_list

print("")


# Question 7

def get_key(dictionary, value, default=None):
    for k, v in dictionary.items():
        if v == value:
            return k
    return default

print("")


# Question 8

def sum_multiple_of_2_3(list_of_dicts):
    new_dict = {}
    for d in list_of_dicts:
        for key, value in d.items():
            if value % 2 == 0 and value % 3 == 0:
                if key in new_dict:
                    new_dict[key] += value
                else:
                    new_dict[key] = value
    return new_dict

print("")

# Question 9

def sort_by_value_length(list_of_dicts):
    sorted_list = []
    for d in list_of_dicts:
        new_dict = dict(sorted(d.items(), key=lambda x: len(str(x[1]))))
        sorted_list.append(new_dict)
    return sorted_list

print("")


# Question 10

def filter_by_greater_than(list_of_tuples, value):
    filtered_list = [tup for tup in list_of_tuples if all(i > value for i in tup)]
    return filtered_list


print("")


# Question 11

def count_occurrences(list_of_dicts):
    new_dict = {}
    for d in list_of_dicts:
        for key, value in d.items():
            if key in new_dict:
                new_dict[key] += 1
            else:
                new_dict[key] = 1
    return new_dict

print("")


# Question 12

def count_occurrences_greater_than(list_of_dicts, value):
    new_dict = {}
    for d in list_of_dicts:
        for key, val in d.items():
            if val in new_dict:
                new_dict[val] += 1
            else:
                new_dict[val] = 1
    final_dict = {k: v for k, v in new_dict.items() if v > value}
    return final_dict

print("")


# Question 13

def average_values(list_of_dicts):
    new_dict = {}
    for d in list_of_dicts:
        for key, value in d.items():
            if key in new_dict:
                new_dict[key][0] += value
                new_dict[key][1] += 1
            else:
                new_dict[key] = [value, 1]
    for key in new_dict:
        new_dict[key] = new_dict[key][0] / new_dict[key][1]
    return new_dict

print("")

# Question 14

def filter_by_prime(list_of_dicts, key):
    def is_prime(n):
        if n < 2:
            return False
        for i in range(2, int(n**0.5)+1):
            if n % i == 0:
                return False
        return True

    filtered_list = []
    for d in list_of_dicts:
        if key in d and is_prime(d[key]):
            filtered_list.append({key: d[key]})
    return filtered_list

print("")

# Question 15

def sort_dict_keys(list_of_dicts):
    sorted_list = []
    for d in list_of_dicts:
        sorted_dict = dict(sorted(d.items(), key=lambda x: len(x[0])))
        sorted_list.append(sorted_dict)
    return sorted_list

print("")


# Question 16

def sum_palindrome_values(list_of_dicts):
    result = {}
    for d in list_of_dicts:
        for key, value in d.items():
            if key == key[::-1]:
                if key in result:
                    result[key] += value
                else:
                    result[key] = value
    return result


print("")

# Question 17

def exclude_keys(dictionary, keys_to_exclude):
    result = {}
    for key, value in dictionary.items():
        if key not in keys_to_exclude:
            result[key] = value
    return result

print("")


# Question 18

def exclude_values(dictionary, values_to_exclude):
    result = {}
    for key, value in dictionary.items():
        if value not in values_to_exclude:
            result[key] = value
    return result

print("")


# Question 19

def nearest_value(dictionary, key):
    keys = list(dictionary.keys())
    keys.sort()
    if key in keys:
        return dictionary[key]
    else:
        closest_key = min(keys, key=lambda x: abs(x-key))
        return dictionary[closest_key]

print("")


# Question 20

def filter_tuples(tuples_list, dictionary):
    result = []
    for tup in tuples_list:
        if tup[0] in dictionary:
            result.append(tup)
    return result

print("")


# Question 21

def filter_by_keys(dictionary, keys_list):
    result = {}
    for key, value in dictionary.items():
        if key in keys_list:
            result[key] = value
    return result


print("")

# Question 22

def filter_by_values(dictionary, values_list):
    result = {}
    for key, value in dictionary.items():
        if value in values_list:
            result[key] = value
    return result

print("")

# Question 23

def filter_string_keys_values(list_of_dicts):
    result = []
    for d in list_of_dicts:
        string_dict = {k:v for k, v in d.items() if isinstance(k, str) or isinstance(v, str)}
        result.append(string_dict)
    return result

print("")


# Question 24

def multiply_values(dictionary, multiplier):
    result = {}
    for key, value in dictionary.items():
        result[key] = value * multiplier
    return result

print("")


# Question 25

def lowercase_keys(dictionary):
    result = {}
    for key, value in dictionary.items():
        result[key.lower()] = value
    return result

print("")

# Question 26

def uppercase_keys(dictionary):
    result = {}
    for key, value in dictionary.items():
        result[key.upper()] = value
    return result

print("")


# Question 27

def round_values(dictionary):
    result = {}
    for key, value in dictionary.items():
        result[key] = round(value)
    return result

print("")

# Question 28

def reverse_keys_values(dictionary):
    return {value: key for key, value in dictionary.items()}

print("")


# Question 29

def sort_keys_ascending(dictionary):
    return dict(sorted(dictionary.items()))

print("")


# Question 30

def sort_keys_descending(dictionary):
    return dict(sorted(dictionary.items(), key=lambda x: x[0], reverse=True))

print("")


# Question 31

def get_value_with_default(dictionary, key, default_value):
    return dictionary.get(key, default_value)
