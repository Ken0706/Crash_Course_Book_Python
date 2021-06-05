class Restaurant():
    def __init__(self, restaurant_name, cuisine_type):
        self.restaurant_name = restaurant_name
        self.cuisine_type = cuisine_type
        self.number_served = 0

    def describe_restaurant(self):
        print(f"Name of restaurant : {self.restaurant_name.title()}")
        print(f"Type of cuisine type : {self.cuisine_type.title()}")

    def open_restaurant(self):
        print("Restaurant open at 8 A.M !!!")

    def set_number_served(self, number):
        self.number_served = number

    def increment_number_served(self, increse_num):
        self.number_served += increse_num


def main():
    restaurant = Restaurant("royah", "vegan cuisine")
    restaurant.describe_restaurant()
    print(f"Number of served now : {restaurant.number_served}")
    restaurant.number_served = 1
    print(f"Number served after change : {restaurant.number_served}")
    restaurant.set_number_served(2)
    print(f"Number served after set : {restaurant.number_served}")
    restaurant.increment_number_served(50)
    print(f"Number served after increase : {restaurant.number_served}")


if __name__ == '__main__':
    main()
