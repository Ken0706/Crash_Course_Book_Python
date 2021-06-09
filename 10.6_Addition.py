def cal_number():
    try:
        a = int(input("Enter a : "))
        b = input("Enter b : ")
        print(f"Sum : {a + b}")
    except (TypeError, ValueError):
        print("Sorry a or b is not a number.")


def main():
    cal_number()


if __name__ == '__main__':
    main()
