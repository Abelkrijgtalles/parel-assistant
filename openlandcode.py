def openen():
    with open("config/welketaal.txt") as welketaal:
        yeet = str(welketaal.read())
        return yeet
