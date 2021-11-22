import pickle

header = "{:<15} {:<15} {:<15} {:<15}".format("Player No.", "Player Name", "Total Score", "Amount")

def P_INSERT():

    pl = []
    f = open('PSPORTS.dat', 'wb')
    n = int(input("Enter the no. of records: "))
    print()

    for i in range(n):
        P_No = int(input("Enter the player no.: "))
        P_Name = input("Enter the Player Name: ")
        Total_Score = int(input("Enter the Total Score: "))
        P_Amount = int(input("Enter the Amount: "))
        print()
        x = [P_No, P_Name, Total_Score, P_Amount]
        pl.append(x)
        pickle.dump(pl, f)

    f.close()

def P_DISP():

    pl = []
    f = open('PSPORTS.dat', 'rb')
    while True:
        try:
            pl = pickle.load(f)
        except EOFError:
            break
    print(header)
    for j in range(len(pl)):
        print("{:<15} {:<15} {:<15} {:<15}".format(pl[j][0], pl[j][1], pl[j][2], pl[j][3]))
        
    f.close()

def P_SEARCH():
    pl = []
    f = open('PSPORTS.dat', 'rb')
    p_no = int(input("Enter the Player No. to search: "))
    found = False
    while True:
        try:
            pl = pickle.load(f)
        except EOFError:
            break
    print()
    print("Original Records....")
    P_DISP()
    print()
    print("Searched Record...")
    for i in pl:
        if i[0] == p_no:
            print(header)
            print("{:<15} {:<15} {:<15} {:<15}".format(i[0], i[1], i[2], i[3]))
            found = True
            break
    if found == False:
        print("Record not found!")
    f.close()

def P_UPDATE():

    pl = []
    f = open('PSPORTS.dat', 'rb')
    print()
    print("Original Records....")
    P_DISP()
    print()
    while True:
        try:
            pl = pickle.load(f)
        except EOFError:
            break
    for i in pl:
        if i[2] >= 100:
            i[3] = i[3] + 50000
    f.close()
    r = open('PSPORTS.dat', 'wb')
    print()
    print("Updated Records...")
    print(header)
    for j in range(len(pl)):
        print("{:<15} {:<15} {:<15} {:<15}".format(pl[j][0], pl[j][1], pl[j][2], pl[j][3]))
    pickle.dump(pl, r)

    f.close()

def P_DELETE():
    pl = []
    f = open('PSPORTS.dat', 'rb')
    print()
    print("Original Records....")
    P_DISP()
    print()
    print("Deleted Record...")
    while True:
        try:
            pl = pickle.load(f)
        except EOFError:
            break
    for i in pl:
        if i[2] < 25:
            print(header)
            print("{:<15} {:<15} {:<15} {:<15}".format(i[0], i[1], i[2], i[3]))
            pl.remove(i)
            break
    else:
        print("No player has Total Score less than 25.")

    f.close()
    r = open('PSPORTS.dat', 'wb')
    print()
    print("Updated Records...")
    print(header)
    for j in range(len(pl)):
        print("{:<15} {:<15} {:<15} {:<15}".format(pl[j][0], pl[j][1], pl[j][2], pl[j][3]))
    pickle.dump(pl, r)

    f.close()

def main():
    cont = "y"
    while cont == 'y' or cont == "Y":
        print()
        print("1. Add Player Records.")
        print("2. Display Players Records.")
        print("3. Search Player's Record.")
        print("4. Update Player's record whose Total score is greater than \n   or equal to 100 by increasing the amount by 50,000.")
        print("5. Delete the records of the players whose score is less than 25")
        print()
        ch = int(input("Enter your option: "))
        print()
        if ch == 1:
            P_INSERT()
        elif ch == 2:
            P_DISP()
        elif ch == 3:
            P_SEARCH()
        elif ch == 4:
            P_UPDATE()
        elif ch == 5:
            P_DELETE()
        print()
        cont = input("Do you want to continue(Y/N)? : ")
        print()
        if cont == 'y' or cont == 'Y':
            continue
        else:
            break

main()


