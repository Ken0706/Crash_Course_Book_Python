def dict_person():
	global people
	people = {"first_name" : "nguyen", "last_name" : "ken", "city" : "hcm"}
	print(people["last_name"].title() + " " + people["first_name"].title()
+ " born at " + people["city"].upper() + " city.")

def main():
	dict_person()
if __name__ == '__main__':
	main()
