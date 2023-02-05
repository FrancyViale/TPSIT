import requests
HOST = "http://localhost:5000"

def getPercorsi():
    percorsi = requests.get(HOST+"/api/v1/percorsi")
    return percorsi

def creaPercorso():
    data = {"nome:quadrato"}
    requests.post(HOST+"/api/v1/percorsi")

def main():
    percorsi = getPercorsi()
    print(percorsi.content)


if __name__ == "__main__":
    main()