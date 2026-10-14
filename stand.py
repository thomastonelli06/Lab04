class Stand:
    def __init__(self, codice, superficie, padiglione, prezzoIniziale):
        self.__codice = codice
        self.__superficie = superficie
        self.__padiglione = padiglione
        self.__prezzoIniziale = prezzoIniziale
        self.__espositore = None


    def prezzoFinale(self):
        return self._prezzoIniziale

    def __str__(self):
       return f"{self.__codice}: {self.__superficie} mq, n:{self.__padiglione}, {self.__prezzoFinale} euro"

# definisco classi figlie:

class StandConPrese(Stand):
    def __init__(self, codice, superficie, padiglione, prezzoIniziale, numPrese):
        super().__init__(codice, superficie, padiglione, prezzoIniziale)

        self.__numPrese = numPrese

    def prezzoFinale(self):
        return self.__prezzoIniziale * (1 + 0.07 * self.__numPrese)

    def __str__(self):
        return f"({super().__str__()}" f"{self.__numPrese} prese"