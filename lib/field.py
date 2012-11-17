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

		cols = screen_size[0] / brick_size[0]
		self.logging.debug("Columns: %d" % cols)

		rows = screen_size[1] / brick_size[1]
		self.logging.debug("Rows: %d" % rows)

		upper_rect = pygame.Rect(0, 0, screen_size[0], brick_size[1])
		lower_rect = pygame.Rect(0, brick_size[1] * (rows - 1), screen_size[0], brick_size[1])
		left_rect = pygame.Rect(0, 0, brick_size[1], brick_size[0] * rows)
		right_rect = pygame.Rect(brick_size[1] * (cols - 1), 0, brick_size[1], brick_size[0] * rows)

		self.__bricks.append(upper_rect)
		self.__bricks.append(lower_rect)
		self.__bricks.append(left_rect)
		self.__bricks.append(right_rect)

		self.logging.debug("Upper brick rect: %s" % upper_rect)
		self.logging.debug("Lower brick rect: %s" % lower_rect)
		self.logging.debug("Left brick rect: %s" % left_rect)
		self.logging.debug("Right brick rect: %s" % right_rect)

		for row in range(rows):
			self.logging.debug("Painting row #%d" % row)
			# First and last line go through
			if row == 0 or row == rows - 1:
				for col in range(cols):
					screen.get_screen().blit(self.__brick, (col * brick_size[0], row * brick_size[1]))
			# Every other line: brick every 2nd position
			else:
				for col in range(cols):
					if col == 0 or col == cols - 1:
						screen.get_screen().blit(self.__brick, (col * brick_size[0], row * brick_size[1]))
					elif col % 2 == 0 and row % 2 == 0:
							screen.get_screen().blit(self.__brick, (col * brick_size[0], row * brick_size[1]))

		return
		# Paint upper row
		for i in range(cols):
			screen.get_screen().blit(self.__brick, (i * brick_size[0], 0))

		# Paint bottom row
		for i in range(cols):
			screen.get_screen().blit(self.__brick, (i * brick_size[0], (rows - 1) * brick_size[1]))

		# Paint left side
		for i in range(rows):
			screen.get_screen().blit(self.__brick, (0, i * brick_size[1]))

		# Paint right side
		for i in range(rows):
			screen.get_screen().blit(self.__brick, (screen_size[0] - brick_size[0], i * brick_size[1]))

	def get_bricks(self):
		return self.__bricks
