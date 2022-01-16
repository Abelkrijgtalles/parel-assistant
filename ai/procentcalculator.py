def main(commando):
    commando = str(commando)
    commands = ["ALLESONGTEKSTEN", "BOEK", "DATA", "FEITEN", "GAGILLEN", "LANDEN", "PAASDAG", "TEKENCORONA", "STOP"]
    procentpercommand = []
    for command in commands:
        bijelkaar = 0
        letters = []
        aantalletters = 0
        if commando == command:
            return command
        for letter in commando:
            letters.append(letter)
        for letter in command:
            if letter in letters:
                bijelkaar = bijelkaar + 100
            else:
                bijelkaar = bijelkaar + 0
            aantalletters = aantalletters + 1
        procentuiteindelijk = bijelkaar / aantalletters
        procentpercommand.append(procentuiteindelijk)
    positie = 0
    hoogtsteprocent = max(procentpercommand)
    for procent in procentpercommand:
        if procent == hoogtsteprocent:
            break
        else:
            positie = positie + 1
    if hoogtsteprocent > 69:
        return commands[positie]
    else:
        return 'NIKS'