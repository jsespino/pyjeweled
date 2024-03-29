# pyjeweled
# programmed by ryuchihoon
# using python2.6, pygame1.9.1
# skeleton code by scriptedfun.com

import pygame
from pygame.locals import *

SCREENRECT = Rect(0,0,640,480)
BACKCOLOR = 0,0,0

def main():
	pygame.init()

	screen = pygame.display.set_mode(SCREENRECT.size)

	# make background
	background = pygame.Surface(SCREENRECT.size).convert()
	background.fill(BACKCOLOR)
	screen.blit(background, (0,0))
	pygame.display.update()

	# keep track of sprites
	all = pygame.sprite.RenderUpdates()

	# keep track of time
	clock = pygame.time.Clock()

	# game loop
	while 1:

		# get input
		for event in pygame.event.get():
			if event.type == QUIT \
			   or (event.type == KEYDOWN and \
			       event.key == K_ESCAPE):
				return

		# clear sprites
		all.clear(screen, background)

		# update sprites
		all.update()

		# redraw sprites
		dirty = all.draw(screen)
		pygame.display.update(dirty)

		# maintain frame rate
		clock.tick(30)

if __name__ == '__main__':
	main()
	
