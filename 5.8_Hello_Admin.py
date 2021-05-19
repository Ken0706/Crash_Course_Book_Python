def check_number_user():
	global n
	while True:
		try:
			n = int(input("How many user you add : "))
			if n <= 1 :
				print("Try again...")
			else:
				break
		except ValueError:
			print("Try again...")
def user_list(n):
	global users
	users = ["admin"]
	for user in range(n):
		users.append(input("Enter user name : ").lower())
def pop_up(users):
	check = input("Who are you ? : ").lower()
	if check == "admin":
		print("Hello admin, would you like to see a status report ?")
		print("Your user here : ")
		for user in users :
			print(f"- {user.title()}")
	else:
		print(f"Hello {check}, thank you for logging in again.")
def main():
	check_number_user()
	user_list(n)
	pop_up(users)
if __name__ == '__main__':
	main()