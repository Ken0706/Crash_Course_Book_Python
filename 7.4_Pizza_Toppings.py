def toppings():
    while True:
        topping = input("Enter topping (enter 'quit' when you done): ")
        if topping == 'quit' : break
        else : print(f"Add {topping} success !!!")


def main():
    toppings()

if __name__ == '__main__': 
    main()

        
