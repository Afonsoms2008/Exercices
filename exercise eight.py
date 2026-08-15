def digit_count(number):
    digits = 0 
    number = str(number)
    for digit in number:
        digits += 1
    print(f"{number} has {digits} digits")
num = int(input("Insert the desired number: "))
digit_count(num)