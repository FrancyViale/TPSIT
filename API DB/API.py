
import json
import sqlite3
from flask import Flask, jsonify, request


# funzione che restituisce i percorsi
def get_lista_percorsi(cursor):
    cursor.execute('''SELECT id, nome FROM Percorso''')
    percorsi = cursor.fetchall()
    return [{"id": percorso[0], "nome": percorso[1]} for percorso in percorsi]


# funzione che restituisce i dettagli di un percorso
def get_percorso(id, cursor):
    cursor.execute('''SELECT id, nome FROM Percorso WHERE id = ?''', (id,))
    percorso = cursor.fetchone()
    mossa = cursor.execute('''SELECT posizione, codMovimento, tempo, nome FROM Mossa, Movimento WHERE Mossa.codMovimento == Movimento.id AND codPercorso = ? ORDER BY posizione''', (id,))
    mossa = cursor.fetchall()
    elenco_mosse = [{"id": m[1], "nome": m[3], "tempo": m[2], "posizione": m[0]} for m in mossa]
    return {"id": percorso[0], "nome": percorso[1], "mossa": elenco_mosse}


app = Flask(__name__)
#decorator
@app.route("/api/v1/percorsi", methods = ['GET'])#sotto URL specifico per le api, v1 per modifiche non retrocompatibile
def lista_percorsi(): 
    try:
        with sqlite3.connect("Percorsi.db") as conn:
            cursor = conn.cursor()
            percorsi = get_lista_percorsi(cursor)
            temp = jsonify({"success": True})
        return temp
    except Exception as e:
        return jsonify({"success": False, "error":str(e)})


@app.route("/api/v1/percorsi", methods = ['GET'])
def creaPercorso():
    dati=request.get_json()
    try:
        with sqlite3.connect("Percorsi.db") as conn:
            cursor = conn.cursor()
            cursor.execute(''''INSERT INTO Percorso values()'''')

    except Exception as e:
        return jsonify({"success": False, "error":str(e)})


@app.route("/api/v1/percorsi/<id>")
def info_percorso(id):
    conn = sqlite3.connect('Percorsi.db')
    cursor = conn.cursor()
    percorso = get_percorso(id, cursor) 
    temp= jsonify(percorso) 
    conn.close()
    return temp


def main():
    app.run()

if __name__ == "__main__":
    main()










