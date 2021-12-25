def main():
    from openeentranslate import openen as op
    from openlandcode import openen as landc

    taal = landc

    # jaartal
    print(op(taal, "jaartalwat"))
    jaartal = int(input())
    print(op(taal, "volgensgauss"))

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
        print(op(taal, "paasin"), jaartal, op(taal, "isop"), getal6, op(taal, "maart"))

    elif getal6 > 31:
        getal6 = getal6 - 31
        print(op(taal, "paasin"), jaartal, op(taal, "isop"), getal6, op(taal, "april"))

    else:
        print(op(taal, "error"), op(taal, "valtnietopmaartofapril"))