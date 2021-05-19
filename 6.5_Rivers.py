def dict_rivers():
	rivers = {
		"nile" : "egypt",
		"mekong" : "campuchia",
		"hong" : "ha noi"
	}
	for k, v in rivers.items():
		print(f"The {k.title()} runs through {v.title()}")
	print("Rivers : ")
	for k in rivers.keys():
		print(f"- {k.title()}")
	print("Country : ")
	for v in rivers.values():
		print(f"- {v.title()}")

def main():
	dict_rivers()
if __name__ == '__main__':
	main()