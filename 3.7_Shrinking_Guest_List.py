from random import randrange
guests = ["ken", "nah", "ben", "Sonat", "Luck"]
msg1 = "\t\t\t\t\t\t--- Welcome my dinner !!! --- "
print(f"{msg1.upper()}")
for guest in range(len(guests)):
	print(f"\t\tWelcome {guests[guest].title()}, welcome to dinner with us - \
Your seat number is {guest + 1}!")
	guest_cant_go = guests[randrange(len(guests))]
	seat = guests.index(guest_cant_go)

print(f"--> {guest_cant_go.title()} cant go with seat number is {seat + 1} <--")
print(f"--> Tayah replace for {guest_cant_go.title()} <--")

for guest in range(len(guests)):
	guests[seat] = "Tayah"
	print(f"\t\tWelcome {guests[guest].title()}, welcome to dinner with us - \
Your seat number is {guest + 1}!")

msg2 = "\t--- Your seat numbers are changed as we have found \
a larger dinner table ---" 
print(f"{msg2.upper()}")
mid_seat = int(len(guests) / 2)
guests.insert(0,"Macro")
guests.insert(mid_seat,"Middle")
guests.append("Late")
"""guests.remove("Middle")
guests.remove("Late")
guests.remove("Macro")"""
for guest in range(len(guests)):
	print(f"\t\tWelcome {guests[guest].title()}, welcome to dinner with us - \
Your seat number changed is {guest + 1}!")


msg3 = "\t--- Unfortunately, the dinner was having problems \
so we limited the number of people that can attend to 2 people ---" 
print(f"{msg3.upper()}")
i = len(guests)
while i > 2:
	guest_pop = guests.pop()
	print(f"Sorry {guest_pop.title()}, you are not invited! ")
	i -= 1
for guest in range(len(guests)):
	print(f"Congratulations {guests[guest]}, you are invited! -- \
Your seat number is {guest + 1}")
print(guests)
print("\t\t\t\t --- END DINNER ---")
i = len(guests)
while i > 0 :
		del guests[0]
		i -=1
print(guests)








