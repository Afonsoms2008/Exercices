def numeros(num):
    for linha in range(1, num + 1):
        for numero in range(1, linha + 1):
            print(numero, end=" ")
        print()

num1 = int(input("Enter a number: "))
numeros(num1)