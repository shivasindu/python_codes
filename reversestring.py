s = input("Enter a string: ")
reversed_str = ""
for i in range(len(s)-1, -1, -1):
    reversed_str += s[i]
print("Reversed string:", reversed_str)
