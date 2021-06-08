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