def car():
    rental_car = input("Enter kind of car you want to rent : ").lower()
    print(f"Let me see if  I can find  you a {rental_car.title()}")
def main():
    car()

if __name__ == '__main__':
    main()