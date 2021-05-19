def sort_lang(lang):
	lang.sort()
	print(*lang)
def sorted_lang(lang):
	tmp = sorted(lang)
	print(*tmp)
def reverse_lang(lang):
	lang.reverse()
	print(*lang)
def reversed_lang(lang):
	tmp = reversed(lang)
	print(*tmp)
def main():
	lang = ["france", "english", "german", "korean", "italian"]
	sort_lang(lang)
	sorted_lang(lang)
	reverse_lang(lang)
	reversed_lang(lang)
if __name__ == "__main__":
	main()
