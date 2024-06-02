#simple calculator with basic arithmetic operation

# take value from user
num1=eval(input("Enter the first number:"))
num2=eval(input("Enter the second number:"))

# given the keyword for operation
print("1.For addition task")
print("2. for subtraction task")
print("3.For multification task")
print("4.For division tasks")
print("5.Exit")

# take choice from user
choice=int(input("Enter your choice :"))

while(1):
    if choice==1:
        print("sum =",num1+num2)
        break
    elif choice==2:
        print("subtraction =",num1-num2)
        break
    elif choice ==3:
        print("multification = ",num1*num2)
        break
    elif choice ==4:
        print("division = ",num1/num2)
        break
    elif choice ==5:
        print("Exit")
        break
    else:
        print("Please enter valid choice")
        break

