text = input("Enter : ")
number = int(input("Enter number : "))
lst = []
lst.append(text)
lst.append(number)
find_value = int(input("Enter value : "))
if text == "abc":
	print("abc is text you need.")
else :
	print(f"{text} isn't text you need.")
if text.lower() == "bcd":
	print("Lower BCD is text you need.")
else :
	print(f"Lower {text} isn't text you need.")
if number == 5:
	print("5 is number you need.")
else :
	if number > 5 :
		print(f"{number} isn't number you need.Must less than !!!")
	else :
		print(f"{number} isn't number you need.Must greater than !!!")
if text == "abc" and number == 5:
	print("Two answer correct.")
else:
	if text.lower() == "abc" or number == 5:
		print("One wrong.")
	else:
		print("Two wrong.")
print(lst)
for i, v in enumerate(lst):
	if find_value == v:
		print(f"{find_value} in list, index : {i}")
		
