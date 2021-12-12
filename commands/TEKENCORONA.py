def main():
    import turtle as t
    from openeentranslate import openen as op
    from openlandcode import openen as landc

    taal = landc()

    print(op(taal, "nieuwvenster"))
    t.color('green')
    t.bgcolor('black')
    t.speed(11)
    t.hideturtle()
    b = 0
    while b < 200:
        t.right(b)
        t.forward(b * 3)
        b = b + 1    