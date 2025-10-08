class Noleggio:
    def __init__(self, codice, data, id_automobile, cognome_cliente):
        self.codice = codice
        self.data = data
        self.id_automobile = id_automobile
        self.cognome_cliente = cognome_cliente

    def __str__(self):
        return f'{self.codice} - {self.data} - {self.id_automobile} - Cliente {self.cognome_cliente}'