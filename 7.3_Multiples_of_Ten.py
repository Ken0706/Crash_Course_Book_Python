def _():
    number = int(input("Enter number : "))
    print("It " + ("is" if number % 10 == 0 else "isn't") + " a multiple of 10.")
def main():
    _()

if __name__ == '__main__':
    main()