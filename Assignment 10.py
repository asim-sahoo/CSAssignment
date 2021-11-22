stack = []
def PUSH():
    n = int(input("Enter the no. of records: "))
    
    for i in range(n):
        Emp_IDno = input("Enter the Identity no.: ")
        Emp_Name = input("Enter the Employee's Name: ")
        Emp_Desig = input("Enter the Designation: ")
        Emp_Salary = int(input("Enter the Salary: "))
        Emp_NetPay = int(input("Enter the NetPay: "))
        print()
        x = (Emp_IDno, Emp_Name, Emp_Desig, Emp_Salary, Emp_NetPay)
        stack.append(x)

def POP():
    if stack == []:
        print("Stack is Empty!")
    else:
        print("Deleted Record is: ", stack.pop())

def DISPLAY():
    if stack == []:
        print("Stack is Empty!")
    else:
        l = len(stack)
        while l > 0:
            print(stack[l-1])
            l = l-1

def main():
    cont = "y"
    while cont == 'y' or cont == "Y":
        print("1. PUSH")
        print("2. POP")
        print("3. DISPLAY")
        print()
        ch = int(input("Enter your option: "))
        print()
        if ch == 1:
            PUSH()
        elif ch == 2:
            POP()
        elif ch == 3:
            DISPLAY()
        print()
        cont = input("Do you want to continue(Y/N)? : ")
        print()
        if cont == 'y' or cont == 'Y':
            continue
        else:
            break
main()