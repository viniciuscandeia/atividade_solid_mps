from valor_calculo import ValorCalculo, NormalCalculo, InfantilCalculo, LancamentoCalculo
from calculadora_pontos import CalculadoraDePontos, CalculadoraDePontosNormal, CalculadoraDePontosLancamento, CalculadoraDePontosInfantil
from enum import Enum
from abc import ABC

class TapeType(Enum):
    NORMAL = 0
    LANCAMENTO = 1
    INFANTIL = 2

class GerenciadorDeTapes():
    def __init__(self, 
                 type: TapeType = TapeType.NORMAL,
                 calculadora_pontos:CalculadoraDePontos = CalculadoraDePontosNormal,
                 calculadora_aluguel: ValorCalculo = NormalCalculo
                 ) -> None:
        self._calculadora_pontos = calculadora_pontos
        self._calculadora_aluguel = calculadora_aluguel
    
    def calcular_pontos(self, dias_alugada:int):
        return self._calculadora_pontos.calcular(dias_alugada)
    
    def calcular_custo_aluguel(self, dias_alugada: int):
        return self._calculadora_aluguel.calcular(dias_alugada)
    
class GerenciadorDeTapesNormal(GerenciadorDeTapes):
    def __init__(self) -> None:
        super().__init__(type=TapeType.NORMAL, calculadora_pontos=CalculadoraDePontosNormal(), calculadora_aluguel=NormalCalculo())

class GerenciadorDeTapesLancamento(GerenciadorDeTapes):
    def __init__(self) -> None:
        super().__init__(type=TapeType.LANCAMENTO, calculadora_pontos=CalculadoraDePontosLancamento(), calculadora_aluguel=LancamentoCalculo())

class GerenciadorDeTapesInfantil(GerenciadorDeTapes):
    def __init__(self) -> None:
        super().__init__(type=TapeType.INFANTIL, calculadora_pontos=CalculadoraDePontosInfantil(), calculadora_aluguel=InfantilCalculo())


class Tape:
    def __init__(self, titulo: str, gerenciadorDeTapes:GerenciadorDeTapes) -> None:
        self.titulo: str = titulo
        self._gerenciadorDeTapes = gerenciadorDeTapes

    def get_titulo(self) -> str:
        return self.titulo

    def mudarTipo(self, novoGerenciamento:GerenciadorDeTapes):
        self._gerenciadorDeTapes = novoGerenciamento
    
    def calcular_custo_aluguel(self, numeroDias:int) -> int:
        return self._gerenciadorDeTapes.calcular_custo_aluguel(numeroDias)
    
    def calcular_pontos(self, numeroDias: int) -> int:
        return self._gerenciadorDeTapes.calcular_pontos(numeroDias)
