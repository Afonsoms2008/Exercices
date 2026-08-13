def numeros(num):
    for n in range(num + 1):
        print(f"{n}  "*n)
num1 = int(input("Introduz um número: "))
numeros(num1)