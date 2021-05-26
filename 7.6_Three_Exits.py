def toppings():
    people = int(input("Enter number of topping you want add : "))
    i = 0
    while i < people:
        topping = input("Enter topping (enter 'quit' when you done): ")
        if topping == 'quit' : break
        else : print(f"Add {topping} success !!!")
        i += 1


def main():
    toppings()

if __name__ == '__main__': 
    main()

        
