def main(commando):
    import ai.filterding as filterding
    import ai.procentcalculator as procentcalculator
    commando = filterding.main(commando)
    commando = procentcalculator.main(commando)
    return commando