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



    def assegna_stand_a_espositore(self, codice_stand, codice_espositore):
        """Associa uno stand a un espositore"""
        # TODO

    def elenca_espositori(self):
        """Stampa l'elenco degli espositori mostrando, per ognuno, lo stand a cui è associato, quando applicabile """
        # TODO

    def stand_ordinati_per_prezzo(self):
        """Restituisce la lista ordinata degli stand in base al prezzo"""
        # TODO
