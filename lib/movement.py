
class Movement:
	screen = None

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
		new_position = self.__fix_position(player, new_position)	
		self.__screen.move_player(player, new_position)
		player.set_position(new_position)
