# Script che CREA il database e lo popola

import sqlite3
conn = sqlite3.connect('Percorsi.db')
cursor = conn.cursor()

# Creo le tabelle necessarie
cursor.execute('''CREATE TABLE Percorso (id INTEGER PRIMARY KEY, nome TEXT)''')

cursor.execute('''CREATE TABLE Mossa (codPercorso INTEGER, posizione INTEGER, 
                                       codMovimento INTEGER, tempo INTEGER, 
                                       PRIMARY KEY (codPercorso, posizione))''')

cursor.execute('''CREATE TABLE Movimento (id INTEGER PRIMARY KEY, nome TEXT)''')



cursor.execute("INSERT INTO Percorso VALUES (0, 'quadrato')")
cursor.execute("INSERT INTO Percorso VALUES (1, 'andamento a T')")
cursor.execute("INSERT INTO Percorso VALUES (2, 'Percorso misto')")


# Inserisco dati nella tabella Mossa
cursor.execute("INSERT INTO Mossa VALUES (0, 1, 0, 20)")
cursor.execute("INSERT INTO Mossa VALUES (0, 2, 2, 20)")
cursor.execute("INSERT INTO Mossa VALUES (0, 3, 1, 20)")
cursor.execute("INSERT INTO Mossa VALUES (0, 4, 3, 20)")

cursor.execute("INSERT INTO Mossa VALUES (1, 1, 0, 50)")
cursor.execute("INSERT INTO Mossa VALUES (1, 2, 3, 20)")
cursor.execute("INSERT INTO Mossa VALUES (1, 3, 0, 10)")
cursor.execute("INSERT INTO Mossa VALUES (1, 4, 2, 50)")
cursor.execute("INSERT INTO Mossa VALUES (1, 5, 1, 10)")
cursor.execute("INSERT INTO Mossa VALUES (1, 6, 3, 20)")
cursor.execute("INSERT INTO Mossa VALUES (1, 7, 1, 50)")
cursor.execute("INSERT INTO Mossa VALUES (1, 8, 3, 10)")

cursor.execute("INSERT INTO Mossa VALUES (2, 1, 0, 20)")
cursor.execute("INSERT INTO Mossa VALUES (2, 2, 0, 10)")
cursor.execute("INSERT INTO Mossa VALUES (2, 3, 2, 50)")
cursor.execute("INSERT INTO Mossa VALUES (2, 4, 3, 20)")
cursor.execute("INSERT INTO Mossa VALUES (2, 5, 1, 50)")
cursor.execute("INSERT INTO Mossa VALUES (2, 6, 3, 10)")
cursor.execute("INSERT INTO Mossa VALUES (2, 7, 1, 20)")


cursor.execute("INSERT INTO Movimento VALUES (0, 'AVANTI')")
cursor.execute("INSERT INTO Movimento VALUES (1, 'INDIETRO')")
cursor.execute("INSERT INTO Movimento VALUES (2, 'DESTRA')")
cursor.execute("INSERT INTO Movimento VALUES (3, 'SINISTRA')")


conn.commit()
conn.close()

