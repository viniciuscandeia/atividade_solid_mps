from abc import ABC, abstractmethod


class CalculadoraDePontos(ABC):
    @abstractmethod
    def calcular(self, dias_alugada: int):
        pass


class CalculadoraDePontosNormal(CalculadoraDePontos):
    def calcular(self, dias_alugada: int):
        return 1


class CalculadoraDePontosLancamento(CalculadoraDePontos):
    def calcular(self, dias_alugada: int):
        pontos = 1
        if dias_alugada > 1:
            pontos += 1
        return pontos


class CalculadoraDePontosInfantil(CalculadoraDePontos):
    def calcular(self, dias_alugada: int):
        return 1
