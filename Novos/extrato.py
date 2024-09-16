from rent import Rent
from calculadora_extrato import CalculadoraDeExtrato
from extrato_formatter import ExtratoFormatter

class Extrato:
    def __init__(self, nome: str, alugueis: list[Rent], calculadora_extrato: CalculadoraDeExtrato, extrato_formatter: ExtratoFormatter):
        self.nome: str = nome
        self.alugueis: list[Rent] = alugueis
        self.calculadora_extrato: CalculadoraDeExtrato = calculadora_extrato
        self.extrato_formatter: ExtratoFormatter = extrato_formatter

    def gerar_extrato(self) -> str:
        valor_total = self.calculadora_extrato.calcular_valor_total()
        pontos_de_alugador_frequente = self.calculadora_extrato.calcular_pontos_totais()
        return self.extrato_formatter.formatar_extrato(self.nome, self.alugueis, valor_total, pontos_de_alugador_frequente)
