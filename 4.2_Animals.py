animals = ["ant", "cat", "bird", "rabbit", "dog", "elephant"]
for animal in animals:
	if animal[:1] in ["u", "e", "o", "a", "i"]:
		#print(animal[:1])
		print(f"An {animal.title()} would make a great pet!")
		continue
	print(f"A {animal.title()} would make a great pet!")
print("I love all animals")
