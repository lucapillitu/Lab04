from contextlib import nullcontext
from os import WCONTINUED

import espositore


class Stand:
    def __init__(self,codice,superficie, padiglione,prezzobase,espositore, disponibilita):
        self.__codice = codice
        self.__superficie = superficie
        self.__padiglione = padiglione
        self.__prezzobase = prezzobase
        self.__espositore = ""
        self.__disponibilita = True

    @property
    def codice(self):
        return self.__codice
    @property
    def superficie(self):
        return self.__superficie
    @property
    def padiglione(self):
        return self.__padiglione
    @property
    def prezzobase(self):
        return self.__prezzobase
    @property
    def espositore(self):
        return self.__espositore
    @property
    def disponibilita(self):
        return self.__disponibilita

    @superficie.setter
    def superficie(self,superficie):
        self.__superficie = superficie
    @padiglione.setter
    def padiglione(self,padiglione):
        self.__padiglione = padiglione
    @prezzobase.setter
    def prezzobase(self,prezzobase):
        self.__prezzobase = prezzobase
    @espositore.setter
    def espositore(self,espositore):
        self.__espositore = espositore
    @disponibilita.setter
    def disponibilita(self,disponibilita):
        self.__disponibilita = disponibilita

    def __str__(self):
        return nullcontext

    def __repr__(self):
        return nullcontext
    def __eq__(self, other):
        return nullcontext

    def __ne__(self, other):
        return nullcontext


