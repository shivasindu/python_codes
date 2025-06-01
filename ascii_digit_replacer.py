str = "a3b5c7"
new = ""
series = 97  # ASCII value of 'a'
for i in range(len(str)):
    if str[i].isdigit():
        ascii_value = series + int(str[i])
        new += chr(ascii_value)
        series += 1 #to increment series
    else:
        new += str[i]
print(new)
