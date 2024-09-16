from client import Client
from rent import Rent
from tape import Tape, GerenciadorDeTapesInfantil, GerenciadorDeTapesLancamento, GerenciadorDeTapesNormal
from valor_calculo import *
from calculadora_pontos import *

if __name__ == "__main__":
    pass
    c1 = Client("Juliana")

    t1 = Tape("O Exorcista", gerenciadorDeTapes=GerenciadorDeTapesNormal())
    t1.mudarTipo(novoGerenciamento=GerenciadorDeTapesInfantil())

    c1.adiciona_rent(Rent(Tape("O Exorcista", gerenciadorDeTapes=GerenciadorDeTapesNormal()), 3))
    c1.adiciona_rent(Rent(Tape("Men in Black", gerenciadorDeTapes=GerenciadorDeTapesNormal()), 2))
    c1.adiciona_rent(Rent(Tape("Jurassic Park III", gerenciadorDeTapes=GerenciadorDeTapesNormal()), 3))
    c1.adiciona_rent(Rent(Tape("Planeta dos Macacos", gerenciadorDeTapes=GerenciadorDeTapesLancamento()), 4))
    c1.adiciona_rent(
        Rent(Tape("Pateta no Planeta dos Macacos", gerenciadorDeTapes=GerenciadorDeTapesInfantil()), 10))
    c1.adiciona_rent(Rent(Tape("O Rei Leão", gerenciadorDeTapes=GerenciadorDeTapesInfantil()), 30))

    print(c1.gerar_extrato_html())
    print(c1.gerar_extrato_text())
