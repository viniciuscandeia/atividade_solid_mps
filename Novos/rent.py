from tape import Tape


class Rent:
    def __init__(self, tape: Tape, dias_alugada: int):
        self.tape: Tape = tape
        self.dias_alugada: int = dias_alugada

    def get_tape(self) -> Tape:
        return self.tape

    def get_dias_alugada(self) -> int:
        return self.dias_alugada

    def get_custo_aluguel(self):
        return self.tape.calcular_custo_aluguel(self.dias_alugada)

    def get_pontos_de_alugador(self):
        return self.tape.calcular_pontos(self.dias_alugada)
    
