import pygame

class Movement:
	__screen = None
	__field = None
	logging = None

	def __init__(self, screen):
		self.__screen = screen

	def check_collision(self, player, new_position, direction):
		bricks = self.__field.get_bricks()
		player_size = player.get_size()
		player_rect = pygame.Rect(list(new_position) + list(player_size))
		self.logging.debug("Player Rect: %s" % player_rect)

		collide_index = player_rect.collidelist(bricks)
		if collide_index != -1:
			self.logging.debug("Collide rect index: %d" % collide_index)
			rect = bricks[collide_index]


			self.logging.debug("Rect: %s" % rect)

			self.logging.debug("New position[0]: %d" % new_position[0])

			if direction == "left" and new_position[0] < rect.left + rect.width:
				new_position[0] = rect.left + rect.width

			if direction == "right" and new_position[0] + player_size[1] > rect.left:
				new_position[0] = rect.left - player_size[0]

			if direction == "down" and new_position[1] < rect.top:
				new_position[1] = rect.top - player_size[1]

			if direction == "up" and new_position[1] < rect.top + rect.height:
				new_position[1] = rect.top + rect.height

			return new_position
		else:
			return new_position
		


	def __fix_position(self, player, new_position, direction):
		new_position = self.check_collision(player, new_position, direction)

		player_size = player.get_size()
		window_size = self.__screen.get_size()

		if new_position[0] + player_size[0] > window_size[0]:
			new_position[0] = window_size[0] - player_size[0]

		if new_position[0] < 0:
			new_position[0] = 0

		if new_position[1] + player_size[1] > window_size[1]: 
			new_position[1] = window_size[1] - player_size[1]

		if new_position[1] < 0:
			new_position[1] = 0
	
		return new_position

	def move_player(self, player, new_position, direction):
		new_position = self.__fix_position(player, new_position, direction)
		self.__field.move_player(player, new_position)
		player.set_position(new_position)

	def set_field(self, field):
		self.__field = field
