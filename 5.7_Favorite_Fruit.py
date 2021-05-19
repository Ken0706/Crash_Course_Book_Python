def check_quatity():
	global n
	while True:
		try:
			n = int(input("Enter number type of fruit : "))
			if n <= 0 :
				print("Try again...")
			else:
				break
		except ValueError:
			print("Try again...")
def in_out_list(n):
	global fruits
	fruits = []
	for i in range(n):
		fruits.append(input("Enter fruit name : ").lower())
	print("List fruits : ")
	for fruit in fruits:
		print(f"- {fruit.title()}")
def check_user_in(fruits):
	name = input("Enter to find fruit : ").lower()
	if name in fruits:
		print(f"You really like {name.title()}")
	else:
		print(f"Hmm... i think you dont like {name.title()}")
def main():
	check_quatity()
	in_out_list(n)
	check_user_in(fruits)

if __name__ == '__main__':
	main()