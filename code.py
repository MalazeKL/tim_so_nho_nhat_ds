def Min_of_List(lst):
    min = lst[0]
    for i in range(len(lst)):
        if min > lst[i]:
            min = lst[i]
    return min
l = [3, 5, 6, 3, 5, 2, 3, 6, 9]
print("số nhỏ nhấn trong danh sách là ", Min_of_List(l))
