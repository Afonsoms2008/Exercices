def reverse(number):
    number = str(number)
    number_reversed = number[::-1]
    print(f"The reverse of {number} is {number_reversed}")
num = int(input("Insert the desired number: "))
reverse(num)