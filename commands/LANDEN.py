def main():
    from openeentranslate import openen as op
    from openlandcode import openen as landc

    taal = landc

    print('Hier zijn ze')
    print(op(taal, "landen"))
