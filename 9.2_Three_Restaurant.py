class Restaurant():
    def __init__(self, restaurant_name, cuisine_type):
        self.restaurant_name = restaurant_name
        self.cuisine_type = cuisine_type

    def describe_restaurant(self):
        print(f"Name of restaurant : {self.restaurant_name.title()}")
        print(f"Type of cuisine type : {self.cuisine_type.title()}")

    def open_restaurant(self):
        print("Restaurant open at 8 A.M !!!")


def main():
    restaurant = Restaurant("Royal", "Vegan cuisine")
    restaurant.describe_restaurant()
    restaurant.open_restaurant()
    print("-" * 15)
    res2 = Restaurant("shri", "european")
    res2.describe_restaurant()
    res2.open_restaurant()
    print("-" * 15)
    res3 = Restaurant("skewers", "mediterranean")
    res3.describe_restaurant()
    res3.open_restaurant()


if __name__ == "__main__":
    main()
