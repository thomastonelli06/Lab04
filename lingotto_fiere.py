from asyncio.windows_events import NULL

from stand import Stand
from standConPrese import StandConPrese
from standPremium import StandPremium
from espositore import Espositore

class LingottoFiere:
    def __init__(self, nome):
        """Inizializza gli attributi e le strutture dati"""
        self._nome = nome
        self._Stand = {}
        self._Espositori = {}


    def __str__(self):
        return f"{self.__nome} : {len(self.__Stand)} {len(self.__Espositori)}"

    """Aggiungere setter e getter se necessari"""
    @property
    def nome(self):
            return self.__nome
    @nome.setter
    def nome(self, newName):
            self.__nome = newName



    def carica_file_dati(self, file_path):
        """Carica i dati (stand ed espositori) dal file"""
        with open(file_path) as file:
            for line in file:
                campi = line.strip().split()
                codice = campi[0]
                if codice.startswith("ES"):

                    espositore = Espositore(codice, campi[1], campi[2])
                    self._Espositori[codice] = espositore
                elif len(campi) == 4:    #standard
                    stand = Stand(codice, campi[1], campi[2], campi[3])
                    self._Stand[codice] = stand
                elif campi[4].isdigit():
                    standElettr = StandConPrese(codice,campi[1], campi[2] ,campi[3],campi[4])
                    self._Stand[codice] = stand
                elif campi[4].isalpha():
                    standPr = StandPremium(codice, campi[1], campi[2],campi[3],campi[4])
                    self._Stand[codice] = stand






    def assegna_stand_a_espositore(self, codice_stand, codice_espositore):
        """Associa uno stand a un espositore"""
        # TODO

    def elenca_espositori(self):
        """Stampa l'elenco degli espositori mostrando, per ognuno, lo stand a cui è associato, quando applicabile """
        # TODO

    def stand_ordinati_per_prezzo(self):
        """Restituisce la lista ordinata degli stand in base al prezzo"""
        # TODO
