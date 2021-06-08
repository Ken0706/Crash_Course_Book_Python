#import class Restaurant from Restaurant module
from Restaurant_module import Restaurant


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
