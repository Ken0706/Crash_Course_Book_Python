def dict_language():
	lang = {
		"ken" : "python",
		"nigh" : "c"
	}
	print("User current : ")
	for k, v in lang.items():
		print(f"- {k.title()} : {v.title()}")
	while True:
		n = int(input("Enter the number of people you want to add : "))
		try:
			if n == 0 :
				print("You don't add anyone!!!")
				break
			elif n < 0 :
				print("Try again...")
			else :
				for i in range(n):
					new_name = input("Enter name : ").lower()
					new_lang = input("Enter lang : ").lower()
					lang[new_name] = new_lang
				print("User current (updated) :")
				for k, v in lang.items():
					print(f"- {k.title()} : {v.title()}")
				break
		except ValueError:
			print("Try again...")

def main():
	dict_language()
if __name__ == '__main__':
	main()