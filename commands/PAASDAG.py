def main():
    import openeentranslate
    import openlandcode

    taal = openlandcode.openen()

    # jaartal
    print(openeentranslate.openen(taal, "jaartalwat"))
    jaartal = int(input())
    print(openeentranslate.openen(taal, "volgensgauss"))

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
        print(openeentranslate.openen(taal, "paasin"), jaartal, openeentranslate.openen(taal, "isop"), getal6, openeentranslate.openen(taal, "maart"))

    elif getal6 > 31:
        getal6 = getal6 - 31
        print(openeentranslate.openen(taal, "paasin"), jaartal, openeentranslate.openen(taal, "isop"), getal6, openeentranslate.openen(taal, "april"))

    else:
        print(openeentranslate.openen(taal, "error"), openeentranslate.openen(taal, "valtnietopmaartofapril"))