#!/usr/bin/python

import pygame, os, sys, logging

# Custom libs
import lib.player
import lib.screen
import lib.movement
import lib.field
import lib.bomb

# Set up logger
if "--debug" in sys.argv or "-d" in sys.argv:
	loglevel = logging.DEBUG
else:
	loglevel = logging.CRITICAL

logging.basicConfig(filename="debug.log", level=loglevel)

pygame.init()
# key-repeat is when keys are kept pushed (important for movement)
pygame.key.set_repeat(1, 50)

screen = lib.screen.Screen()
screen.logging = logging

field = lib.field.Field(screen)
field.logging = logging
screen.set_field(field)
brick_size = field.get_brick_size()

player1 = lib.player.Player([brick_size[0], brick_size[1]])
field.add_player(player1)

movement = lib.movement.Movement(screen)
movement.logging = logging
movement.set_field(field)

bomb = lib.bomb.Bomb()

def input(events):
	for event in events:
		logging.debug(event)

		# Do nothing when the key is released
		if (event.type == pygame.KEYUP):
			return

		if event.type == pygame.QUIT:
			sys.exit(0)
		elif hasattr(event, "key"):
			current_position = player1.get_position()
			new_position = list(player1.get_position())
			# Todo: Remove the next 2 lines
			player_size = player1.get_size()
			window_size = screen.get_size()

			if event.key == pygame.K_UP:
				# Only move monkey up if this doesn't mean that the monkey leaves the screen
				new_position[1] = current_position[1] - player1.movement_step
				movement.move_player(player1, new_position, "up")

			elif event.key == pygame.K_DOWN:
				# only move monkey if this doesn't mean that the monkey leaves the screen
				new_position[1] = current_position[1] + player1.movement_step
				movement.move_player(player1, new_position, "down")

			elif event.key == pygame.K_LEFT:
				# only move monkey left, if it doesn't leave the screen
				new_position[0] = current_position[0] - player1.movement_step
				movement.move_player(player1, new_position, "left")

			elif event.key == pygame.K_RIGHT:
				# if moving right would mean leaving the screen, set position to maximum possible
				new_position[0] = current_position[0] + player1.movement_step
				movement.move_player(player1, new_position, "right")

			elif event.key == pygame.K_SPACE:
				field.add_bomb(bomb, current_position)

			elif event.key == pygame.K_c and pygame.key.get_mods() & KMOD_CTRL:
				sys.exit(0)



while True:
	input(pygame.event.get())
