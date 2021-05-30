def orders(*toppings) :
    print("Topping(s) you want : ")
    for topping in toppings:
        print(f"+ {topping.title()}")
def main():
    orders("cheese", "chicken", "paparazi")
    orders("hawaii", "big")

if __name__ == '__main__':
    main()