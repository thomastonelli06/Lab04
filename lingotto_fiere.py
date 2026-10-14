class LingottoFiere:
    def __init__(self, nome):
        """Inizializza gli attributi e le strutture dati"""
        self.__nome = nome
        self.__Stand = {}
        self.__Espositori = {}


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
        # TODO

    def assegna_stand_a_espositore(self, codice_stand, codice_espositore):
        """Associa uno stand a un espositore"""
        # TODO

    def elenca_espositori(self):
        """Stampa l'elenco degli espositori mostrando, per ognuno, lo stand a cui è associato, quando applicabile """
        # TODO

    def stand_ordinati_per_prezzo(self):
        """Restituisce la lista ordinata degli stand in base al prezzo"""
        # TODO
