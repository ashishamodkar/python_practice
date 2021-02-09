grocery = ["Harpic", "Vim BAr", "Deodrent", "Bhindi"]
print(grocery)

numbers = [11, 1, 4, 7, 2, 3]

print(numbers)
# it is used to print specipic index nu.
print(4)
# There Are some function in list

# sort function is used to sort numbers by accending order

numbers.sort()
print(numbers)

# reverse is used to arrange number in desending order

numbers.reverse()
print(numbers)

# List Splicing

# List Slicing is like stringslicing only

# it Will print only from 1 to 5 index only
print(numbers[1:5])

# by default it contain 0 and the length on the list
print(numbers[:])
# it will print the length of list

print(len(numbers))

# Max Function is used to print Max number in list

print(max(numbers))

# Append Function is Used to add function at end of string or list

numbers.append(44)
numbers.sort()
print(numbers)

# Insert function is used to insert number in the particular index

numbers.insert(5, 74)
# numbers.sort()
print(numbers)

# pop()	Removes the element at the specified position

numbers.pop(4)
print(numbers)

