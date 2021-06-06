import time


class User():
    def __init__(self,  first_name, last_name):
        self.first_name = first_name
        self.last_name = last_name
        self.login_attempts = 0

    def describe_user(self):
        print(f"Name user : {self.last_name.title()} {self.first_name.title()}")

    def greet_user(self):
        print(f"\nWelcome {self.first_name.title()}")

    def increment_login_attempts(self):
        self.login_attempts += 1

    def reset_login_attempts(self):
        self.login_attempts = 0

    def get_login_attempts(self):
        return self.login_attempts


def main():
    user1 = User("ken", "nguyen")
    # user1.describe_user()
    # user1.greet_user()
    pwd = 'ken123'
    while True:
        tmp = input("Enter password : ")
        user1.increment_login_attempts()
        print(f"Login attemps : {user1.get_login_attempts()}")
        for i in range(3):
            print('.', end='')
            time.sleep(0.5)
        if tmp != pwd:
            time.sleep(1)
            print("\nTry again")
            print("---" * 20)
        else:
            user1.greet_user()
            break


if __name__ == '__main__':
    main()
