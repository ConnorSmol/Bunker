import ui

import random

import time

import sound

#camoflage graphic used found on free site blog.spoongraphics.co.uk
#tank and helicopter icons found on free site icons8.com

#set up a score variable for later and timer
global score

#hard time coming up multiple title screens so do button pushes
global titlecount
titlecount = 0

#easy splash screen
def SplashButton(sender):
	#hide all elements until SplashButton is pressed twice
	global titlecount
	if titlecount < 1:
		sound.play_effect('arcade:Coin_1')
		view['SplashButton'].image = ui.Image.named('IMG_0295.PNG').with_rendering_mode(ui.RENDERING_MODE_ORIGINAL)
		titlecount = titlecount + 1
	else:
		sound.play_effect('arcade:Coin_1')
		view['SplashButton'].alpha = 0
		view['TitleLabel'].alpha = 1
		view['InstructionButton'].alpha = 1
		view['PlayButton'].alpha = 1

def InstructionButton(sender):
	#this code executes when the instruction button is pressed
	#this unhides the instruction label or hides it if visible
	if view['InstructionLabel'].alpha == 0:
		view['InstructionLabel'].alpha = 1
	else:
		view['InstructionLabel'].alpha = 0

def PlayButton(sender):
	#this code executes when the player presses Play
	#hide all buttons and labels
	view['TitleLabel'].alpha = 0
	view['InstructionLabel'].alpha = 0
	view['InstructionButton'].alpha = 0
	view['PlayButton'].alpha = 0
	sound.play_effect('arcade:Laser_2')

	#show the tank with random starting spot
	#y coordinate is given a dual range because of icon background issues
	#only used tank at first then added helicopter but kept TankImage as name, easier
	global x_spot
	global y_spot

	x_spot = random.randint(40,500)
	y_spot = (random.choice([random.randint(20,200),random.randint(300,500)]))
	#set up if upper half of screen helicopter lower half is tank
	if y_spot > 250:
		view['TankImage'].image = ui.Image.named('IMG_0288.PNG').with_rendering_mode(ui.RENDERING_MODE_ORIGINAL)
	else:
		view['TankImage'].image = ui.Image.named('IMG_0294.PNG').with_rendering_mode(ui.RENDERING_MODE_ORIGINAL)
	
	#unhide the tank and start the game
	view['TankImage'].alpha = 1
	view['TankImage'].x = (x_spot)
	view['TankImage'].y = (y_spot)
	
	#reset the score
	global score
	score = 0
	
	#start the timer immediately, otherwise it starts on first hit
	global start_time
	start_time = time.time()
	view['TimerLabel'].alpha = 0
	
def TankImage(sender):
	
	#seem to need to keep declaring the same variable
	global score
	
	#variables for moving the tank
	global x_spot
	global y_spot
	
	#if statement or maybe a do while
	#for each tap score goes up by one and the tank moves
	#reused code from above for randomizing location and if its a tank or helicopter
	if score < 19:	
		score = score +1
		sound.play_effect('arcade:Explosion_5')
		view['TimerLabel'].text = '%s'%(score)
		x_spot = random.randint(40,500)
		y_spot = (random.choice([random.randint(20,200),random.randint(300,500)]))
		if y_spot > 250:
			view['TankImage'].image = ui.Image.named('IMG_0288.PNG').with_rendering_mode(ui.RENDERING_MODE_ORIGINAL)
		else:
			view['TankImage'].image = ui.Image.named('IMG_0294.PNG').with_rendering_mode(ui.RENDERING_MODE_ORIGINAL)
		view['TankImage'].x = (x_spot)
		view['TankImage'].y = (y_spot)
	else:
		#calculate end time and figure out how long it took
		end_time = time.time()
		sound.play_effect('arcade:Powerup_1')
		view['TimerLabel'].text = 'It took you %d seconds to destroy 20 enemies' % (end_time-start_time)
		
		#reset the screen except the score box
		view['TitleLabel'].alpha = 1
		view['InstructionLabel'].alpha = 0
		view['InstructionButton'].alpha = 1
		view['PlayButton'].alpha = 1
		view['TankImage'].alpha = 0
		view['TimerLabel'].alpha = 1

view = ui.load_view()
view.name = 'Bunker Protector'
view.present('sheet')
