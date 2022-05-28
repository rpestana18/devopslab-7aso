from flask import Flask
from flask_wtf.csrf import CSRFProtect

app = Flask(__name__)

csrf = CSRFProtect(app)

@app.route("/")
def pagina_inicial():
    return "Grupo 22 4Winds\n1-Danilo Caporal\n2-Gicele Castro\n3-Jeremias Oliveira\n4-Rodrigo Pestana"   

if __name__ == '__main__':
    app.run()