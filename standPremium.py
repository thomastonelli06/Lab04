from stand import Stand

class StandPremium(Stand):
    def __init__(self, cod, sup, npad, prezzobase, ingresso):
        super().__init__(cod, sup, npad, prezzobase)
        self._ingresso = ingresso

    def prezzo(self):
        return self._prezzobase * 1.30

    def __str__(self):
        return f"{super().__str__()} - {self._ingresso}"