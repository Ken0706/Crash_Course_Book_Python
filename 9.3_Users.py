class User():
    def __init__(self,  first_name, last_name):
        self.first_name = first_name
        self.last_name = last_name

    def describe_user(self):
        print(f"Name user : {self.last_name.title()} {self.first_name.title()}")

    def greet_user(self):
        print(f"Welcome {self.first_name.title()}")


def main():
    user1 = User("ken", "nguyen")
    user1.describe_user()
    user1.greet_user()


if __name__ == '__main__':
    main()
