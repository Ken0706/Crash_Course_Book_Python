#module for 8.16
def orders(*toppings) :
    print("Topping(s) you want : ")
    for topping in toppings:
        print(f"+ {topping.title()}")