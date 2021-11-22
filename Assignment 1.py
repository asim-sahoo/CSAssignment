def SHIFT():
    no = int(input("Enter the number of elements: "))
    L = []
    while no > 0:
        k = input("Enter an element: ")
        L.append(k)
        no = no - 1
    print()
    print("This is the original list: ", L)

    length = len(L) - 1
    store = L[length]

    for i in range(length, 0, -1):
        L[i] = L[i-1]

    L[0] = store
    print()
    print('This is the list after shifting: ', L)


def CONV_CAPITAL():
    str = input("Enter the string: ")
    print("Original String: ", str)
    str = str.title()
    spl = str.split()
    n = ''
    for i in spl:
        w1 = i[:-1]
        w2 = i[-1].upper()
        n = n + w1 + w2 + ' '
    print("Modified String: ", n)


def main():
    cont = "y"
    while cont == 'y' or cont == "Y":
        print("1. Shift the elements of a list to the right side position(last element to the first position).")
        print("2. Capitalize first and last letters of each word of a string.")
        print()
        ch = int(input("Enter your option: "))
        print()
        if ch == 1:
            SHIFT()
        elif ch == 2:
            CONV_CAPITAL()
        print()
        cont = input("Do you want to continue(Y/N)? : ")
        print()
        if cont == 'y' or cont == 'Y':
            continue
        else:
            break


main()