import random
def check_input():
	global alien_color
	global goal
	color = ["green", "yellow", "red"]
	goal = random.choice(color)
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

def play_game(alien_color, goal):
	if alien_color == goal:
		print("You win!!!")
	else:
		print("You fail!!!")
			
	

def main():
	check_input()
	play_game(alien_color,goal)

if __name__ == "__main__":
	main()