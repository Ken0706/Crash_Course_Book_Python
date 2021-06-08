# store name in guest.txt


def store_name_txt():
    name = str(input("What is your name : "))
    with open('guest.txt', 'w') as f:
        f.write(name.title())


def main():
    store_name_txt()


if __name__ == '__main__':
    main()
