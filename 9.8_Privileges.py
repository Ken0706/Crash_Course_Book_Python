class User():
    def __init__(self,  first_name, last_name=''):
        self.first_name = first_name
        self.last_name = last_name

    def describe_user(self):
        print(f"Name user : {self.last_name.title()} {self.first_name.title()}")

    def greet_user(self):
        print(f"Welcome {self.first_name.title()}")


class Admin(User):
    def __init__(self, first_name, last_name=''):
        super().__init__(first_name, last_name)
        self.privileges = Privileges()


class Privileges():
    def __init__(self, privileges=['can add post', 'can delete post', 'can ban user']):
        self.privileges = privileges

    def show_privileges(self):
        print("Privilege of you : ")
        for i in self.privileges:
            print("- " + i)


def main():
    user1 = User("ken", "nguyen")
    admin2 = Admin("admin")
    user1.describe_user()
    user1.greet_user()
    print("-" * 20)
    admin2.describe_user()
    admin2.greet_user()
    admin2.privileges.show_privileges()


if __name__ == '__main__':
    main()
