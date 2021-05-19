import time
def check_number_user():
	global n
	while True:
		try:
			n = int(input("How many user you add : "))
			break
		except ValueError:
			print("Try again...")
def user_list(n):
	global current_users
	admins = ["admin"]
	current_users = ["ken", "nah", "bi", "black", "dragon"]
	new_users = []
	for new_user in range(n):
		while True:
			check_name = input("Enter user name : ").lower()
			if check_name in current_users:
				print("Usersname has been already been used.")
				print("Try again...")
			else:
				new_users.append(check_name)
				break

def pop_up(current_users):
	check = input("Who are you ? : ").lower()
	if check == "admin":
		print("Hello admin, would you like to see a status report ?")
		print("Your user here : ")
		for current_user in current_users :
			print(f"- {current_user.title()}")
		print(f"{check.title()} delete all user...")
		time.sleep(2)
		current_users.clear()
		print("Done.")
		print("We need to find some users!")
	else:
		print(f"Hello {check.title()}, thank you for logging in again.")
def main():
	check_number_user()
	user_list(n)
	pop_up(current_users)
if __name__ == '__main__':
	main()