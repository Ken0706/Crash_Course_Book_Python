def poll():
    with open('reason.txt', 'a') as f:
        while True:
            reason = input("Why you like programming ('q' to quit) : ")
            if reason == 'q':
                break
            else:
                f.write(reason.capitalize().strip() + "\n")
                print("--" * 25)


def main():
    poll()


if __name__ == '__main__':
    main()
