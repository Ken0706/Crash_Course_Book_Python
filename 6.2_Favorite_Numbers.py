def dict_numbers():
	favorite_numbers = {"ken" : 5, "nah" : 3, "vip" : 2, "dragon" : 7, "spring" : 1}
	for i, k in enumerate(favorite_numbers):
		print("- " + str(k).title() + " : " + str(favorite_numbers[k]))
	n = int(input("Enter quatity name you want add : "))
	for i in range(n):
		new_name = input("Enter name : ").lower()
		new_number = int(input("Enter number : "))
		favorite_numbers[new_name] = new_number
	print("After add")
	for i, k in enumerate(favorite_numbers):
		print("- " + str(k).title() + " : " + str(favorite_numbers[k]))
def main():
	dict_numbers()
if __name__ == '__main__':
	main()