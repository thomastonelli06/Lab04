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
        return f"{self._nome} : {len(self._Stand)} {len(self._Espositori)}"

    """Aggiungere setter e getter se necessari"""
    @property
    def nome(self):
            return self._nome
    @nome.setter
    def nome(self, newName):
            self._nome = newName



    def carica_file_dati(self, file_path):
        """Carica i dati (stand ed espositori) dal file"""


            try:
                with open(file_path) as file:
                    for line in file:
                        campi = line.strip().split(",")
                        codice = campi[0]

                        if codice.startswith("ES"):
                            espositore = Espositore(codice, campi[1], campi[2])
                            self._Espositori[codice] = espositore

                        elif len(campi) == 4:  # standard
                            stand = Stand(codice, campi[1], campi[2], float(campi[3]))
                            self._Stand[codice] = stand

                        elif campi[4].isdigit():
                            standElettr = StandConPrese(codice, campi[1], campi[2], float(campi[3]), int(campi[4]))
                            self._Stand[codice] = standElettr

                        elif campi[4].isalpha():
                            standPr = StandPremium(codice, campi[1], campi[2], float(campi[3]), campi[4])
                            self._Stand[codice] = standPr

            except FileNotFoundError:
                raise






    def assegna_stand_a_espositore(self, codice_stand, codice_espositore):
        """Associa uno stand a un espositore"""

        if codice_stand not in self._Stand:
            raise ValueError("niente codice valido")

        if codice_espositore not in self._Espositori:
            raise ValueError("niente codice valido")

        if not self._Stand[codice_stand]._disponibile:
            raise ValueError("Stand nodisponibile")

        if self._Espositori[codice_espositore]._proprieta is not None:
            raise ValueError("Espositore già associato a uno stand")


        self._Stand[codice_stand]._disponibile = False
        self._Stand[codice_stand]._assegnato = self._Espositori[codice_espositore]
        self._Espositori[codice_espositore]._proprieta = self._Stand[codice_stand]




    def elenca_espositori(self):
        """Stampa l'elenco degli espositori mostrando, per ognuno, lo stand a cui è associato, quando applicabile """
        for espositore in self._Espositori:
            if self._Espositori[espositore]._proprieta is not None:
                 print(f"{espositore}, --- {self._Espositori[espositore]._proprieta} assegnato")
            else: print(f"{espositore}")

    def stand_ordinati_per_prezzo(self):
        """Restituisce la lista ordinata degli stand in base al prezzo"""
        # TODO
