def main():
    import turtle as t

    def rechthoek(horizontaal, verticaal, kleur):
        t.pendown()
        t.pensize(1)
        t.color(kleur)
        t.begin_fill()
        for teller in range(1, 3):
            t.forward(horizontaal)
            t.right(90)
            t.forward(verticaal)
            t.right(90)
        t.end_fill()
        t.penup()

    def arm(kleur):
        t.pendown()
        t.begin_fill()
        t.color(kleur)
        t.forward(60)
        t.right(90)
        t.forward(50)
        t.right(90)
        t.forward(10)
        t.right(90)
        t.forward(40)
        t.left(90)
        t.forward(50)
        t.right(90)
        t.forward(10)
        t.end_fill()
        t.penup()
        t.setheading(0)

    t.penup()
    t.speed("slow")
    t.bgcolor("Dodger blue")

    # voeten
    t.goto(-100, -150)
    rechthoek(50, 20, "blue")
    t.goto(-30, -150)
    rechthoek(50, 20, "blue")

    # benen
    t.goto(-25, -50)
    rechthoek(15, 100, "grey")
    t.goto(-55, -50)
    rechthoek(-15, 100, "grey")

    # lichaam
    t.goto(-90, 100)
    rechthoek(100, 150, "red")

    # armen
    t.goto(-90, 85)
    t.setheading(180)
    arm("light blue")

    t.goto(-90, 20)
    t.setheading(180)
    arm("purple")

    t.goto(10, 85)
    t.setheading(0)
    arm("goldenrod")

    # nek
    t.goto(-50, 120)
    rechthoek(15, 20, "grey")

    # hoofd
    t.goto(-85, 170)
    rechthoek(80, 50, "red")

    #ogen
    t.goto(-60, 160)
    rechthoek(30, 10, "white")
    t.goto(-60, 160)
    rechthoek(5, 5, "black")
    t.goto(-45, 155)
    rechthoek(5, 5, "black")

    # mond
    t.goto(-65, 135)
    t.right(5)
    rechthoek(40, 5, "black")

    t.hideturtle()