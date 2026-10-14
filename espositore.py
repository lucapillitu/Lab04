class Espositore:
    def __init__(self, codice, nome, cognome):
        self.__codice = codice
        # senza "__" → passano dai setter, quindi vengono controllati
        self.nome = nome
        self.cognome = cognome
        self.__stand = None

    @property
    def codice(self):          # sola lettura: nessun setter
        return self.__codice

    @property
    def nome(self):
        return self.__nome

    @nome.setter
    def nome(self, valore):
        if not valore.strip():
            raise ValueError("Nome espositore non valido")
        self.__nome = valore.strip()

    @property
    def cognome(self):
        return self.__cognome

    @cognome.setter
    def cognome(self, valore):
        if not valore.strip():
            raise ValueError("Cognome espositore non valido")
        self.__cognome = valore.strip()

    @property
    def stand(self):
        return self.__stand

    @stand.setter
    def stand(self, stand):
        self.__stand = stand

    def __str__(self):
        assegnato = self.__stand.codice if self.__stand is not None else "nessuno stand"
        return f"{self.__codice}: {self.__nome} {self.__cognome} - Stand: {assegnato}"

    def __repr__(self):
        return f"Espositore({self.__codice!r}, {self.__nome!r}, {self.__cognome!r})"

    def __eq__(self, other):
        # due espositori sono uguali se hanno lo stesso codice
        if not isinstance(other, Espositore):
            return NotImplemented
        return self.__codice == other.codice

    def __hash__(self):
        return hash(self.__codice)