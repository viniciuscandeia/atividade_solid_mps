from abc import ABC, abstractmethod


class ValorCalculo(ABC):
    @abstractmethod
    def calcular(self, dias_alugada: int):
        pass


class NormalCalculo(ValorCalculo):
    def calcular(self, dias_alugada: int):
        valor = 2
        if dias_alugada > 2:
            valor += (dias_alugada - 2) * 1.5
        return valor


class LancamentoCalculo(ValorCalculo):
    def calcular(self, dias_alugada: int):
        return dias_alugada * 3


class InfantilCalculo(ValorCalculo):
    def calcular(self, dias_alugada: int):
        valor = 1.5
        if dias_alugada > 3:
            valor += (dias_alugada - 3) * 1.5
        return valor
