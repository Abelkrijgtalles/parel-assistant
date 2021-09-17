def open():
    with open("welketaal.txt") as welketaal:
        return str(welketaal.read())
