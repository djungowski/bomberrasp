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
		self.__field.render()

	def get_size(self):
		return self.__size

	def get_screen(self):
		return self.__screen

	def get_background_color(self):
		return self.__background_color
