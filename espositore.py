class Espositore:
    def __init__(self,codE, nome,cognome):
        self._codE = codE
        self._nome = nome
        self._cognome = cognome
        self._proprieta = None


    def __str__(self):
        return f"{self._codE} - {self._nome} - {self._cognome}"