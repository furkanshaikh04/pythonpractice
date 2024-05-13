X = int(input("Enter your first number:"))
Y = int(input("Enter your second number:"))
C= X+Y
D= X-Y
E= X*Y
F= X/Y
Select = int(input("""Select any one operation from below:
1.Addition
2.Substraction
3.Multiplication
4.Division\n"""))
match Select:
    case 1:
        print("Addition of two nos. is",C)
    case 2:
        print("Substraction of two nos. is",D)
    case 3:
        print("Multiplication of two nos. is",E)
    case 4:
        print("Division of two nos. is",F)
    case _:
        print("Invalid Option")