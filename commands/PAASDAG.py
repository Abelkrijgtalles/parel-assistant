def main():
    # jaartal
    jaartal = int(input("Wat is het jaartal"))
    print("Deze berekening is volgens het recept van Gauss")

    # getal1
    getal1 = jaartal % 19
    getal1 = 19 * getal1 + 24
    getal1 = getal1 % 30

    # getal2
    getal2 = jaartal % 7

    # getal3
    getal3 = jaartal % 7

    # getal4
    getal4 = 6 * getal1 + 4 * getal2 + 2 * getal3 + 5

    # getal5
    getal5 = getal4 % 7

    # getal6
    getal6 = getal1 + getal5 + 22

    if getal6 < 32:
        print("Paas in", jaartal, "is op", getal6, "maart")

    elif getal6 > 31:
        getal6 = getal6 - 31
        print("Paas in", jaartal, "is op", getal6, "april")

    else:
        print("Error. Code Jaar ")