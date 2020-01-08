numbers_list = [2, 6, 8, 10, 11, 4, 12, 7, 13, 17, 0, 3, 21]

mapped_list = list(map(lambda num: num % 2, numbers_list))

print(mapped_list)

# map(object, iterable_1, iterable_2, ...)
# The iterable to the map() function can be a dictionary, a list, etc. The map() function basically maps every item in the input iterable to the corresponding item in the output iterable, according to the logic defined by the lambda function
