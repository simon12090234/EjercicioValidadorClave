from abc import ABC, abstractmethod
from errores import *

class ReglaValidacion(ABC):
    def init(self, longitud_esperada: int):
        self._longitud_esperada: int = longitud_esperada


    @abstractmethod
    def es_valida(self):
        pass
    def _validar_longitud(self, clave):
        try:
            if len(clave) > self._longitud_esperada:
                return True

            else:
                raise NoCumpleLongitudMinimaError

        except():
            pass