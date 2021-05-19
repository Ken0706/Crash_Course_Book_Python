import random
def check_input():
	global alien_color
	global second, first,third
	color = ["green", "yellow", "red"]
	first, second,third = random.sample(color,3)
	while True:
		try :
			alien_color = input("Enter color (green, yellow, red) : ")
			if alien_color in color:
				break
			elif len(alien_color) == 0:
				print("You fail!!!")
			else:
				print("Try again...")
		except ValueError:
			print("Try again...")

def play_game(alien_color, first, second):
	if alien_color == first:
		print("+ 15 points... You first!!!")
	elif alien_color == second:
		print("+ 10 points... You second!!!")
	elif alien_color == third:
		print("+ 5 points... You third!!!")
	else:
		print("You fail!!!")
			
	

def main():
	check_input()
	play_game(alien_color,first, second)

if __name__ == "__main__":
	main()