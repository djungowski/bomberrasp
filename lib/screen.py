import pygame, sys


class Screen:
	__window = None
	__size = (1280, 720)
	__background_color = (255, 255, 255)
	__screen = None
	__field = None

	def __init__(self):
		self.__init_maximum_size()
		self.__window = pygame.display.set_mode(self.__size, pygame.FULLSCREEN | pygame.HWSURFACE)
		pygame.display.set_caption("Monkey Fever")
		pygame.mouse.set_visible(False)
		self.__screen = pygame.display.get_surface()
		background = pygame.Surface(self.__size)
		background = background.convert()
		background.fill(self.__background_color)
		self.__screen.blit(background, (0, 0))
		pygame.display.flip()

	def __init_maximum_size(self):
		display_info = pygame.display.Info()
		self.__size = (display_info.current_w, display_info.current_h)

	def set_field(self, field):
		self.__field = field

	def get_size(self):
		return self.__size

	def add_player(self, player):
		self.__screen.blit(player.get_surface(), player.get_position())
		pygame.display.update()

	def move_player(self, player, new_position):
		player_size = player.get_size()
		old_position = player.get_position()
		pygame.draw.rect(self.__screen, self.__background_color, (old_position[0], old_position[1], player_size[0], player_size[1]))
		self.__screen.blit(player.get_surface(), new_position)

		# Not needed when HWSURFACE is true :-)
#		pygame.display.update()
