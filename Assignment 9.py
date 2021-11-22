import csv
h = ["S_AdNo", "S_Name", "S_CLSec", "S_RollNo", "S_TotalMarks", "S_PerMarks"]

def S_DISP(a, b):
    with open(a, b) as f:
        rd = csv.reader(f)
        c = []
        for r in rd:
            c.append(r)

        for j in range(len(c)):

            print("{:<20} {:<15} {:<15} {:<15} {:<15} {:<15}".format(c[j][0], c[j][1], c[j][2], c[j][3], c[j][4], c[j][5]))


def S_APPEND():
    print("Before Appending...")
    S_DISP('Students.csv', 'r')
    cn = []
    n = int(input("Enter the no. of records: "))
    for i in range(n):
        S_AdNo = input("Enter the Admission No.: ")
        S_Name = input("Enter the Student's Name: ")
        S_CLSec = input("Enter the Class and Sec: ")
        S_RollNo = int(input("Enter the Roll No.: "))
        S_TotalMarks = int(input("Enter the Total Marks(Out of 500): "))
        S_PerMarks = (S_TotalMarks/500)*100
        print()
        x = [S_AdNo, S_Name, S_CLSec, S_RollNo, S_TotalMarks, int(S_PerMarks)]
        cn.append(x)
    with open('Students.csv', 'a', newline='') as f:
        w = csv.writer(f, delimiter=',')
        for i in cn:
            w.writerow(i)
    print("After Appending...")
    S_DISP('Students.csv', 'r')


def S_SEARCH():
    print("Original Records...")
    S_DISP('Students.csv', 'r')
    with open('Students.csv', 'r') as f:
        s = input("Enter the Admission No. to search: ")
        rd = csv.reader(f)
        found = False
        print()
        print("Searched Records...")
        for r in rd:
            if r[0] == s:
                print("{:<20} {:<15} {:<15} {:<15} {:<15} {:<15}".format("S_AdNo", "S_Name", "S_CLSec", "S_RollNo", "S_TotalMarks", "S_PerMarks"))
                print("{:<20} {:<15} {:<15} {:<15} {:<15} {:<15}".format(r[0], r[1], r[2], r[3], r[4], r[5]))
                found = True
                break
        if found == False:
            print("Record not found!")


def S_UPDATE():
    print("Original Records...")
    S_DISP('Students.csv', 'r')
    f = open('Students.csv', 'r', newline='')
    rd = csv.reader(f)
    next(f)
    data = []
    for rec in rd:
        data.append(rec)
    for i in range(len(data)):
        data[i][4] = int(data[i][4])
    for r in data:

        if r[4] >= 155 and r[4] < 165:
            r[4] = r[4] + 10
    f.close()
    f1 = open('Students.csv', 'w', newline='')
    rd2 = csv.writer(f1)
    rd2.writerow(h)
    for i in data:
        rd2.writerow(i)
    print()
    print("After Updating...")
    f1.close()
    S_DISP('Students.csv', 'r')



def S_COPY():
    with open('Students.csv', 'r') as f:
        rd = csv.reader(f)
        c = []
        s_top = []
        s_back = []
        next(f)
        for r in rd:
            c.append(r)
        for i in c:
            if int(i[5]) >= 80:
                s_top.append(i)
            if int(i[5]) < 33:
                s_back.append(i)
        f.close()
        print("Students.csv Records...")
        S_DISP('Students.csv', 'r')
    with open('StudentTop.csv', 'w', newline='') as f1:
        rd1 = csv.writer(f1)
        rd1.writerow(h)
        for i in s_top:
            rd1.writerow(i)
        f1.close()
        print("StudentTop.csv Records...")
        S_DISP('StudentTop.csv', 'r')
    with open('StudentBack.csv', 'w', newline='') as f2:
        rd3 = csv.writer(f2)
        rd3.writerow(h)
        for i in s_back:
            rd3.writerow(i)
        f2.close()
        print("StudentBack.csv Records...")
        S_DISP('StudentBack.csv', 'r')


def main():
    cont = "y"
    while cont == 'y' or cont == "Y":
        print()
        print("1. Display Student's Records.")
        print("2. Add more Records.")
        print("3. Search Student's Record by Admission No.")
        print("4. Update the student's record whose Total Marks is >= 155 and <165 by increasing 10 marks")
        print("5. Copy the records having S_PerMarks >=80 from 'Students.CSV' to 'StudentTop.csv' and also copy the records \n   having S_PerMarks < 33 from “Students.csv” to “StudentBack.csv” and display the records")
        print()
        ch = int(input("Enter your option: "))
        print()
        if ch == 1:
            S_DISP('Students.csv', 'r')
        elif ch == 2:
            S_APPEND()
        elif ch == 3:
            S_SEARCH()
        elif ch == 4:
            S_UPDATE()
        elif ch == 5:
            S_COPY()
        print()
        cont = input("Do you want to continue(Y/N)? : ")
        print()
        if cont == 'y' or cont == 'Y':
            continue
        else:
            break


main()
