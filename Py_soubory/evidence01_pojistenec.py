class Pojistenec:

    def __init__(self, jmeno, prijmeni, vek, tel_cislo):
        self.jmeno = jmeno
        self.prijmeni = prijmeni
        self.vek = vek
        self.tel_cislo = tel_cislo


    def __str__(self):
        return f"{self.jmeno}, {self.prijmeni}, {self.vek}, {self.tel_cislo}"

    def vytvor_seznam(self):
        return [self.jmeno, self.prijmeni, self.vek, self.tel_cislo]
