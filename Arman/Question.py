import sys
import pygame
from pygame.locals import *

mline_text= "Question"
text = "Write a Program that print minimum and maximum of 4 intigers \nExample one \n4 \n5\n6 \n7 \n minimum = 4, maximum = 7"
WIDTH = 600
HEIGHT= 500
WHITE = 255,255,255
BLUE  = 0,0,200

###
### Draw a multi-line block of text to the screen at (x,y)
### With optional justification
###
def multilineRender(screen, text,text2, x,y, the_font, colour=(128,128,128), justification="left"):
    justification = justification[0].upper()
    text = text.strip().replace('\r','').split('\n')
    text2 = text2.strip().replace('\r','').split('\n')
    max_width = 0
    text_bitmaps = []
    max_width2 = 0
    text_bitmaps2 = []
    # Convert all the text into bitmaps, calculate the justification width
    for t in text:
        text_bitmap = the_font.render(t, True, colour)
        text_width  = text_bitmap.get_width()
        text_bitmaps.append((text_width, text_bitmap))
        if (max_width < text_width):
            max_width = text_width
    for t in text2:
        text_bitmap = the_font.render(t, True, colour)
        text_width2  = text_bitmap.get_width()
        text_bitmaps2.append((text_width, text_bitmap))
        if (max_width2 < text_width2):
            max_width2 = text_width2
    # Paint all the text bitmaps to the screen with justification
    for (width, bitmap) in text_bitmaps:
        xpos = x
        width_diff = max_width - width
        screen.blit(bitmap, (xpos, y) )
        y += bitmap.get_height()
    for (width2, bitmap2) in text_bitmaps2:
        xpos2 = x
        width_diff2 = max_width2 - width2
        screen.blit(bitmap2, (xpos2, y) )
        y += bitmap.get_height()

#start pygame, create a font for the text
pygame.init()
screen2 = pygame.display.set_mode((600,500))
pygame.font.init
myfont = pygame.font.Font(None,14)
screen2.fill(BLUE)
# three copies of the same text, different justificaiton
multilineRender(screen2, mline_text + " one",text, 20, 20, myfont, WHITE)
pygame.display.update()

while (True):
    event = pygame.event.wait()
    if event.type == QUIT:
        pygame.quit()
        sys.exit()