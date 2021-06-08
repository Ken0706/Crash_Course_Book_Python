def welcome_visiter():
    with open('guest_book.txt', 'a') as f:
        while True:
            name = str(input("Name ('q' to quit): "))
            f.write(name.title() + "\n")
            if name == 'q':
                break
            print(f"Welcome {name.title()}")


def main():
    welcome_visiter()


if __name__ == '__main__':
    main()
