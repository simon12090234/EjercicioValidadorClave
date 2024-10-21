from abc import ABC, abstractmethod
from validadorclave.modelo.errores import *


class ReglaValidacion(ABC):

    def __init__(self, longitud_esperada: int):
        self._longitud_esperada: int = longitud_esperada

    def _validar_longitud(self, clave: str) -> bool:
        return len(clave) > self._longitud_esperada

    def _contiene_mayuscula(self, clave):
        for Letra in clave:
            if Letra.isupper():
                return True
        return False

    def _contiene_minuscula(self, clave):
        for Letra in clave:
            if Letra.islower():
                return True
        return False

    def _contiene_numero(self, clave):
        for Letra in clave:
            if Letra.isdigit():
                return True
        return False

    @abstractmethod
    def es_valida(self, clave):
        pass

class ReglaValidacionGanimedes(ReglaValidacion):

    def __init__(self):
        super().__init__(longitud_esperada=8)

    def contiene_caracter_especial(self, clave: str) -> bool:
        especial = "@_#$%"
        for i in especial:
            if i in clave:
                return True
        return False

    def es_valida(self, clave: str) -> bool:
        if not self._validar_longitud(clave):
            raise NoCumpleLongitudMinimaError()

        if not self._contiene_mayuscula(clave):
            raise NoTieneLetraMayusculaError()

        if not self._contiene_minuscula(clave):
            raise NoTieneLetraMinusculaError()

        if not self._contiene_numero(clave):
            raise NoTieneNumeroError()

        if not self.contiene_caracter_especial(clave):
            raise NoTieneCaracterEspecialError()

        return True

class ReglaValidacionCalisto(ReglaValidacion):

    def __init__(self):
        super().__init__(longitud_esperada=6)

    def contiene_calisto(self, clave: str) -> bool:
        palabra = "calisto"
        clave_temp: str = clave.lower()
        calisto_index = 0
        while calisto_index < len(clave):
            calisto_index = clave_temp.find(palabra, calisto_index)
            # Si encontro la palabra
            if calisto_index > -1:
                pi = calisto_index  #posiicion incial
                pf = calisto_index + len(palabra) #posicion final
                calisto_str = clave[pi:pf]

                contador_mayusculas = 0
                for letra in calisto_str:
                    if letra.isupper():
                        contador_mayusculas += 1

                if 2 <= contador_mayusculas < len(palabra):
                    return True
                else:
                    #aca participe yo
                    calisto_index = pf
            else:
                return False

        return False


    def es_valida(self, clave: str) -> bool:
        if not self._validar_longitud(clave):
            raise NoCumpleLongitudMinimaError()

        if not self._contiene_numero(clave):
            raise NoTieneNumeroError()

        if not self.contiene_calisto(clave):
            raise NoTienePalabraSecretaError()

        return True

class Validador:

    def __init__(self, regla: ReglaValidacion):
        self.regla: ReglaValidacion = regla

    def es_valida(self, clave: str) -> bool:
        return self.regla.es_valida(clave)




