from evidence01_pojistenec import Pojistenec


class Evidence:

    def __init__(self):
        self.seznam_pojistencu = [["vaclav", "mrkev", 45, 789456123]]

    # pridani osoby na seznam

    def pridani_pojistence(self):

        while True:
            jmeno = input("zadejte jmeno: ").lower()
            if len(jmeno) >= 3 and jmeno.isalpha():
                break
            print("Jmeno musi mit alespon 3 znaky a nesmi obsahovat cisla.")

        while True:
            prijmeni = input("zadejte prijmeni: ").lower()
            if len(prijmeni) >= 3 and prijmeni.isalpha():
                break
            print("Prijmeni musi mit alespon 3 znaky a nesmi obsahovat cisla.")

        vek = None
        while True:
            try:
                vek = int(input("zadejte vek: "))
            except ValueError:
                print("Vek zadejte v cislech.")
            if vek is not None and (vek >= 1 and vek < 135):
                break
            else:
                print("Vek nemuze byt mensi nez 1 rok nebo vyssi nez 135 roku.")

        while True:
            tel_cislo = input("zadejte tel.cislo: ")
            if len(tel_cislo) == 9 and tel_cislo.isdigit():
                break
            print("Telefoni cislo musi mit 9 cislic.")

        pojistenec = Pojistenec(jmeno.title(), prijmeni.title(), vek, tel_cislo)
        self.seznam_pojistencu.append(pojistenec.vytvor_seznam())

        print("Databaze byla ulozena.", "\n")
        input("pokracujte stisknutim klavesy ENTER")

    # vypis vsech pojistenych

    def vypis_pojistencu(self):
        for x in self.seznam_pojistencu:
            polozka = x[0].ljust(10).title() + x[1].ljust(10).title() + str(x[2]).ljust(5) + str(x[3]).ljust(10)
            print(polozka)
        input("pokracujte stisknutim klavesy ENTER")

    # vyhledani pojisteneho

    # program projde seznam a pokud PRVEK []
    # obsahuje hledane jmeno a prijmeni, tak z nej vypise i vek a tel cislo.

    def vyhledat_pojistence(self):

        while True:
            hledane_jmeno = input("zadejte jmeno: ").lower()
            if len(hledane_jmeno) >= 3 and hledane_jmeno.isalpha():
                break
            print("Jmeno musi mit alespon 3 znaky a nesmi obsahovat cisla.")
        while True:
            hledane_prijmeni = input("zadejte prijmeni: ").lower()
            if len(hledane_prijmeni) >= 3 and hledane_prijmeni.isalpha():
                break
            print("Prijmeni musi mit alespon 3 znaky a nesmi obsahovat cisla.")

        nalezeno = False
        for jmeno, prijmeni, vek, tel_cislo in self.seznam_pojistencu:
            if jmeno == hledane_jmeno.title() and prijmeni == hledane_prijmeni.title():
                print(hledane_jmeno.title(), hledane_prijmeni.title(), vek, tel_cislo)
                nalezeno = True
        if not nalezeno:
            print("Tato osoba neni na seznamu")

        input("pokracujte stisknutim klavesy ENTER")

    # prochazeni pres while a kontrola zadani.)

    def spusteni(self):

        pokracovat = True
        while pokracovat:
            print("\nVyberte si akci: ")
            print("1 - Pridat noveho pojistneho")
            print("2 - Vypis vsech pojistnych")
            print("3 - Vyhledat pojisteneho")
            print("4 - Konec")
            try:
                volba = int(input("Zadejte cislo akce: "))
                if volba == 1:
                    self.pridani_pojistence()
                elif volba == 2:
                    self.vypis_pojistencu()
                elif volba == 3:
                    self.vyhledat_pojistence()
                elif volba == 4:
                    pokracovat = False
                else:
                    print("Zadej cislo od 1 do 4")
            except ValueError:
                print("Chybna volba, zadejte prosim pouze cislo od 1 do 4.")

        print("Program ukoncen")


