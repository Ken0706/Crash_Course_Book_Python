def cal_number():
    while True:
        try:
            a = int(input("Enter a : "))
            b = int(input("Enter b : "))
            print(f"Sum : {a + b}")
        except (TypeError, ValueError):
            print("Sorry a or b is not a number.")
            q = input("Continue ('yes' or 'no'): ")
            if q == 'no':
                break
        else:
            q = input("Continue ('yes' or 'no') : ")
            if q == 'no':
                break


def main():
    cal_number()


if __name__ == '__main__':
    main()
