class Stand:
    def __init__(self, cod, sup, npad, prezzobase):
        self._cod = cod
        self._sup = sup
        self._npad = npad
        self._prezzobase = prezzobase
        self._disponibile = True
        self._assegnato = None

    def __str__(self):
        return f"{self._cod} - {self._sup} - {self._npad} - {self._prezzobase}"

