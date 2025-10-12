from automobile import Automobile
from noleggio import Noleggio
import csv

class Autonoleggio:
    def __init__(self, nome, responsabile):
        """Inizializza gli attributi e le strutture dati"""
        # TODO
        self.nome = nome
        self.responsabile = responsabile
        self.automobili = []
        self.noleggi = []
        self.prossimo_id_auto= 1
        self.prossimo_id_noleggio = 1



    def carica_file_automobili(self, file_path):
        """Carica le auto dal file"""
        # TODO
        try:
            f = open(file_path, 'r')
            righe = csv.reader(f)
            for riga in righe:
                codice, marca, modello, anno, num_posti = riga
                auto = Automobile(codice, marca, modello, anno, num_posti)
                self.automobili.append(auto)

                numero = int(codice[1:])
                self.prossimo_id_auto = max(self.prossimo_id_auto, numero + 1)

        except FileNotFoundError:
            print(f'Errore: il file {file_path} non esiste')

        f.close()



    def aggiungi_automobile(self, marca, modello, anno, num_posti):
        """Aggiunge un'automobile nell'autonoleggio: aggiunge solo nel sistema e non aggiorna il file"""
        # TODO
        codice = f'A{self.prossimo_id_auto}'
        self.prossimo_id_auto += 1
        nuova_auto = Automobile(codice, marca, modello, anno, num_posti)
        self.automobili.append(nuova_auto)
        return nuova_auto



    def automobili_ordinate_per_marca(self):
        """Ordina le automobili per marca in ordine alfabetico"""
        # TODO
        automobili_ordinate = sorted(self.automobili, key=lambda a: a.marca.lower())
        return automobili_ordinate



    def nuovo_noleggio(self, data, id_automobile, cognome_cliente):
        """Crea un nuovo noleggio"""
        # TODO
        auto = None
        for a in self.automobili:
            if a.codice == id_automobile:
                auto = a
        if auto is None:
            raise Exception(f'Automobile {id_automobile} non trovata')\

        for n in self.noleggi:
            if n.id_automobile == id_automobile:
                raise Exception(f'Automobile {id_automobile} già noleggiata')

        codice_noleggio = f'N{self.prossimo_id_noleggio}'
        self.prossimo_id_noleggio += 1
        nuovo_noleggio = Noleggio(codice_noleggio, data, id_automobile, cognome_cliente)
        self.noleggi.append(nuovo_noleggio)
        return nuovo_noleggio



    def termina_noleggio(self, id_noleggio):
        """Termina un noleggio in atto"""
        # TODO
        noleggi_restanti = [n for n in self.noleggi if n.codice != id_noleggio]
        if len(noleggi_restanti) == len(self.noleggi):
            raise Exception(f'Noleggio {id_noleggio} non trovato')
        self.noleggi = noleggi_restanti