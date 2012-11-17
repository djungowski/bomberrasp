
class Movement:
	screen = None

	# With how many frames is movement animated
	__frames = 5

	def __init__(self, screen):
		self.__screen = screen

	def __fix_position(self, player, new_position):
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

	def move_player(self, player, new_position):
		old_position = player.get_position()
		new_position = self.__fix_position(player, new_position)

		movement_x = new_position[0] - old_position[0]
		movement_x_step = movement_x / self.__frames

		movement_y = new_position[1] - old_position[1]
		movement_y_step = movement_y / self.__frames

		current_position = list(old_position)

		for x in range(self.__frames):
			current_position[0] = current_position[0] + movement_x_step
			current_position[1] = current_position[1] + movement_y_step
			self.__screen.move_player(player, current_position)
		player.set_position(current_position)
