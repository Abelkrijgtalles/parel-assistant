def openen():
    import os
    with open(os.path.join("config", "welketaal.txt")) as welketaal:
        return str(welketaal.read())
