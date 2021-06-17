import json


def get_stored_username():
    """Stored username if it available"""
    filename = 'username.json'
    try:
        with open(filename) as f:
            username = json.load(f)
    except FileNotFoundError:
            return None
    else:
        return username


def get_new_username():
    username = input("Enter your name : ")
    filename = 'username.json'
    with open(filename, 'w') as f:
        json.dump(username, f)
    return username


def greet_user():
    username = get_stored_username()
    if username:
        check_name = input("Who are you ? ")
        if check_name == username:
            print(f"Welcome back, {username}!")
        else:
            print("Sorry, name does not exits... You can create new!!!")
            get_new_username()
    else:
        username = get_new_username()
        print(f"We'll remember you when you come back, {username}!")


def main():
    greet_user()


if __name__ == '__main__':
    main()
