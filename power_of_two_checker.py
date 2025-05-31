num = int(input("Enter a number: "))
if num > 0:
    while num % 2 == 0:
        num //= 2
    if num == 1:
        print("The number is a power of 2.")
    else:
        print("The number is not a power of 2.")
else:
    print("The number is not a power of 2.")  prgm name suitable
