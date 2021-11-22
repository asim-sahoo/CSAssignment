q = []
def ENQUEUE():
    n = int(input("Enter the no. of records: "))
    
    for i in range(n):
        Stu_Rollno = input("Enter the Students Roll No.: ")
        Stu_Name = input("Enter the Student's Name: ")
        Stu_Class = input("Enter the Student's class: ")
        Stu_TM = int(input("Enter the Total Marks: "))
        Stu_PM = (Stu_TM/500)*100
        print()
        x = (Stu_Rollno, Stu_Name, Stu_Class, Stu_TM, Stu_PM)
        q.append(x)

def DEQUEUE():
    if q == []:
        print("Stack is Empty!")
    else:
        print("Deleted Record is: ", q.pop(0))

def DISPLAY():
    if q == []:
        print("Queue is Empty!")
    else:
        l = len(q)
        for i in range(0, l):
            print(q[i])

def main():
    cont = "y"
    while cont == 'y' or cont == "Y":
        print("1. ENQUEUE")
        print("2. DEQUEUE")
        print("3. DISPLAY")
        print()
        ch = int(input("Enter your option: "))
        print()
        if ch == 1:
            ENQUEUE()
        elif ch == 2:
            DEQUEUE()
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