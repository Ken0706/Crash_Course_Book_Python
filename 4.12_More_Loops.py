pizzas = ["cheese", "pepperoni", "seafood"]
friend_pizzas = pizzas[::]
pizzas.append("hawai")
friend_pizzas.append("turkey")
print(f"My favorite pizzas are : ",end = " ")
for i,pizza in enumerate(pizzas):
	if i == (len(pizzas) - 1):
		print(f"{pizza} pizza.", end = " ")
		break
	print(f"{pizza} pizza,", end = " ")

print()
print("My friend's favorite pizzas: ", end = "")
for i,pizza in enumerate(friend_pizzas):
	if i == (len(friend_pizzas) - 1):
		print(f"{pizza} pizza.", end = " ")
		break
	print(f"{pizza} pizza,", end = " ")
