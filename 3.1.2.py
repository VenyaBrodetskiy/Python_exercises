def modify_list(l):
    i = 0
    while i < len(l):
        if l[i] % 2 == 0:
            l[i] = int(l[i] /  2)
            i += 1
        else:
            del l[i]
lst = [1, 2, 3, 4, 5, 6]
# print(modify_list(lst))  # None
print(lst)               # [1, 2, 3]
modify_list(lst)
print(lst)               # [1]

lst = [10, 5, 8, 3]
modify_list(lst)
print(lst)               # [5, 4]