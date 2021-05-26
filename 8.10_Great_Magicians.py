def show_magicians(names):
    for name in names :
        print("Welcome the Great " + name + "!!!")

def main():
    names = ["Johnathan Szeles", "Christopher Sarantakos", "Theodore John Squires"]
    show_magicians(names)
if __name__ == '__main__':
    main()