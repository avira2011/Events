import pgzrun
import random

WIDTH = 500
HEIGHT = 500

TITLE = 'Hit It'
hutao = Actor('hutao')

def draw():
    hutao.draw()
    screen.draw.text(message,center = (400,10), fontsize = 30)

def place():
    hutao.x = random.randint(0,WIDTH)
    hutao.y = random.randint(0,HEIGHT)

message = ""

def on_mouse_down(pos):
    global message
    if hutao.collidepoint(pos):
        screen.clear()
        message = "Good Shot"
        place()
    else:
        screen.clear()
        message = "You missed"



pgzrun.go()