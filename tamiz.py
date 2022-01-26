import pygame as py
from pygame.locals import *
import tkinter.filedialog as tkfd
#import shutil.copy as sc

py.init()
screen_w = 1024
screen_h = 768	
screen = py.display.set_mode((screen_w, screen_h))

class Picture:
	def __init__(self, address):
		self.x = 0
		self.y = 0
		self.w = screen_w
		self.h = screen_h
		self.address = address
		self.pic = py.image.load(address)
		self.pic = py.transform.scale(self.pic, (self.w, self.h))
		return

	def show(self):
		screen.blit(self.pic, (self.x, self.y))
		return

class Button:
	def __init__(self, x, y, w, h, address):
		self.x = x
		self.y = y
		self.w = w
		self.h = h
		self.address = address
		self.pic = py.image.load(address)
		self.pic = py.transform.scale(self.pic, (w, h))
		return

	def show(self):
		screen.blit(self.pic, (self.x, self.y))
		return

class Level:
	def __init__(self, ind):
		self.id = ind
		return

def updateScreen():
	py.display.update()
	py.time.Clock().tick(30)
	return

def onRect(pos, button):
	if button.x <= pos[0] <= button.x + button.w:
		if button.y <= pos[1] <= button.y + button.h:
			return True
	return False
def Question():
	mline_text= "Question"
	file = open("Question.txt", "r")
	text = file.readlines(-1)
	WHITE = 255,255,255
	BLUE  = 0,0,200

	###
	### Draw a multi-line block of text to the screen at (x,y)
	### With optional justification
	###
	def multilineRender(screen, text,text2, x,y, the_font, colour=(128,128,128), justification="left"):
		justification = justification[0].upper()
		text = text.strip().replace('\r','').split('\n')
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
	py.init()
	screen = py.display.set_mode((screen_w,screen_h))
	py.font.init
	myfont = py.font.Font(None,30)
	home_button = Button(143.5 + 150 + 143.5 + 150 + 143.5, 400, 150, 150, "home-button.png")
	while True:
		screen.fill(BLUE)
		home_button.show()
		go = ""
		multilineRender(screen, mline_text + " one",text, 20, 20, myfont, WHITE)
		py.display.update()
		for event in py.event.get():
			if event.type == py.MOUSEBUTTONDOWN:
				#(x, y) = event.pos
				if onRect(event.pos, home_button):
					go = "return"
		if go == "return":
			return
	return
def showLevel(level):
	background = Picture("index.jpg")
	home_button = Button(143.5 + 150 + 143.5 + 150 + 143.5, 400, 150, 150, "home-button.png")
	questions_button = Button(100 + 100,100,100,100,"png/buttons/normal/help.png")
	while True:
		background.show()
		home_button.show()
		questions_button.show()
		updateScreen()
		
		go = ""
		for event in py.event.get():
			if event.type == py.QUIT:
				py.quit()
				exit()
			if event.type == py.MOUSEBUTTONDOWN:
				#(x, y) = event.pos
				if onRect(event.pos, home_button):
					go = "return"
			if event.type == py.MOUSEBUTTONDOWN:
				if onRect(event.pos,questions_button):
					go = "Q"
			if event.type == py.MOUSEBUTTONDOWN:
				pass
				#(x, y) = event.pos
		if go == "Q":
			Question()
		if go == "return":
			return
	return
#################### TODO ####################
def getLevels():
	levels_buttons = []
	levels_buttons.append(Button(100,463, 40, 40, "level 1.png"))
	#levels_buttons.append(Button(143, 100, 150, 150, "level 1.png"))
	levels_buttons.append(Button(150,463, 40, 40, "level 2.png"))
	#levels_buttons.append(Button(143.5 + 150 + 143.5, 100, 150, 150, "level 2.png"))
	levels_buttons.append(Button(200,463, 40, 40, "level 3.png"))
	levels = []
	levels.append(Level(1))
	levels.append(Level(2))
	levels.append(Level(3))
	return (levels_buttons, levels)
##############################################
def menu():
	background = Picture("map/island.png")
	(levels_buttons, levels) = getLevels()
	home_button = Button(143.5 + 150 + 143.5 + 150 + 143.5, 400, 150, 150, "home-button.png")
	while True:
		background.show()
		for level_button in levels_buttons:
			level_button.show()
		home_button.show()
		updateScreen()
		go = ""
		for event in py.event.get():
			if event.type == py.QUIT:
				py.quit()
				exit()
			if event.type == py.MOUSEBUTTONDOWN:
				#(x, y) = event.pos
				if onRect(event.pos, home_button):
					go = "menu"
				for i in range(len(levels_buttons)):
					if onRect(event.pos, levels_buttons[i]):
						go = "level"
						target_level = i
		if go == "menu":
			return
		if go == "level":
			showLevel(levels[i])

	return

def main():
	background = Picture("png/background1.png")
	start_button = Button(350, 214, 325, 125, "start-button.png")
	quit_button = Button(410, 350, 200, 75, "quit-button.png")

	while True:
		background.show()
		start_button.show()
		quit_button.show()
		updateScreen()

		go = ""
		for event in py.event.get():
			if event.type == py.QUIT:
				py.quit()
				exit()
			if event.type == py.MOUSEBUTTONDOWN:
				#(x,y) = event.pos
				if onRect(event.pos, start_button):
					go = "menu"
				if onRect(event.pos, quit_button):
					py.quit()
					exit()
		if go == "menu":
			menu()

	return

main()