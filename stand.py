class Stand:
    def __init__(self, cod, sup, npad, prezzobase):
        self._cod = cod
        self._sup = sup
        self._npad = npad
        self._prezzobase = prezzobase
        self._disponibile = True
        self._assegnato = None


    def prezzo(self):
        return self._prezzobase

    def __str__(self):
        if self._disponibile:
              stato = "Disponibile"
        else: stato = "Non disponibile"
        return f"{self._cod}: {self._sup} mq - Padiglione {self._npad} - Prezzo {self.prezzo():.2f}€ - {stato}"

