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
if(Select==1):
    print("The Addition of two nos. is:",C)
elif(Select==2):
    print("The Substraction of two nos. is:",D)
elif(Select==3):
    print("The Multiplication of two nos. is:",E)
elif(Select==4):
    print("The Division of two nos. is:",F)
else:
    print('Invalid input')