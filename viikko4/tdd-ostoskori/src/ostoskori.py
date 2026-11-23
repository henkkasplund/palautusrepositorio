from tuote import Tuote
from ostos import Ostos

class Ostoskori:
    def __init__(self):
        self._ostokset = []

    def tavaroita_korissa(self):
        return sum(ostos.lukumaara() for ostos in self._ostokset)

    def hinta(self):
        return sum(ostos.hinta() for ostos in self._ostokset)

    def _hae_ostos(self, tuote: Tuote):
        for ostos in self._ostokset:
            if ostos.tuote is tuote:
                return ostos
        return None

    def lisaa_tuote(self, lisattava: Tuote):
        ostos = self._hae_ostos(lisattava)
        if ostos is not None:
            ostos.muuta_lukumaaraa(1)
            return
        self._ostokset.append(Ostos(lisattava))

    def poista_tuote(self, poistettava: Tuote):
        ostos = self._hae_ostos(poistettava)
        if ostos is not None:
            ostos.muuta_lukumaaraa(-1)
            if ostos.lukumaara() == 0:
                self._ostokset.remove(ostos)

    def tyhjenna(self):
        self._ostokset.clear()

    def ostokset(self):
        return self._ostokset
