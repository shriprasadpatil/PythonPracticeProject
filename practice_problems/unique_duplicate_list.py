# List contains duplicate and unique -> get output as separate list of duplicates and unique

list_duplicate_unique = [1, 2, 3, 3, 4, 4, 5, 6, 7, 7, 8, 9, 10, 11, 11, 12, 12]


def get_lists(number_list):
    # initialize a null list
    list_unique = []
    list_duplicate = []
    # traverse for all elements
    for x in number_list:
        # check if exists in unique_list or not
        if x not in list_unique:
            list_unique.append(x)
        else:
            list_unique.remove(x)
            list_duplicate.append(x)
    return list_unique, list_duplicate


unique_list, duplicate_list = get_lists(list_duplicate_unique)
print(unique_list)
print(duplicate_list)
