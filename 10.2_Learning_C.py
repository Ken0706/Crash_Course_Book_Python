def replace_text():
    with open('learning_python.txt') as f:
        text = f.read()
    text = text.replace('Python', 'C')
    print(text)


def main():
    replace_text()


if __name__ == '__main__':
    main()
