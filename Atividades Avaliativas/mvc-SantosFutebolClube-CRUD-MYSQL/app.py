from flask import Flask
from controllers import routes
import pymysql
from models.database import db

app = Flask(__name__, template_folder='views')

DB_NAME = 'santos_fc'
app.config['DATABASE_NAME'] = DB_NAME
app.config['SQLALCHEMY_DATABASE_URI'] = f'mysql+pymysql://root@localhost/{DB_NAME}'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

routes.init_app(app)

if __name__ == '__main__':
    connection = pymysql.connect(host='localhost',
                                user='root',
                                password='',
                                charset='utf8mb4',
                                cursorclass=pymysql.cursors.DictCursor)
    try:
        with connection.cursor() as cursor:
            cursor.execute(f"CREATE DATABASE IF NOT EXISTS {DB_NAME}")
            print(f"O banco de dados {DB_NAME} está criado!")
    except Exception as e:
        print(f"Erro ao criar o banco de dados: {e}")
    finally:
        connection.close()

    db.init_app(app=app)

    with app.test_request_context():
        db.create_all()

    app.run(host='0.0.0.0', port=4000, debug=True)