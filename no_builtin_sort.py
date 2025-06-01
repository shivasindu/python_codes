numbers = [3, 5, 1, 9, 2, 8]
for i in range(len(numbers)):
    for j in range(i + 1, len(numbers)):
        if numbers[i] > numbers[j]:
            numbers[i], numbers[j] = numbers[j], numbers[i]
print("Sorted list:", numbers)
