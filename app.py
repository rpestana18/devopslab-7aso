from flask import Flask
from flask_wtf.csrf import CSRFProtect
import os

app = Flask(__name__)

csrf = CSRFProtect(app)

@app.route("/")
def pagina_inicial():
    return "Grupo Tech Leads Brazil"   

if __name__ == '__main__':
    port = os.getenv('PORT')
    app.run('0.0.0.0', port=port)
