#use class User from User_module
from User_module import User


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