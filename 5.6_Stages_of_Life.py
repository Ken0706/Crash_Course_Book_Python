def check_input():
	global age
	while True:
		try:
			age = int(input("Enter age : "))
			if age < 0 :
				print("Try again...")
			else :
				break
		except ValueError:
			print("Try again...")
def result(age):
	if age >= 65:
		return "elder"
	elif age < 65 and age >= 20:
		return "adult"
	elif age < 20 and age >= 13:
		return "teenager"
	elif age < 13 and age >= 4:
		return "kid"
	elif age < 4 and age >= 2 :
		return "toddler"
	else:
		return "baby"
def fix_font(age):
	lst = ["u", "e", "o", "a", "i"]
	a = result(age)[:1]
	if a in lst:
		return f"The person is an {result(age)}"
	else:
		return f"The person is a {result(age)}"
def main():
	check_input()
	print(fix_font(age))
if __name__ == "__main__":
	main()