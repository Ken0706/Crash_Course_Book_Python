class Restaurant():
    def __init__(self, restaurant_name, cuisine_type):
        self.restaurant_name = restaurant_name
        self.cuisine_type = cuisine_type

    def describe_restaurant(self):
        print(f"Name of restaurant : {self.restaurant_name}")
        print(f"Type of cuisine type : {self.cuisine_type}")

    def open_restaurant(self):
        print("Restaurant open at 8 A.M !!!")


def main():
    restaurant = Restaurant("Royal", "Vegan cuisine")
    restaurant.describe_restaurant()
    restaurant.open_restaurant()


if __name__ == "__main__":
    main()
