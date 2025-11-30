import csv
from operator import attrgetter
from automobile import Automobile
from noleggio import Noleggio

class Autonoleggio:
    def __init__(self, nome, responsabile):
        """Inizializza gli attributi e le strutture dati"""
        # TODO
        self._nome = nome
        self.responsabile = responsabile
        self.automobili = []
        self.noleggi = []

    @property
    def nome(self):
        return self._nome

    @nome.setter
    def nome(self, nome):
        self._nome = nome

    def carica_file_automobili(self, file_path):
        """Carica le auto dal file"""
        # TODO
        self.automobili.clear()
        try:
            with open(file_path, newline="", encoding="utf-8") as file:
                reader = csv.reader(file)
                for riga in reader:
                    codice, marca, modello, anno, posti = riga
                    auto = Automobile(codice, marca, modello, int(anno), int(posti))
                    self.automobili.append(auto)
        except FileNotFoundError:
            raise Exception(f"File {file_path} non trovato.")

    def aggiungi_automobile(self, marca, modello, anno, num_posti):
        """Aggiunge un'automobile nell'autonoleggio: aggiunge solo nel sistema e non aggiorna il file"""
        # TODO
        if self.automobili:
            ultimi_codici = []
            for a in self.automobili:
                ultimi_codici.append(int(a.codice[1:]))
            nuovo_id = max(ultimi_codici) + 1
        else:
            nuovo_id = 1
        codice = f"A{nuovo_id}"

        auto = Automobile(codice, marca, modello, anno, num_posti)
        self.automobili.append(auto)
        return auto

    def automobili_ordinate_per_marca(self):
        """Ordina le automobili per marca in ordine alfabetico"""
        # TODO
        lista_tuple = []
        for a in self.automobili:
            lista_tuple.append((a.marca, a))
        lista_tuple.sort()
        lista_ordinata = []
        for t in lista_tuple:
            lista_ordinata.append(t[1])
        return lista_ordinata

    def nuovo_noleggio(self, data, id_automobile, cognome_cliente):
        """Crea un nuovo noleggio"""
        # TODO
        auto = None
        for a in self.automobili:
            if a.codice == id_automobile:
                auto = a
        if auto is None:
            raise Exception(f'Automobile {id_automobile} non trovata')
        if not auto.disponibile:
            raise Exception(f"L'automobile {id_automobile} è già noleggiata.")

        noleggio = Noleggio(data, id_automobile, cognome_cliente)
        auto.disponibile = False
        self.noleggi.append(noleggio)
        return noleggio

    def termina_noleggio(self, id_noleggio):
        """Termina un noleggio in atto"""
        # TODO
        noleggio = None
        for n in self.noleggi:
            if n.codice == id_noleggio:
                noleggio = n
        if noleggio is None:
            raise Exception(f"Noleggio {id_noleggio} non trovato.")

        # Rende disponibile l'automobile
        for a in self.automobili:
            if a.codice == noleggio.id_automobile:
                a.disponibile = True

        # Elimina il noleggio
        self.noleggi.remove(noleggio)