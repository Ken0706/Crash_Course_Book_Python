def dict_numbers():
	favorite_numbers = {"ken" : [5, 4], "nah" : [3, 6], "vip" : [2, 7], "dragon" : [7, 10], "spring" : [1, 9]}
	for name, numbers in favorite_numbers.items():
		print(name.title())
		print("\tNumbers : ", end = '')
		for number in numbers:
			print(f"{number}",end = ' ')
		print("\n")


def main():
	dict_numbers()
if __name__ == '__main__':
	main()