import pygame, os

class Bomb:
	__bomb = None

	def __init__(self):
		bomb_image_file = os.path.join("gfx", "bomb.png")
		self.__bomb = pygame.image.load(bomb_image_file)

	def get_surface(self):
		return self.__bomb
