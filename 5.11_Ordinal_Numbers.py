def number_list():
	numbers = list(range(1,10))
	for i in numbers:
		if i == 1:
			print("1st") 
			continue
		elif i == 2:
			print("2nd") 
		elif i == 3:
			print("3rd") 
		else:
			print(f"{i}th") 
def main():
	number_list()
if __name__ == '__main__':
	main()
