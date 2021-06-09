def find_word(filename):
    try:
        with open(filename) as f:
            lines = f.read()
    except FileNotFoundError:
        print(f"File {filename} does not exits.")
    else:
        tmp = lines.lower().count('the')
        print("Count 'the' : " + str(tmp))


def main():
    filename = 'common_words.txt'
    find_word(filename)


if __name__ == '__main__':
    main()
