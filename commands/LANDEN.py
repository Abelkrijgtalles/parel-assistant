def main():
    import openeentranslate
    import openlandcode

    taal = openlandcode.openen()

    print(openeentranslate.openen(taal, "hierlanden"))
    print(openeentranslate.openen(taal, "landen"))
