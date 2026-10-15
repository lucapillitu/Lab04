import stand
from stand import Stand,StandPremium,StandPreseExtra
from espositore import Espositore


class LingottoFiere:
    def __init__(self, nome):
        self.__nome = nome.strip()
        self.stand = []
        self.espositori = []


    @property
    def nome(self):
        return self.__nome
    @nome.setter
    def nome(self, value):
        if not value.strip():
            raise ValueError("Nome non valido")
        self.__nome = value.strip()

#caricamento da file
    def carica_file_dati(self, file_path):
        with open(file_path, "r") as file:

            for l in file:
                line = l.strip().split(",")

                if line[0].startswith("ST"):
                    if len(line) == 4:
                        self.stand.append(Stand(line[0],int(line[1]),int(line[2]),int(line[3])))
                    elif len(line) == 5 and line[4].isdigit():
                        self.stand.append(StandPreseExtra(line[0],int(line[1]),int(line[2]),int(line[3]),int(line[4])))
                    elif len(line) == 5 and not line[4].isdigit():
                        self.stand.append(StandPremium(line[0],int(line[1]),int(line[2]),int(line[3]),line[4]))

                elif line[0].startswith("ES") and len(line) == 3:
                    self.espositori.append(Espositore(line[0],line[1],line[2]))

#metodi per associare stand a espositore
    def cerca_stand(self, codice):
        for s in self.stand:
            if s.codice == codice:
                return s
        raise ValueError(f"Stand {codice} non trovato")

    def cerca_espositore(self, codice):
        for e in self.espositori:
            if e.codice == codice:
                return e
        raise ValueError(f"Espositore {codice} non trovato")

    def assegna_stand_a_espositore(self, codice_stand, codice_espositore):

        s = self.cerca_stand(codice_stand)
        e = self.cerca_espositore(codice_espositore)

        if s.espositore is not None:
            raise ValueError(f"Stand {codice_stand} occupato")
        if e.stand is not None:
            raise ValueError(f"Espositore {codice_espositore} ha già uno stand")

        s.espositore = e
        e.stand = s


    def elenca_espositori(self):
        for e in self.espositori:
            print(e.__str__())


    def stand_ordinati_per_prezzo(self):
        return sorted(self.stand, key=lambda s: s.prezzo, reverse=False)


