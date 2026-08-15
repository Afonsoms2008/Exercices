def frame(row,column):
    while True:
        if  1>row or row>20 or 1>column or column>20:
            print("Invalid Values please insert again")
        else:
            print(" +", "-"*(column -2), "+")
            print(f"\n |{" "*(column)} |"*(row) ,"\n +","-"*(column -2), "+")
            break

rows = int(input("Insert how many rows you wish your portrait to have: "))
columns = int(input("Insert how many columns you wish your portrait to have: "))
frame(rows,columns)
            