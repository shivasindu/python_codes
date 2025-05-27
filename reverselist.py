#reverselist without builtin and slicing
original_list = [1, 2, 3, 4, 5]
reversed_list = []
for i in range(len(original_list) - 1, -1, -1):  
    reversed_list += [original_list[i]]
print("Reversed list:", reversed_list) 

#or

a = [1, 2, 3, 4, 5]
b = [a[i] for i in range(len(a) - 1, 0, -1)]  # `end` is now 0
print(b)
