import json

filename = 'favorite_number.json'

def fav_num():
    number = int(input("Enter your number : "))
    with open(filename, 'w') as f:
        json.dump(number, f)

def get_fav_num():
    fav_num()
    with open(filename) as f:
        data = json.load(f)
    return f"I know your favorite number! It's {data}"


def main():
    print(get_fav_num())


if __name__ == '__main__':
    main()