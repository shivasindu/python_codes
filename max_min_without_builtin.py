numbers = [5, 9, 1, 7, 3, 10, 2]
max_num = numbers[0]
min_num = numbers[0]

for num in numbers:
    if num > max_num:
        max_num = num
    if num < min_num:
        min_num = num

print("Maximum element is:", max_num)
print("Minimum element is:", min_num)
