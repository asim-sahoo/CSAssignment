stack = []
def PUSH():
    n = int(input("Enter the no. of records: "))
    
    for i in range(n):
        Book_Id = input("Enter the Book Id no.: ")
        Book_Name  = input("Enter the Book Name: ")
        Book_Auth_Name = input("Enter the Author's Name: ")
        Book_Pub_Name = input("Enter the Publisher's Name: ")
        Book_Cost = int(input("Enter Cost of the Book: "))
        print()
        x = (Book_Id, Book_Name, Book_Auth_Name, Book_Pub_Name, Book_Cost)
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