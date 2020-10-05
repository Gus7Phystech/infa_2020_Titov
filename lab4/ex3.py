import random

import pygame
from pygame.draw import *

def draw_background(surface, sky_color, sky_polygon, ground_color, ground_polygon):
	'''
	func draws gray sky and getting color in rgb and polygons for them
	'''
	polygon(surface, ground_color, ground_polygon)
	polygon(surface, sky_color, sky_polygon)

def draw_moon(surface, color, pos, size):
	'''
	func draws moon getting background surface, color in rgb, size in pixels
	pos - tuple (x,y) - coords of the center
	'''
	circle(surface, color, pos, size)

def draw_house(surface, x, y, w, h):
	'''
	x, y - the base points are the upper left corner of the house
	w - width of the house
	h - height of the house
	'''

	# color consts
	HOUSE_COLOR = (110, 76, 9)
	LIGHTED_WINDOW_COLOR = (255, 255, 0)
	CURTAINED_WINDOW_COLOR = (139, 0, 0)
	DARK_WINDOW_COLOR = (128, 128, 128)

	range_of_colors = {
		1: LIGHTED_WINDOW_COLOR,
		2: CURTAINED_WINDOW_COLOR,
		3: DARK_WINDOW_COLOR
	}


	#house
	polygon(surface, HOUSE_COLOR, ([x,y+h] , [x+w, y+h ], [x+w, y], [x, y]))

	# first floor windows
	polygon(surface, range_of_colors[random.randint(1, 3)], ([x+(w//8),y+4*(h//6)] , [x+2*(w//8), y+4*(h//6) ], [x+2*(w//8), y+5*(h//6)], [x+(w//8), y+5*(h//6)]))
	polygon(surface, range_of_colors[random.randint(1, 3)], ([x+3*(w//8),y+4*(h//6)] , [x+4*(w//8), y+4*(h//6) ], [x+4*(w//8), y+5*(h//6)], [x+3*(w//8), y+5*(h//6)]))
	polygon(surface, range_of_colors[random.randint(1, 3)], ([x+5*(w//8),y+4*(h//6)] , [x+6*(w//8), y+4*(h//6) ], [x+6*(w//8), y+5*(h//6)], [x+5*(w//8), y+5*(h//6)]))




	# upper floor windows
	polygon(surface, range_of_colors[random.randint(1, 3)], ([x+(w//5),y] , [x+2*(w//5), y ], [x+2*(w//5), y + (h//2)], [x+(w//5), y + (h//2)]))
	polygon(surface, range_of_colors[random.randint(1, 3)], ([x+3*(w//5),y] , [x+4*(w//5), y ], [x+4*(w//5),  y + (h//2)], [x+3*(w//5),  y + (h//2)]))

	# chimney
	polygon(surface, (36, 34, 14), ([x+(w//6),y] , [x+2*(w//6), y ], [x+2*(w//6), y - h//4], [x+(w//6), y - h//4]))
	polygon(surface, (36, 34, 14), ([x+3*(w//6),y] , [x+4*(w//6), y ], [x+4*(w//6), y - h//6], [x+3*(w//6), y - h//6]))
	# roof
	polygon(surface, (0, 30, 0), ([x-(w//8),y] , [x+w+(w//8), y ], [x+w, y -(h//8)], [x, y - (h//8)]))
	# balcony
	polygon(surface, (0, 31, 27), ([x-(w//8),y + (h//2)] , [x+w+(w//8), y + (h//2) ], [x+w+(w//8), y + (h//2)+(h//10) ], [x-(w//8),y + (h//2)+(h//10)]))
	# fence
	polygon(surface, (0, 31, 27), ( [x-(w//8),y + (h//2)] , [x+(w//25), y + (h//2) ], [x+(w//25), y + (h//2)-(h//10)], [x-(w//8), y + (h//2)-(h//10)]))
	polygon(surface, (0, 31, 27), ([x+w+(w//8) - (h//10),y + (h//2)] , [x+w+(w//8), y + (h//2) ], [x+w+(w//8), y + (h//2)-(h//10)], [x+w+(w//8) - (h//10), y + (h//2)-(h//10)]))

	i=1
	while i < 11:
		polygon(surface, (0, 31, 27), ([x+i*(w//10),y + (h//2)] , [x+(i+1)*(w//10), y + (h//2) ], [x+(i+1)*(w//10),  y + (h//2)-(h//10)], [x+i*(w//10),  y + (h//2)-(h//10)]))
		i+=2
	polygon(surface, (0, 31, 27), ([x-(w//8),y + (h//2)-(h//10)] , [x+w+(w//8), y + (h//2)-(h//10) ], [x+w+(w//8), y + (h//2)-(h//9)], [x-(w//8), y + (h//2)-(h//9)]))

def draw_cloud(surface, color, x, y, h, w):
	'''
	func draws one cloud
	surface - screen the cloud is situated
	color - in rgb
	x - x_position of the left upper corner of rect around
	y - y_position of the left upper corner of rect around
	h - height
	w - width
	'''
	ellipse(surface, color, (x, y, h, w))


def draw_ghost(surface, bkg_color, x, y, r, h):
	'''
	func draws a ghost
	surface - screen for the ghost
	x, y - coords of the center of the head of the ghost
	r - radius of the head, the parameter also changes the wight of the grost
	h - height of the ghost
	'''
	#head
	circle(surface, WHITE_COLOR, (x, y), r)
	polygon(surface, WHITE_COLOR, ([x + r, y], [x + r * 1.2, y + h], [x - r * 1.2, y + h], [x - r, y]))

	#skirt is formed of 6 pairs of circles: white and colored the same as the background of the ghost
	R = int(r//2.5) #radius of the circles in the skirt
	for i in range(6):
		circle(surface, WHITE_COLOR, ((x - r) + R * i, y + h), R)
	for i in range(6):
		circle(surface, bkg_color, ((x - r) + R * i, y + h + R), R)

	# eyes
	ellipse(surface, BLUE_COLOR, (x - 0.5 * r, y - 0.5 * r, r * 0.25, r * 0.5))
	ellipse(surface, BLUE_COLOR, (x + 0.25 * r, y - 0.5 * r, r * 0.25, r * 0.5))
	ellipse(surface, BLACK_COLOR, (x - 0.50 * r, y - 0.3 * r, r * 0.25, r * 0.25))
	ellipse(surface, BLACK_COLOR, (x + 0.25 * r, y - 0.3 * r, r * 0.25, r * 0.25))

	# mouth
	ellipse(surface, BLACK_COLOR, (x + (0.1 * r)*(-1), y + 0.1 * r, r * 0.7, r * 0.5))


pygame.init()

FPS = 30

#CONSTS of size
SCREEN_WIGHT = 400
SCREEN_HEIGHT = 400
PART_OF_SKY = 0.375

#CONSTS of color
WHITE_COLOR = (255, 255, 255)
BLACK_COLOR = (0, 0, 0)

GRAY_COLOR = (105, 105, 105)
DARKER_LIGHT_GRAY = (60, 60, 60)
LIGHT_GRAY = (40, 40, 40)
LIGHT_LIGHT_GRAY = (30, 30, 30)

BLUE_COLOR = (0, 191, 255)

#creating surfaces
'''
BKG - for sky, ground, moon, houses, 
'''
BKG_SURFACE = pygame.display.set_mode((SCREEN_WIGHT, SCREEN_HEIGHT))
BKG_SURFACE.fill(WHITE_COLOR)

TRANSPARENT_GHOST_SCREEN = pygame.Surface((SCREEN_WIGHT, SCREEN_HEIGHT))
TRANSPARENT_GHOST_SCREEN.set_alpha(180)
TRANSPARENT_GHOST_SCREEN.fill(BLACK_COLOR)
TRANSPARENT_GHOST_SCREEN.set_colorkey(BLACK_COLOR)

TRANSPARENT_CLOUD_SCREEN = pygame.Surface((SCREEN_WIGHT, SCREEN_HEIGHT))
TRANSPARENT_CLOUD_SCREEN.set_alpha(200)
TRANSPARENT_CLOUD_SCREEN.fill(GRAY_COLOR)
TRANSPARENT_CLOUD_SCREEN.set_colorkey(GRAY_COLOR)


#BACKGROUND LAYER
# background
draw_background(BKG_SURFACE, GRAY_COLOR, 							#sky params
							([0,0],
							[0, PART_OF_SKY*SCREEN_HEIGHT],
							[SCREEN_WIGHT, PART_OF_SKY*SCREEN_HEIGHT],
							[SCREEN_WIGHT, 0]),

							BLACK_COLOR,							#ground params
							([0,PART_OF_SKY*SCREEN_HEIGHT] ,
							[SCREEN_WIGHT, PART_OF_SKY*SCREEN_HEIGHT ],
							[SCREEN_WIGHT, SCREEN_HEIGHT],
							[0, SCREEN_HEIGHT]))
#moon
draw_moon(BKG_SURFACE, WHITE_COLOR, (350, 50), 20)

#1ST LAYER
#four houses
draw_house(BKG_SURFACE, 30,100,50,100)
draw_house(BKG_SURFACE, 30,300,50,100)
draw_house(BKG_SURFACE, 100,200, 100,150)
draw_house(BKG_SURFACE, 150,60,50,100)

#2ND LAYER
#one cloud one the backwards partially hiding the moon
draw_cloud(BKG_SURFACE, LIGHT_GRAY, 200, 20, 250, 30)

#3TH LAYER
#ghosts
draw_ghost(BKG_SURFACE, BLACK_COLOR, 300, 150, 30, 20)
draw_ghost(BKG_SURFACE, BLACK_COLOR, 300, 350, 30, 20)
rot = pygame.transform.rotate(TRANSPARENT_GHOST_SCREEN, 45)
draw_ghost(TRANSPARENT_GHOST_SCREEN, BLACK_COLOR, 180, 350,  30, 30)

#4TH LAYER
#clouds in the forefront
draw_cloud(BKG_SURFACE, DARKER_LIGHT_GRAY, 80, 100, 100, 20)
draw_cloud(TRANSPARENT_CLOUD_SCREEN, LIGHT_LIGHT_GRAY, 150, 50, 140, 40)
draw_cloud(TRANSPARENT_CLOUD_SCREEN, LIGHT_LIGHT_GRAY, 150, 200, 200, 30)
draw_cloud(TRANSPARENT_CLOUD_SCREEN, LIGHT_LIGHT_GRAY, 50, 150, 100, 30)


#blitting surfaces
BKG_SURFACE.blit(TRANSPARENT_CLOUD_SCREEN,(0, 0))
BKG_SURFACE.blit(TRANSPARENT_GHOST_SCREEN,(0, 0))

pygame.display.update()
clock = pygame.time.Clock()
finished = False

while not finished:
    clock.tick(FPS)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            finished = True

pygame.quit()
