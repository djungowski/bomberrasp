import pygame, os

class Field:
	__brick = None;
	__bricks = [];
	__screen = None
	logging = None;

	def __init__(self, screen):
		self.__screen = screen
		brick_image_file = os.path.join("gfx", "brick.png")
		self.__brick = pygame.image.load(brick_image_file)

	def get_brick_size(self):
		return self.__brick.get_size()

	def render_brick(self, position):
		self.__screen.get_screen().blit(self.__brick, position)
		brick_size = self.get_brick_size()
		brick_rect = pygame.Rect(list(position) + list(brick_size))
		self.__bricks.append(brick_rect)

	def render(self):
		screen_size = self.__screen.get_size()
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
					self.render_brick((col * brick_size[0], row * brick_size[1]))
			# Every other line: brick every 2nd position
			else:
				for col in range(cols):
					if col == 0 or col == cols - 1:
						self.render_brick((col * brick_size[0], row * brick_size[1]))
					elif col % 2 == 0 and row % 2 == 0:
						self.render_brick((col * brick_size[0], row * brick_size[1]))

		return

	def get_bricks(self):
		return self.__bricks

	def add_player(self, player):
		self.__screen.get_screen().blit(player.get_surface(), player.get_position())
		pygame.display.update()

	def add_bomb(self, bomb, position):
		self.__screen.get_screen().blit(bomb.get_surface(), position)

	def move_player(self, player, new_position):
		player_size = player.get_size()
		old_position = player.get_position()
		pygame.draw.rect(self.__screen.get_screen(), self.__screen.get_background_color(), (old_position[0], old_position[1], player_size[0], player_size[1]))
		self.__screen.get_screen().blit(player.get_surface(), new_position)

		# Not needed when HWSURFACE is true :-)
		pygame.display.update()

