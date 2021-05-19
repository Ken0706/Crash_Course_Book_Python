def invite_poll():
	fav_lang = {
		"ken" : "python",
		"na" : "c#",
		"vy" : "java",
		"jen" : "ruby",
		"karl" : "java"
	}
	peole = ["karl", "ken", "mi", "jin"]
	for k, v in fav_lang.items():
		if k in peole:
			print(f"Thank {k.title()} for responding.")
		else : print(f"We invite {k.title()} take the poll.")
	name = input("Enter name : ").lower()
	if name in fav_lang.keys():
		print(f"Thank {name.title()} for responding.")
	else : print(f"We invite {name.title()} take the poll.")
	print("Languages use : ")
	print("-" * 10)
	for v in set(fav_lang.values()):
		print(f"- {v.title()}")
def main():
	invite_poll()
if __name__ == '__main__':
	main()