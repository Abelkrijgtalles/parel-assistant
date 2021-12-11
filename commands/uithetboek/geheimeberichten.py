def main():
    from tkinter import messagebox, simpledialog, Tk
    from random import choice

    def is_even(getal):
        return getal % 2 == 0

    def ontvang_even_letters(bericht):
        even_letters = []
        for teller in range(0, len(bericht)):
            if is_even(teller):
                even_letters.append(bericht[teller])
        return even_letters

    def ontvang_oneven_letters(bericht):
        oneven_letters = []
        for teller in range(0, len(bericht)):
            if not is_even(teller):
                oneven_letters.append(bericht[teller])
        return oneven_letters

    def wissel_letters(bericht):
        letter_lijst = []
        if not is_even(len(bericht)):
            bericht = bericht + "x"
        even_letters = ontvang_even_letters(bericht)
        oneven_letters = ontvang_oneven_letters(bericht)
        for teller in range(0, int(len(bericht) /2)):
            letter_lijst.append(oneven_letters[teller])
            letter_lijst.append(even_letters[teller])
        nieuw_bericht = "".join(letter_lijst)
        return nieuw_bericht

    def coderen(bericht):
        gecodeerde_lijst = []
        valse_letters = ["a", "b", "c", "d", "e", "f", "g", "i", "r", "s", "t", "u", "v"]
        for teller in range(0, len(bericht)):
            gecodeerde_lijst.append(bericht[teller])
            gecodeerde_lijst.append(choice(valse_letters))
        nieuw_bericht = "".join(gecodeerde_lijst)
        gecodeerd_bericht = "".join(reversed(nieuw_bericht))
        gecodeerd_bericht = wissel_letters(gecodeerd_bericht)
        return gecodeerd_bericht

    def decoderen(bericht):
        gedecodeerd_bericht = wissel_letters(bericht)
        niet_omgedraaid_bericht = "".join(reversed(gedecodeerd_bericht))
        even_letters = ontvang_even_letters(niet_omgedraaid_bericht)
        nieuw_bericht = "".join(even_letters)
        return nieuw_bericht

    def ontvang_taak():
        taak = simpledialog.askstring("Taak", "Wil je coderen of decoderen")
        return taak

    def ontvang_bericht():
        bericht = simpledialog.askstring("Bericht", "Voer het geheime bericht in :")
        return bericht

    root = Tk()

    while True:
        taak = ontvang_taak()
        if taak == "coderen":
            bericht = ontvang_bericht()
            gecodeerd = coderen(bericht)
            messagebox.showinfo("Het beveiligde bericht is:", gecodeerd)
            print(gecodeerd)
        elif taak == "decoderen":
            bericht = ontvang_bericht()
            gedecodeerd = decoderen(bericht)
            messagebox.showinfo("Dit was het:", gedecodeerd)
            print(gedecodeerd)
        else:
            break
    root.mainloop()