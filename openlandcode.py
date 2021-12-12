def openen():
    import os
    with open(os.path.join("config", "welketaal.txt")) as welketaal:
        yeet = str(welketaal.read())
        return yeet
