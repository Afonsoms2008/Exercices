#I am using a brazilian exercise list CPF is like their ID number
cpf = input("Introduce your CPF number in the xxx.xxx.xxx-xx format: ")
if cpf[3] != "." or cpf[7] != "." or cpf[11] !="-":
    print("Invalid CPF!")
elif cpf[0:3].isdigit() == False or cpf[4:7].isdigit() == False or cpf[8:11].isdigit() == False or cpf[12:14].isdigit() == False:
    print("Invalid CPF!")
else:
    print("Valid CPF!")