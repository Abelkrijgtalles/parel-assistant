from random import randint

WIDTH = 800
HEIGHT = 600
MIDDEN_X = WIDTH / 2
MIDDEN_Y = HEIGHT / 2

beweging_lijst = []
toon_lijst = []

score = 0
huidige_beweging = 0
tellen = 4
dans_lengte = 4

zeg_dans = False
toon_aftellen = True
bewegingen_voltooid = False
game_over = False

danser = Actor("dancer-start")
danser.pos = MIDDEN_X + 5, MIDDEN_Y - 40

omhoog = Actor("up")
omhoog.pos = MIDDEN_X, MIDDEN_Y + 110
rechts = Actor("right")
rechts.pos = MIDDEN_X + 60, MIDDEN_Y + 170
omlaag = Actor("down")
omlaag.pos = MIDDEN_X, MIDDEN_Y + 230
links = Actor("left")
links.pos = MIDDEN_X - 60, MIDDEN_Y + 170

def draw():
    global game_over, score, zeg_dans
    global count, toon_aftellen
    if not game_over:
        screen.clear()
        screen.blit("stage", (0, 0))
        danser.draw()
        omhoog.draw()
        omlaag.draw()
        rechts.draw()
        links.draw()
        screen.draw.text("Score: " +
                        str(score), color="black" ,
                        topleft=(10, 10))

        if zeg_dans:
            screen.draw.text("Dans!", color="black",
                            topleft=(MIDDEN_X - 65, 150), fontsize=60)

        if toon_aftellen:
            screen.draw.text(str(tellen), color="black",
                            topleft=(MIDDEN_X - 8, 150), fontsize=60)

    else:
        screen.clear()
        screen.blit("stage", (0, 0))
        screen.draw.text("Score: " + 
                        str(score), color="black",
                        topleft=(10, 10))
        screen.draw.text("GAME OVER!", color="black",
                        topleft=(MIDDEN_X - 130, 220), fontsize=60)

    return

def reset_danser():
    global game_over
    if not game_over:
        danser.image = "dancer-start"
        omhoog.image = "up"
        rechts.image = "right"
        omlaag.image = "down"
        links.image = "left"
    return

def update_danser(beweging):
    global game_over
    if not game_over:
        if beweging == 0:
            omhoog.image = "up-lit"
            danser.image = "dancer-up"
            clock.schedule(reset_danser, 0.5)
        elif beweging == 1:
            rechts.image = "right-lit"
            danser.image = "dancer-right"
            clock.schedule(reset_danser, 0.5)
        elif beweging == 2:
            omlaag.image = "down-lit"
            danser.image = "dancer-down"
            clock.schedule(reset_danser, 0.5)
        elif beweging == 3:
            links.image = "left-lit"
            danser.image = "dancer-left"
            clock.schedule(reset_danser, 0.5)
    return

def toon_bewegingen():
    global beweging_lijst, toon_lijst, dans_lengte
    global zeg_dans, toon_aftellen, huidige_beweging
    if toon_lijst:
        deze_beweging = toon_lijst[0]
        toon_lijst = toon_lijst[1:]
        if deze_beweging == 0:
            update_danser(0)
            clock.schedule(toon_bewegingen, 1)
        elif deze_beweging == 1:
            update_danser(1)
            clock.schedule(toon_bewegingen, 1)
        elif deze_beweging == 2:
            update_danser(2)
            clock.schedule(toon_bewegingen, 1)
        else:
            update_danser(3)
            clock.schedule(toon_bewegingen, 1)
        
    else:
        zeg_dans = True
        toon_aftellen = False
    return

def genereer_bewegingen():
    global beweging_lijst, dans_lengte, tellen
    global toon_aftellen, zeg_dans
    tellen = 4
    beweging_lijst = []
    zeg_dans = False
    for beweging in range(0, dans_lengte):
        rand_beweging = randint(0, 3)
        beweging_lijst.append(rand_beweging)
        toon_lijst.append(rand_beweging)
    toon_aftellen = True
    aftellen()
    return

def aftellen():
    global tellen, game_over, toon_aftellen
    if tellen > 1:
        tellen = tellen - 1
        clock.schedule(aftellen, 1)
    else:
        toon_aftellen = False
        toon_bewegingen()
    return

def volgende_beweging():
    global dans_lengte, huidige_beweging, bewegingen_voltooid
    if huidige_beweging < dans_lengte - 1:
        huidige_beweging = huidige_beweging + 1
    else:
        bewegingen_voltooid = True
    return

def on_key_up(key):
    global score, game_over, beweging_lijst, huidige_beweging
    if key == keys.UP:
        update_danser(0)
        if beweging_lijst[huidige_beweging] == 0:
            score = score + 1
            volgende_beweging()
        else:
            game_over = True
    elif key == keys.RIGHT:
        update_danser(1)
        if beweging_lijst[huidige_beweging] == 1:
            score = score + 1
            volgende_beweging()
        else:
            game_over = True
    elif key == keys.DOWN:
        update_danser(2)
        if beweging_lijst[huidige_beweging] == 2:
            score = score + 1
            volgende_beweging()
        else:
            game_over = True
    elif key == keys.LEFT:
        update_danser(3)
        if beweging_lijst[huidige_beweging] == 3:
            score = score + 1
            volgende_beweging()
        else:
            game_over = True
    return

genereer_bewegingen()
music.play("vanishing-horizon")

def update():
    global game_over, huidige_beweging, bewegingen_voltooid
    if not game_over:
        if bewegingen_voltooid:
            genereer_bewegingen()
            bewegingen_voltooid = False
            huidige_beweging = 0
    else:
        music.stop()