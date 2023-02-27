def merge_sort(list, key_index):
    length = len(list)
    assert length, "List must contain at least 1 element"
    if length == 1:
        return list
    mid = length//2
    list1 = list[:mid]
    list2 = list[mid:]
    list1 = merge_sort(list1, key_index)
    list2 = merge_sort(list2, key_index)
    i = 0
    j = 0
    while i < len(list1) or j < len(list2):
        if i == len(list1):
            list[i+j] = list2[j]
            j += 1
        elif j == len(list2):
            list[i+j] = list1[i]
            i += 1
        else:
            if list1[i][key_index] < list2[j][key_index]:
                list[i+j] = list1[i]
                i += 1
            else:
                list[i+j] = list2[j]
                j += 1
    return list

if __name__ == "__main__":
    import random
    list = [[random.randint(1,20), random.randint(0,3)] for i in range(10)]
    print(list)
    list = merge_sort(list, 0)
    print(list)
    list = [[random.randint(1,20), random.randint(0,3)] for i in range(10)]
    print(list)
    list = merge_sort(list, 1)
    print(list)