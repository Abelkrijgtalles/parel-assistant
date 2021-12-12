def main():
    from openeentranslate import openen as op
    from openlandcode import openen as landc

    taal = landc()

    for n in range(50):
        print(op(taal, "help"))