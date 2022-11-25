# Find Longest word in given string

test_str = "Hello Welcome to the world of Python Programming"
list_str = test_str.split(' ')
dict_count = {}
list_count = []
for string in list_str:
    dict_count[len(string)] = string
    list_count.append(len(string))
print(dict_count.get(list_count[-1]))
