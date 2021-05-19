from random import randrange 
guests = ["ken", "nah", "ben", "Sonat", "Luck"]
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

msg = "\t--- Your seat numbers are changed as we have found \
a larger dinner table ---" 
print(f"{msg.upper()}")
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





