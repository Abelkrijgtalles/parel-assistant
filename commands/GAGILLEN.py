def main():
    import openeentranslate
    import openlandcode

    taal = openlandcode.openen()

    for n in range(50):
        print(openeentranslate.openen(taal, "help"))