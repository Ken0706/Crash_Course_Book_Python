def quantity():
    people = int(input("How many people in their dinner group ? : "))
    print("Their table is ready" if people < 8 else "They'll have to wait\
 for a table")
def main():
    quantity()

if __name__ == '__main__': 
    main()