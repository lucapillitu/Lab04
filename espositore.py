class Espositore:
    def __init__(self, codice, nome, cognome):
        self.__codice = codice
        # senza i __ → passano dai setter, quindi vengono controllati
        self.nome = nome
        self.cognome = cognome
        self.__stand = None


    @property
    def codice(self):          # sola lettura: nessun setter
        return self.__codice

    @property
    def nome(self):
        return self.__nome

    @property
    def cognome(self):
        return self.__cognome

    @property
    def stand(self):
        return self.__stand


    @nome.setter
    def nome(self, valore):
        if not valore.strip():
            raise ValueError("Nome espositore non valido")
        self.__nome = valore.strip()

    @cognome.setter
    def cognome(self, valore):
        if not valore.strip():
            raise ValueError("Cognome espositore non valido")
        self.__cognome = valore.strip()

    @stand.setter
    def stand(self, stand):
        self.__stand = stand

    def __str__(self):
        if self.__stand is not None:
            assegnato = self.__stand.codice
        else :
            assegnato = "nessuno stand assegnato"
        return f"{self.__codice}: '{self.__nome} {self.__cognome}' - Stand: {assegnato}"

    def __repr__(self):
        return f"Espositore({self.__codice!r}, {self.__nome!r}, {self.__cognome!r})"

    def __eq__(self, other):
        # due espositori sono uguali se hanno lo stesso codice
        if not isinstance(other, Espositore):#controlla siano lo stesso tipo di oggetto py
            return ValueError
        return self.__codice == other.codice