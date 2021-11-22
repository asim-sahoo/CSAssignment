q = []
def InQ():
    n = int(input("Enter the no. of records: "))
    
    for i in range(n):
        Flight_Number = input("Enter the Flight No.: ")
        Flight_Name = input("Enter the Flight Name: ")
        Flight_Type = input("Enter the Flight Type(Domestic/International): ")
        Distance_Travelled = int(input("Total Distance Travelled: "))
        Fare = int(input("Total Fare: "))
        print()
        x = (Flight_Number, Flight_Name, Flight_Type, Distance_Travelled, Fare)
        q.append(x)

def DeIQ():
    if q == []:
        print("Stack is Empty!")
    else:
        print("Deleted Record is: ", q.pop(0))

def Display():
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
            InQ()
        elif ch == 2:
            DeIQ()
        elif ch == 3:
            Display()
        print()
        cont = input("Do you want to continue(Y/N)? : ")
        print()
        if cont == 'y' or cont == 'Y':
            continue
        else:
            break
main()