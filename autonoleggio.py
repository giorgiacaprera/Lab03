class Autonoleggio:
    def __init__(self, nome, responsabile):
        """Inizializza gli attributi e le strutture dati"""
        # TODO



    def carica_file_automobili(self, file_path):
        """Carica le auto dal file"""
        # TODO
        try:
            with open(file_path, 'r', encoding='utf-8') as f:
                for riga in f:
                    riga = riga.strip()
                    parti = riga.split(',')
                    codice, marca, modello, anno, num_posti = parti
                    auto = Automobile(codice, marca, modello, anno, num_posti)
                    self.automobili.append(auto)

        except FileNotFoundError:
            print(f'Errore: il file {file_path} non esiste')
            return None



    def aggiungi_automobile(self, marca, modello, anno, num_posti):
        """Aggiunge un'automobile nell'autonoleggio: aggiunge solo nel sistema e non aggiorna il file"""
        # TODO
        self.num_codice += 1
        nuovo_codice = f'N{self.num_codice}'
        nuova_auto = Automobile(nuovo_codice, marca, modello, anno, num_posti)
        self.automobili.append(nuova_auto)



    def automobili_ordinate_per_marca(self):
        """Ordina le automobili per marca in ordine alfabetico"""
        # TODO

    def nuovo_noleggio(self, data, id_automobile, cognome_cliente):
        """Crea un nuovo noleggio"""
        # TODO

    def termina_noleggio(self, id_noleggio):
        """Termina un noleggio in atto"""
        # TODO
