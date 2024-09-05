class Film:
    def __init__(self) -> None:
        self._tytul = ""
        self.liczbaW = 0
    def SetTytul(self, t):
        self._tytul = t
    def GetTytul(self):
        return self._tytul
    def GetLiczbaW(self):
        return self.liczbaW
    def UppLiczbaW(self):
        self.liczbaW+=1

film1 = Film()
film1.SetTytul("obcy")
print(film1.GetTytul())
print(film1.GetLiczbaW())
film1.UppLiczbaW()
print(film1.GetLiczbaW())