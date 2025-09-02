from flask import Flask, render_template # Importando o Flask
from controllers import routes
from models.database import db
import os
# Criando uma instância do Flask
app = Flask(__name__, template_folder='views') # O __name__ representa o nome da aplicação/arquivo que está sendo executado futuramente irá ser __main__

routes.init_app(app)

dir = os.path.abspath(os.path.dirname(__file__))

app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///' + os.path.join(dir, 'models/games.sqlite3')

# Se o arquivo for executado diretamento pelo interpretador ele vira o nome __main__ e inicia o servidor
if __name__ == '__main__':
    db.init_app(app=app)
    with app.test_request_context():
        db.create_all()
    app.run(host='localhost', port=5000, debug=True) # Iniciando o servidor