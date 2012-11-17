import os

import pygame

class Player:
	__position = [0, 0]
	__size = None
	__surface = None
	movement_step = 15

	def __init__(self, position):
		self.__position = position
		self.load_image()

	def load_image(self):
		monkey_head_file_name = os.path.join("gfx", "player1.png")
		self.__surface = pygame.image.load(monkey_head_file_name)
		self.__size = self.__surface.get_size()

	def set_position(self, position):
		self.__position = position

	def get_position(self):
		return self.__position

	def get_size(self):
		return self.__size

	def get_surface(self):
		return self.__surface

	def move_to(self):
		print("Nothing yet")
		
