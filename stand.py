class Stand:
    def __init__(self, codice, superficie, padiglione, prezzobase):
        self.__codice = codice
        self.__superficie = superficie
        self.__padiglione = padiglione
        self.__prezzobase = prezzobase
        self.__espositore = None

    @property
    def codice(self):
        return self.__codice

    @property
    def superficie(self):
        return self.__superficie

    @superficie.setter
    def superficie(self, superficie):
        self.__superficie = superficie

    @property
    def padiglione(self):
        return self.__padiglione

    @padiglione.setter
    def padiglione(self, padiglione):
        self.__padiglione = padiglione

    @property
    def prezzobase(self):
        return self.__prezzobase

    @prezzobase.setter
    def prezzobase(self, prezzobase):
        self.__prezzobase = prezzobase

    @property
    def prezzo(self):
        # stand Standard: prezzo finale = prezzo base
        return self.__prezzobase

    @property
    def espositore(self):
        return self.__espositore

    @espositore.setter
    def espositore(self, espositore):
        self.__espositore = espositore



    def __str__(self):
        return {f"{self.codice}: Standard | {self.superficie} mq - Padiglione {self.padiglione} - "
                f"Prezzo {self.prezzo:.2f}€ - espositore : {self.espositore}"}

    def __repr__(self):
        return f"Stand({self.codice!r}, {self.superficie}, {self.padiglione}, {self.prezzobase})"

    def __eq__(self, other):
        # due stand sono uguali se hanno lo stesso codice
        if not isinstance(other, Stand):
            return ValueError
        return self.codice == other.codice



# sottoclassi di Stand

class StandPreseExtra(Stand):
    def __init__(self, codice, superficie, padiglione, prezzobase, prese):
        super().__init__(codice, superficie, padiglione, prezzobase)
        self.__prese = prese

    @property
    def prese(self):
        return self.__prese

    @property
    def prezzo(self):
        return self.prezzobase * (1 + 0.07 * self.__prese)

    def __str__(self):
        return (f"{self.codice}: Prese Extra | {self.superficie} mq - Padiglione {self.padiglione} - "
                f"Prezzo {self.prezzo:.2f}€ - Prese aggiuntive: {self.__prese} - espositore : {self.espositore}")

    def __repr__(self):
        return (f"StandPreseExtra({self.codice!r}, {self.superficie}, {self.padiglione}, "
                f"{self.prezzobase}, {self.__prese})")


class StandPremium(Stand):
    def __init__(self, codice, superficie, padiglione, prezzobase, posizione):
        super().__init__(codice, superficie, padiglione, prezzobase)
        self.__posizione = posizione

    @property
    def posizione(self):
        return self.__posizione

    @property
    def prezzo(self):
        return self.prezzobase * 1.30

    def __str__(self):
        return {f"{self.codice}: Premium | {self.superficie} mq - Padiglione {self.padiglione} - "
                f"Prezzo {self.prezzo:.2f}€ - Posizione: {self.__posizione} - espositore {self.espositore}"}

    def __repr__(self):
        return (f"StandPremium({self.codice!r}, {self.superficie}, {self.padiglione}, "
                f"{self.prezzobase}, {self.__posizione!r})")