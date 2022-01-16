def main(commando):
    str(commando)
    # unicode look-alike check
    ala = ["а","ạ","ą","ä","à","á","ą"]
    cla = ["с","ƈ","ċ"]
    dla = ["ԁ","ɗ"]
    ela = ["е","ẹ","ė","é","è"]
    ila = ["і","í","ï"]
    jla = ["ј","ʝ"]
    lla = ["ӏ","ḷ"]
    ola = ["о","ο","օ","ȯ","ọ","ỏ","ơ","ó","ò","ö"]
    ula = ["υ","ս","ü","ú","ù"]
    vla = ["ν","ѵ"]
    xla = ["х","ҳ"]
    yla = ["у","ý"]
    zla = ["ʐ","ż"]
    commando = commando.replace(" ", "")
    for lookalike in ala:
        commando = commando.replace(lookalike, "a")
    for lookalike in cla:
        commando = commando.replace(lookalike, "c")
    for lookalike in dla:
        commando = commando.replace(lookalike, "d")
    for lookalike in ela:
        commando = commando.replace(lookalike, "e")
    commando = commando.replace("ġ", "g")
    commando = commando.replace("һ", "h")
    for lookalike in ila:
        commando = commando.replace(lookalike, "i")
    for lookalike in jla:
        commando = commando.replace(lookalike, "j")
    commando = commando.replace("κ", "k")
    for lookalike in lla:
        commando = commando.replace(lookalike, "l")
    commando = commando.replace("ո", "n")
    for lookalike in ola:
        commando = commando.replace(lookalike, "o")
    commando = commando.replace("р", "p")
    commando = commando.replace("զ", "q")
    commando = commando.replace("ʂ", "s")
    for lookalike in ula:
        commando = commando.replace(lookalike, "u")
    for lookalike in vla:
        commando = commando.replace(lookalike, "v")
    for lookalike in xla:
        commando = commando.replace(lookalike, "x")
    for lookalike in yla:
        commando = commando.replace(lookalike, "y")
    for lookalike in zla:
        commando = commando.replace(lookalike, "z")
    # maakt het allemaal hoofdletters
    commando = (str.upper(commando))
    commando = commando.encode("ascii", "ignore")
    return commando