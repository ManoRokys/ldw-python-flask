from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

class Time(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    nome = db.Column(db.String(150), nullable=False)
    cidade = db.Column(db.String(150))
    estado = db.Column(db.String(2))
    fundacao = db.Column(db.Integer)
    
    jogadores = db.relationship('Jogador', backref='time', lazy=True)
    
    partidas_mandante = db.relationship('Partida', 
                                      foreign_keys='Partida.time_mandante_id',
                                      backref='time_mandante', 
                                      lazy=True)
    
    partidas_visitante = db.relationship('Partida', 
                                       foreign_keys='Partida.time_visitante_id',
                                       backref='time_visitante', 
                                       lazy=True)
    
    def __init__(self, nome, cidade, estado, fundacao):
        self.nome = nome
        self.cidade = cidade
        self.estado = estado
        self.fundacao = fundacao

class Jogador(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    nome = db.Column(db.String(150), nullable=False)
    posicao = db.Column(db.String(50))
    numero = db.Column(db.Integer)
    time_id = db.Column(db.Integer, db.ForeignKey('time.id'), nullable=False)
    
    def __init__(self, nome, posicao, numero, time_id):
        self.nome = nome
        self.posicao = posicao
        self.numero = numero
        self.time_id = time_id

class Partida(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    data = db.Column(db.Date, nullable=False)
    competicao = db.Column(db.String(150))
    time_mandante_id = db.Column(db.Integer, db.ForeignKey('time.id'), nullable=False)
    time_visitante_id = db.Column(db.Integer, db.ForeignKey('time.id'), nullable=False)
    gols_mandante = db.Column(db.Integer, default=0)
    gols_visitante = db.Column(db.Integer, default=0)
    
    def __init__(self, data, competicao, time_mandante_id, time_visitante_id, gols_mandante, gols_visitante):
        self.data = data
        self.competicao = competicao
        self.time_mandante_id = time_mandante_id
        self.time_visitante_id = time_visitante_id
        self.gols_mandante = gols_mandante
        self.gols_visitante = gols_visitante