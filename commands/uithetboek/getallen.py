import pgzrun
from random import randint

WIDTH = 400
HEIGHT = 400

stippen = []
lijnen = []

volgende_stip = 0

for stip in range(0, 10):
    actor = Actor("dot")
    actor.pos = randint(20, WIDTH - 20), randint(20, HEIGHT - 20)
    stippen.append(actor)

def draw():
    screen.fill("black")
    getal = 1
    for stip in stippen:
        screen.draw.text(str(getal), (stip.pos[0], stip.pos[1] + 12))
        stip.draw()
        getal = getal + 1
    for lijn in lijnen:
        screen.draw.line(lijn[0], lijn[1], (100, 0, 0))

def on_mouse_down(pos):
    global volgende_stip
    global lijnen
    if stippen[volgende_stip].collidepoint(pos):
        if volgende_stip:
            lijnen.append((stippen[volgende_stip - 1].pos, stippen[volgende_stip].pos))
        volgende_stip = volgende_stip + 1
    else:
        lijnen = []
        volgende_stip = 0

pgzrun.go()