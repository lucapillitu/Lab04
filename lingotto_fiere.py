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
                line = l.strip()
                if not line:
                    continue
                if l[0].startswith("ST"):
                    continue
                elif l[0].startswith("ES"):
                    continue
                else:
                    continue

    def assegna_stand_a_espositore(self, codice_stand, codice_espositore):
        """Associa uno stand a un espositore"""
        # TODO

    def elenca_espositori(self):
        """Stampa l'elenco degli espositori mostrando, per ognuno, lo stand a cui è associato, quando applicabile """
        # TODO

    def stand_ordinati_per_prezzo(self):
        """Restituisce la lista ordinata degli stand in base al prezzo"""
        # TODO
