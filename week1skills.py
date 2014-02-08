# Things you should be able to do.
animals = ['cat','dog', 'fish', 'gorilla', 'baloonicorn', 'monkey', 'cheese']
numbers = range(1,10)

# Write a function that takes a list and returns a new list with only the odd numbers.
def all_odd(some_list):
    new_list = []
    for i in range(len(some_list)):
        if i % 2 == 1:
            addme = some_list[i]
            new_list.append(addme)
    return new_list

print all_odd(numbers)

# Write a function that takes a list and returns a new list with only the even numbers.
def all_even(some_list):
    new_list = []
    for i in range(len(some_list)):
        if i % 2 == 0:
            new_list.append(some_list[i])
    return new_list

print all_even(numbers)

# Write a function that takes a list of strings and a new list with all strings of length 4 or greater.
def long_words(word_list):
    new_list = []
    for i in range(len(word_list)):
            if len(word_list[i]) >= 4:
                new_list.append(word_list[i])
    return new_list
print long_words(animals)

# Write a function that finds the smallest element in a list of integers and returns it.
def smallest(some_list):
    minnumber = some_list[0]
    for i in range(len(some_list)):
        if some_list[i] <= minnumber:
            minnumber = some_list[i]
    return minnumber
print smallest(numbers)

# Write a function that finds the largest element in a list of integers and returns it.
def largest(some_list):
    maxnumber = some_list[0]
    for i in range(len(some_list)):
        if some_list[i] >= maxnumber:
            maxnumber = some_list[i]
    return maxnumber

print largest(numbers)

# Write a function that takes a list of numbers and returns a new list of all those numbers divided by two.
def halvesies(some_list):
    halflist = []
    for i in range(len(some_list)):
        halflist.append((some_list[i]/2))
    return halflist

print halvesies(numbers)

# Write a function that takes a list of words and returns a list of all the lengths of those words.
def word_lengths(word_list):
    lengthlist = []
    for i in range(len(word_list)):
        length = len(word_list[i])
        lengthlist.append(length)
    return lengthlist
print word_lengths(animals)

# Write a function (using iteration) that sums all the numbers in a list.
def sum_numbers(numbers):
    total = 0
    for i in range(len(numbers)):
        total = total + numbers[i]
    return total
print sum_numbers(numbers)

# Write a function that multiplies all the numbers in a list together.
def mult_numbers(numbers):
    product = 1
    for i in range(len(numbers)):
        product = product * numbers[i]
    return product

print mult_numbers(numbers)

# Write a function that joins all the strings in a list together (without using the join method) and returns a single string.
def join_strings(string_list):
    big_string = ""
    for i in range(len(string_list)):
        big_string = big_string + string_list[i]
    return big_string

print join_strings(animals)

# Write a function that takes a list of integers and returns the average (without using the avg method)
def average(numbers):
    total = 0
    counter = 0
    for i in range(len(numbers)):
        total = total + numbers[i]
        counter += 1
    return total/counter

print average(numbers)

