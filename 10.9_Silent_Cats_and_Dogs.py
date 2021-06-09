def check_file(filename):
    try:
        with open(filename) as f:
            data = f.read()
    except FileNotFoundError:
        pass
    else:
        data = data.split("\n")
        print(f"List name of {filename} : ")
        for i in data:
            print("- " + i.title())


def main():
    files = ['cats.txt', 'dogs.txt']
    for i in files:
        check_file(i)


if __name__ == '__main__':
    main()
