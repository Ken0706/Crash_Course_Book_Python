class Restaurant():
    def __init__(self, restaurant_name, cuisine_type):
        self.restaurant_name = restaurant_name
        self.cuisine_type = cuisine_type

    def describe_restaurant(self):
        print(f"Name of restaurant : {self.restaurant_name.title()}")
        print(f"Type of cuisine type : {self.cuisine_type.title()}")

    def open_restaurant(self):
        print("Restaurant open at 8 A.M !!!")


class IceCreamStand(Restaurant):
    def __init__(self, restaurant_name, cuisine_type):
        super().__init__(restaurant_name, cuisine_type)
        self.flavors = ["strawberry", "coconut", "chocolate"]

    def describe_flavors(self):
        print("List of favor : ")
        for i in self.flavors:
            print(f"- {i.title()}")


def main():
    icecream = IceCreamStand("royal", "vegan cuisine")
    icecream.describe_restaurant()
    icecream.open_restaurant()
    icecream.describe_flavors()


if __name__ == "__main__":
    main()
