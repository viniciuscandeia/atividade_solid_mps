from rent import Rent


class CalculadoraDeExtrato:
    def __init__(self, alugueis: list[Rent]):
        self.alugueis = alugueis

    def calcular_valor_total(self) -> float:
        valor_total = 0.0
        for rent in self.alugueis:
            valor_total += rent.get_custo_aluguel()
        return valor_total

    def calcular_pontos_totais(self) -> int:
        pontos_total = 0
        for rent in self.alugueis:
            pontos_total += rent.get_pontos_de_alugador()
        return pontos_total
