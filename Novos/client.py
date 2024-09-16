from extrato import Extrato
from rent import Rent
from calculadora_extrato import CalculadoraDeExtrato
from extrato_formatter import ExtratoTextoFormatter, ExtratoHTMLFormatter


class Client:
    def __init__(self, nome):
        self.nome = nome
        self.tapes_alugadas = []

    def get_nome(self):
        return self.nome

    def adiciona_rent(self, rent):
        self.tapes_alugadas.append(rent)

    def gerar_extrato_html(self):
        extrato = Extrato(self.nome, self.tapes_alugadas, CalculadoraDeExtrato(
            self.tapes_alugadas), ExtratoHTMLFormatter())
        
        html_content = f"""
            <!DOCTYPE html>
            <html lang="pt-BR">
            <head>
                <meta charset="UTF-8">
                <meta name="viewport" content="width=device-width, initial-scale=1.0">
                <title>Página Gerada em Python</title>
            </head>
            <body>
                {extrato.gerar_extrato()}
            </body>
            </html>
            """

        with open("extrato.html", "w", encoding="utf-8") as file:
                file.write(html_content)

        return extrato.gerar_extrato()
    
    def gerar_extrato_text(self):
        extrato = Extrato(self.nome, self.tapes_alugadas, CalculadoraDeExtrato(
            self.tapes_alugadas), ExtratoTextoFormatter())
        return extrato.gerar_extrato()
