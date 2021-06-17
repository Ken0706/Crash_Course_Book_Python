import json


def favorite_num():
    filename = 'favorite_num.json'
    try:
        with open(filename) as f:
            data = json.load(f)
    except FileNotFoundError:
        with open(filename, 'w') as f:
            number = int(input("Your favorite number : "))
            json.dump(number, f)
            print(f"File created...I know your number! It's {number}")
    else:
        print(f"File exits... Your number is {data}")


def main():
    favorite_num()


if __name__ == '__main__':
    main()