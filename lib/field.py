import pygame, os

class Field:
	__brick = None;
	__logging = None;

	def __init__(self):
		brick_image_file = os.path.join("gfx", "brick.png")
		self.__brick = pygame.image.load(brick_image_file)

	def set_logging(self, logging):
		self.__logging = logging

	def get_brick_size(self):
		return self.__brick.get_size()

	def render(self, screen):
		screen_size = screen.get_size()
		brick_size = self.get_brick_size()

		bricks_per_row = screen_size[0] / brick_size[0]
		self.__logging.debug("Bricks per row: %d" % bricks_per_row)

		bricks_per_column = screen_size[1] / brick_size[1]
		self.__logging.debug("Bricks per col: %d" % bricks_per_column)

		# Paint upper row
		for i in range(bricks_per_row):
			screen.get_screen().blit(self.__brick, (i * brick_size[0], 0))

		# Paint bottom row
		for i in range(bricks_per_row):
			screen.get_screen().blit(self.__brick, (i * brick_size[0], (bricks_per_column - 1) * brick_size[1]))

		# Paint left side
		for i in range(bricks_per_column):
			screen.get_screen().blit(self.__brick, (0, i * brick_size[1]))

		# Paint right side
		for i in range(bricks_per_column):
			screen.get_screen().blit(self.__brick, (screen_size[0] - brick_size[0], i * brick_size[1]))
