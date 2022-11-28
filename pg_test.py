import pygame
import random


def game(**kwargs):
	print("inside the game function....")
	for key, value in kwargs.items():
		print(key, value)
		
	print("bye bye")
	pygame.quit()
	score = random.randint(2000,5000)
	return score
	

if __name__ == "__main__":
	print("Program can only be started from towermenu.py")

