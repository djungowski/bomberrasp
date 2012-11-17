import pygame, os

class Field:
	__brick = None;
	__bricks = [];
	logging = None;

	def __init__(self):
		brick_image_file = os.path.join("gfx", "brick.png")
		self.__brick = pygame.image.load(brick_image_file)

	def get_brick_size(self):
		return self.__brick.get_size()

	def render(self, screen):
		screen_size = screen.get_size()
		brick_size = self.get_brick_size()

		bricks_per_row = screen_size[0] / brick_size[0]
		self.logging.debug("Bricks per row: %d" % bricks_per_row)

		bricks_per_column = screen_size[1] / brick_size[1]
		self.logging.debug("Bricks per col: %d" % bricks_per_column)

		upper_rect = pygame.Rect(0, 0, screen_size[0], brick_size[1])
		lower_rect = pygame.Rect(0, brick_size[1] * (bricks_per_column - 1), screen_size[0], brick_size[1])
		left_rect = pygame.Rect(0, 0, brick_size[1], brick_size[0] * bricks_per_column)
		right_rect = pygame.Rect(brick_size[1] * (bricks_per_row - 1), 0, brick_size[1], brick_size[0] * bricks_per_column)

		self.__bricks.append(upper_rect)
		self.__bricks.append(lower_rect)
		self.__bricks.append(left_rect)
		self.__bricks.append(right_rect)

		self.logging.debug("Upper brick rect: %s" % upper_rect)
		self.logging.debug("Lower brick rect: %s" % lower_rect)
		self.logging.debug("Left brick rect: %s" % left_rect)
		self.logging.debug("Right brick rect: %s" % right_rect)

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

	def get_bricks(self):
		return self.__bricks
