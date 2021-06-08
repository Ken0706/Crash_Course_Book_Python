# read file learning_python.txt


def read_file():
    with open('learning_python.txt') as f:
        entire_file = f.read()
        f.seek(0)  # to turn back the page
        lst = f.readlines()
        f.seek(0)
        print("Print by read line by line (use loop) : ")
        for i in f:
            print(i.strip())
    print("-" * 35)
    print("Print by read entire file : ")
    print(entire_file)
    print("-" * 35)
    print("Print by read file and storing lines in list")
    for i in lst:
        print(i.strip())
    print("-" * 35)


def main():
    read_file()


if __name__ == '__main__':
    main()
