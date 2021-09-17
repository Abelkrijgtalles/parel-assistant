import pgzrun
from random import randint
appel = Actor("apple")

def draw():
    screen.clear()
    appel.draw()

def on_mouse_down(pos):
    if appel.collidepoint(pos):
        print("Goed schot!")
        plaats_appel()
    else:
        print("Je hebt gemist!")
        exit()

def plaats_appel():
    appel.x = randint(10, 400)
    appel.y = randint(10, 300)

plaats_appel()
pgzrun.go()