from abc import ABC, abstractmethod
from rent import Rent


# Interface para diferentes estratégias de formatação
class ExtratoFormatter(ABC):
    @abstractmethod
    def formatar_extrato(self, nome: str, alugueis: list[Rent], valor_total: float, pontos: int) -> str:
        pass


# Implementação de extrato como string
class ExtratoTextoFormatter(ExtratoFormatter):
    def formatar_extrato(self, nome: str, alugueis: list[Rent], valor_total: float, pontos: int) -> str:
        fim_de_linha = "\n"
        resultado = f"Registro de Alugueis de {nome}{fim_de_linha}"

        for rent in alugueis:
            valor_corrente = rent.get_custo_aluguel()
            resultado += f"\t{rent.get_tape().get_titulo()}\t{valor_corrente}{fim_de_linha}"

        resultado += f"Valor total devido: {valor_total}{fim_de_linha}"
        resultado += f"Você acumulou {pontos} pontos de alugador frequente"
        return resultado


# Implementação de extrato como HTML
class ExtratoHTMLFormatter(ExtratoFormatter):
    def formatar_extrato(self, nome: str, alugueis: list[Rent], valor_total: float, pontos: int) -> str:
        resultado = f"<h1>Registro de Alugueis de {nome}</h1><ul>"

        for rent in alugueis:
            valor_corrente = rent.get_custo_aluguel()
            resultado += f"<li>{rent.get_tape().get_titulo()}: {valor_corrente}</li>"

        resultado += f"</ul><p>Valor total devido: {valor_total}</p>"
        resultado += f"<p>Você acumulou {pontos} pontos de alugador frequente</p>"
        return resultado
