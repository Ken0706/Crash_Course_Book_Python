def storage():
	global person1, person2, person3
	person1 = {"first_name" : "nguyen", "last_name" : "ken", "city" : "hcm"}
	"""	print(people["last_name"].title() + " " + people["first_name"].title()
	+ " born at " + people["city"].upper() + " city.")"""
	person2 = {"first_name" : "tran", "last_name" : "dinh xu", "city" : "Ha Noi"}
	person3 = {"first_name" :  "Hai", "last_name" : "pro", "city" : "france"}
	people = [person1, person2, person3]
	for i, p in enumerate(people) : # i for index, p for person
		print(str(i + 1)+ "|" + p["last_name"].title() + " " + p["first_name"].title() + " born at " + p["city"])

def main():
	storage()

if __name__ == '__main__':
	main()
