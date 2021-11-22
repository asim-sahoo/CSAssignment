import pickle

header = "{:<15} {:<15} {:<15} {:<15} {:<15}".format("Consumer No.", "Consumer Name", "Area Code", "Phone No.", "Phone Bill(Per Month)")

def C_INSERT(a, b):

    cn = []
    f = open(a, b)
    n = int(input("Enter the no. of records: "))
    print()
    while True:
        try:
            cn = pickle.load(f)
        except EOFError:
            break
    for i in range(n):
        C_No = int(input("Enter the Consumer no.: "))
        C_Name = input("Enter the Consumer Name: ")
        C_AreaCode = (input("Enter the Area Code: "))
        C_Phone_No = int(input("Enter the Phone No.: "))
        C_Bill = int(input("Enter the Phone Bill per Month: "))
        print()
        x = [C_No, C_Name, C_AreaCode, C_Phone_No, C_Bill]
        cn.append(x)
    pickle.dump(cn, f)
    print("Records Added Successfully!")
    f.close()

def C_DISP(a, b):
    cn = []
    f = open(a, b)

    while True:
        try:
            cn = pickle.load(f)
        except EOFError:
            break
    print(header)
    for j in range(len(cn)):
        print("{:<15} {:<15} {:<15} {:<15} {:<15}".format(cn[j][0], cn[j][1], cn[j][2], cn[j][3], cn[j][4]))
        
    f.close()

def C_APPEND():
    print("Before Adding Records...")
    C_DISP('TELEPHONE.dat', 'rb')
    print()
    C_INSERT('TELEPHONE.dat', 'rb+')
    print()
    print("After Adding Records...")
    C_DISP('TELEPHONE.dat', 'rb')

def C_COPY():
    cn = []
    rec = []
    f = open('TELEPHONE.dat', 'rb')
    while True:
        try:
            cn = pickle.load(f)
        except EOFError:
            break
    for i in cn:
        if i[2] == '03222':
            rec.append(i)
    f.close()
    f1 = open('TELEBACK.dat', 'wb')
    pickle.dump(rec, f1)
    f1.close()
    print("TELEPHONE file records...")
    C_DISP('TELEPHONE.dat', 'rb')
    print()
    print("TELEBACK file records...")
    C_DISP('TELEBACK.dat', 'rb')
    

def C_UPDATE():
    cn = []
    f = open('TELEPHONE.dat', 'rb')
    print()
    print("Original Records....")
    C_DISP('TELEPHONE.dat', 'rb')
    print()
    while True:
        try:
            cn = pickle.load(f)
        except EOFError:
            break
    for i in cn:
        if i[4] >= 2000:
            i[4] = i[4] + 0.05*i[4]
    f.close()
    r = open('TELEPHONE.dat', 'wb')
    print()
    print("Updated Records...")
    print(header)
    for j in range(len(cn)):
        print("{:<15} {:<15} {:<15} {:<15} {:<15}".format(cn[j][0], cn[j][1], cn[j][2], cn[j][3], cn[j][4]))
    pickle.dump(cn, r)

    f.close()

def main():
    cont = "y"
    while cont == 'y' or cont == "Y":
        print()
        print("1. Insert Consumer's Record.")
        print("2. Display Consumer's Records.")
        print("3. Add More Records in the File.")
        print("4. Copy Records to a new file whose Area Code is '03222'.")
        print("5. Add extra 5 percent charge whose Bill is greater than or equal to 2000")
        print()
        ch = int(input("Enter your option: "))
        print()
        if ch == 1:
            C_INSERT('TELEPHONE.dat', 'wb+')
        elif ch == 2:
            C_DISP('TELEPHONE.dat', 'rb')
        elif ch == 3:
            C_APPEND()
        elif ch == 4:
            C_COPY()
        elif ch == 5:
            C_UPDATE()
        print()
        cont = input("Do you want to continue(Y/N)? : ")
        print()
        if cont == 'y' or cont == 'Y':
            continue
        else:
            break

main()