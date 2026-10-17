from stand import Stand

class StandConPrese(Stand):
    def __init__(self, cod, sup, npad, prezzobase, nprese):
        super().__init__(cod, sup, npad, prezzobase)
        self._nprese = nprese

    def prezzo(self):

        return self._prezzobase * (1 + 0.07 * self._nprese)


    def __str__(self):
        return f"{super().__str__()} - n.prese:{self._nprese}"

