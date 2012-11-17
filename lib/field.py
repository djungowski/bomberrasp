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

	def render_brick(self, screen, position):
		screen.get_screen().blit(self.__brick, position)
		brick_size = self.get_brick_size()
		brick_rect = pygame.Rect(list(position) + list(brick_size))
		self.logging.debug("Brick rect: %s" % brick_rect)
		self.__bricks.append(brick_rect)

	def render(self, screen):
		screen_size = screen.get_size()
		brick_size = self.get_brick_size()

		cols = screen_size[0] / brick_size[0]
		self.logging.debug("Columns: %d" % cols)

		rows = screen_size[1] / brick_size[1]
		self.logging.debug("Rows: %d" % rows)

		for row in range(rows):
			self.logging.debug("Painting row #%d" % row)
			# First and last line go through
			if row == 0 or row == rows - 1:
				for col in range(cols):
					self.render_brick(screen, (col * brick_size[0], row * brick_size[1]))
			# Every other line: brick every 2nd position
			else:
				for col in range(cols):
					if col == 0 or col == cols - 1:
						self.render_brick(screen, (col * brick_size[0], row * brick_size[1]))
					elif col % 2 == 0 and row % 2 == 0:
						self.render_brick(screen, (col * brick_size[0], row * brick_size[1]))

		return

	def get_bricks(self):
		return self.__bricks
