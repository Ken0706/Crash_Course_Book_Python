import time
def show_magicians(names, names_great):
    while len(names) != 0:
        current_name = names.pop()
        print("Current name add 'Great' : " + current_name)
        names_great.append("the Great " + current_name)
        print("...")
        time.sleep(1.5) # wait 1.5 seconds

def show_names_great(names_great):
    print("--- DONE ---")
    for name in names_great :
        print("Welcome " + name + "!!!")

def main():
    names = ["Johnathan Szeles", "Christopher Sarantakos", "Theodore John Squires"]
    names_great = []
    show_magicians(names, names_great)
    show_names_great(names_great)
if __name__ == '__main__':
    main()