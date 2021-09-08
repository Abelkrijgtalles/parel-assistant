import turtle as t

testkleur = "blue"
snelheid = "normal"
positie = "idk"


def test():
    t.penup()
    t.speed(snelheid)
    t.pensize(1)
    t.color(testkleur)
    t.setheading(0)
    t.goto(-200, 200)
    t.pendown()
    for teller in range(1, 5):
        t.forward(400)
        t.right(90)
    print(positie)