def dict_language():
	favorite_languages = {
						"ken" : "python",
						"nah" : "ruby"
						}
	for i, k in enumerate(favorite_languages):
		print("- " + str(k).title() + " : " + str(favorite_languages[k]).title())
	n = int(input("Enter quatity name you want add : "))
	for i in range(n):
		new_name = input("Enter name : ").lower()
		new_language = input("Enter language : ")
		favorite_languages[new_name] = new_language
	print("After add")
	for i, k in enumerate(favorite_languages):
		print("- " + str(k).title() + " : " + str(favorite_languages[k]).title())
def main():
	dict_language()
if __name__ == '__main__':
	main()