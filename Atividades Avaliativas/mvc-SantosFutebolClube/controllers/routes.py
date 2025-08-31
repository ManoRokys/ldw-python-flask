from flask import render_template, request, redirect, url_for


def init_app(app):
    jogadores = [
        'Gabriel Brazão (Goleiro) - 77',
        'João Paulo (Goleiro) - 1',
        'Diógenes (Goleiro) - 12', 
        'Mayke (Defensor) - 2',
        'Zé Ivaldo (Defensor) - 2',
        'João Basso (Defensor) - 3',
        'Gil (Defensor) - 4',
        'Neymar (Meio-campo/Atacante) - 10',
        'Guilherme Augusto (Atacante) - 11',
        'Deivid Washington (Atacante) - 36',
        'Gustavo Caballero (Atacante) - 17',
        'Benjamín Rollheiser (Atacante) - 32',
        'Willian Arão (Meio-campo) - 15',
        'Thaciano (Meio-campo) - 16',
        'Hyan (Meio-campo) - 20',
        'Gabriel Bontempo (Meio-campo) - 49',
        'Robinho Júnior (Atacante) - 7',
        'Tiquinho Soares (Atacante) - 9',
        'Luca Meirelles (Atacante) - 79',
        'Mateus Xavier (Atacante) - 41'
    ]
    
    posicoes = [
        'Goleiro',
        'Defensor', 
        'Meio-campo',
        'Atacante',
        'Meio-campo/Atacante'
    ]
    
    estatisticas = [
        {'Ano': 1961, 'Competição': 'Taça Brasil', 'Resultado': 'Campeão'},
        {'Ano': 1962, 'Competição': 'Taça Brasil', 'Resultado': 'Campeão'},
        {'Ano': 1963, 'Competição': 'Taça Brasil', 'Resultado': 'Campeão'},
        {'Ano': 1964, 'Competição': 'Taça Brasil', 'Resultado': 'Campeão'},
        {'Ano': 1965, 'Competição': 'Taça Brasil', 'Resultado': 'Campeão'},
        {'Ano': 1968, 'Competição': 'Robertão', 'Resultado': 'Campeão'},
        {'Ano': 2002, 'Competição': 'Brasileirão', 'Resultado': 'Campeão'},
        {'Ano': 2004, 'Competição': 'Brasileirão', 'Resultado': 'Campeão'},
        {'Ano': 2011, 'Competição': 'Copa Libertadores', 'Resultado': 'Campeão'},
        {'Ano': 2021, 'Competição': 'Brasileirão Série A', 'Resultado': '10º lugar'},
        {'Ano': 2022, 'Competição': 'Brasileirão Série A', 'Resultado': '12º lugar'},
        {'Ano': 2023, 'Competição': 'Brasileirão Série A', 'Resultado': '17º lugar - Rebaixamento'},
        {'Ano': 2024, 'Competição': 'Brasileirão Série B', 'Resultado': '1º lugar - Campeão e Acesso'},
        {'Ano': 2025, 'Competição': 'Brasileirão Série A', 'Resultado': '15º lugar - Em Andamento'}
    ]
    
    @app.route('/')
    def home():
        return render_template('index.html')

    @app.route('/jogadores', methods=['GET', 'POST'])
    def jogadores_rota():
        if request.method == 'POST':
            nome = request.form.get('nome')
            posicao = request.form.get('posicao')
            numero = request.form.get('numero')
            if nome and posicao and numero:
                jogador_completo = f"{nome} ({posicao}) - {numero}"
                jogadores.append(jogador_completo)
                return redirect(url_for('jogadores_rota'))
                
        return render_template('jogadores.html', jogadores=jogadores, posicoes=posicoes)
        
    @app.route('/estatisticas', methods=['GET', 'POST'])
    def estatisticas_rota():
        if request.method == 'POST':
            if request.form.get('ano') and request.form.get('competicao') and request.form.get('resultado'):
                estatisticas.append({
                    'Ano': request.form.get('ano'), 
                    'Competição': request.form.get('competicao'), 
                    'Resultado': request.form.get('resultado')
                })
                return redirect(url_for('estatisticas_rota'))
        return render_template('estatisticas.html', estatisticas=estatisticas)