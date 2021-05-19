from random import randrange
guests = ["ken", "nah", "ben", "Sonat", "Luck"]
for guest in range(len(guests)):
	print(f"\t\tWelcome {guests[guest].title()}, welcome to dinner with us - \
Your seat number is {guest + 1}!")
	guest_cant_go = guests[randrange(len(guests))]
	seat = guests.index(guest_cant_go)

print(f"XXX{guest_cant_go.title()} cant go with seat number is {seat + 1} XXX")
print(f"-->Tayah replace for {guest_cant_go.title()}<--")

for guest in range(len(guests)):
	guests[seat] = "Tayah"
	print(f"\t\tWelcome {guests[guest].title()}, welcome to dinner with us - \
Your seat number is {guest + 1}!")



