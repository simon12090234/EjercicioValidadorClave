from abc import ABC, abstractmethod
from errores import *


class ReglaValidacion(ABC):
    def init(self, longitud_esperada: int):
        self._longitud_esperada: int = longitud_esperada

    @abstractmethod
    def es_valida(self):
        pass

    def _validar_longitud(self, clave):
        count_1 = 0
        for i in clave:
            count_1 += 1

        if count_1 > self._longitud_esperada:
            return True

    def _contiene_mayuscula(self, clave):
        for item in clave:
            if item.isupper():
                return True
        return False

    def _contiene_minuscula(self, clave):
        for item in clave:
            if item.islower():
                return True
        return False

    def _contiene_numero(self, clave):
        for item in clave:
            if item.isdigit():
                return True
        return False



