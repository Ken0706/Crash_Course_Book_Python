print("Cube of number with list comprehension : ")
cubes = [ v ** 3 for v in range(1,11)]
for i, v in enumerate(cubes):
	print(f"{i + 1} ^ 3 = {v}")