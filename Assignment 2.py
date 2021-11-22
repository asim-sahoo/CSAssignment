def ARMSTRONG(n):
    n1 = n
    r = 0

    while n > 0:
        d = n % 10
        r = r + (d ** 3)
        n = int(n / 10)

    print("The result is: ", r)

    if r == n1:
        print("It is a Armstrong Number")
    else:
        print("It is not a Armstrong Number")


def PALIN(p):
    p = p.upper()
    if p == p[::-1]:
        print("It is a palindrome.")
    else:
        print("It is not palindrome.")


def main():
    cont = "y"
    while cont == 'y' or cont == "Y":
        print("1. Find whether the number is armstrong or not.")
        print("2. Find whether the number is palindrome or not.")
        print()
        ch = int(input("Enter your option: "))
        print()
        if ch == 1:
            x = int(input("Enter a number: "))
            ARMSTRONG(x)
        elif ch == 2:
            x1 = input("Enter a string: ")
            PALIN(x1)
        print()
        cont = input("Do you want to continue(Y/N)? : ")
        print()
        if cont == 'y' or cont == 'Y':
            continue
        else:
            break


main()