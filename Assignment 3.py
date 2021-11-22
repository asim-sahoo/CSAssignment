def FACT_SERIES(a, n):

    fact = 1
    s = 1
    print("The series is:")
    print(1, end=" ")
    for i in range(1, n):
        print("+", end=" ")
        print(a, "^", i+1, "/", i, "!", end=" ", sep="")
    for j in range(1, n):
        fact = fact * j
        s = s + ((a**(j+1))/fact)
    print()
    print("Sum of the series:", round(s, 2))


def NEW_STR(str):

    print("Original String: ", str)
    spl = str.title()
    print("Modified String: ", spl)
    print()


def main():
    cont = "y"
    while cont == 'y' or cont == "Y":
        print()
        print("1. Display the sum and equation of the following series : \n   S = 1 + a^2/1! + a^3/2! + a^4/3! + ....... to n")
        print("2. Capitalize first letter of each word of the string.")
        print()
        ch = int(input("Enter your option: "))
        print()
        if ch == 1:
            x = int(input("Enter the value of a: "))
            x1 = int(input("Enter the limit: "))
            print()
            FACT_SERIES(x, x1)
        elif ch == 2:
            x2 = input("Enter a string: ")
            print()
            NEW_STR(x2)
        print()
        cont = input("Do you want to continue(Y/N)? : ")
        print()
        if cont == 'y' or cont == 'Y':
            continue
        else:
            break


main()