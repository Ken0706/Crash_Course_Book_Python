import random
def check_input():
	global alien_color
	global second, first
	color = ["green", "yellow", "red"]
	first, second = random.sample(color,2)
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
		print("+ 10 points... You first!!!")
	elif alien_color == second:
		print("+ 5 points... You second!!!")
	else:
		print("You fail!!!")
			
	

def main():
	check_input()
	play_game(alien_color,first, second)

if __name__ == "__main__":
	main()