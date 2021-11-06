def openen():
    with open("config/welketaal.txt") as welketaal:
        return str(welketaal.read())
