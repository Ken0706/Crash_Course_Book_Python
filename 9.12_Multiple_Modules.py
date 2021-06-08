#use class from User_module and Admin_Pri_module
from User_module import User
from Admin_Pri_module import Admin, Privileges


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
