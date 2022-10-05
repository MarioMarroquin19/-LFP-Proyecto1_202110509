class Excepcion:

    def __init__(self, error, tipo, columna, fila):
        self.error = error
        self.tipo = tipo
        self.columna = columna
        self.fila = fila
