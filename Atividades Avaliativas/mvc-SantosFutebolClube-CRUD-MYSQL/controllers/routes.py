from flask import render_template, request, redirect, url_for
import urllib
import json
from models.database import db, Time, Jogador, Partida
from datetime import datetime

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
    
    def processar_secoes(texto):
        secoes = []
        linhas = texto.split('\n')
        
        secao_atual = None
        conteudo_atual = []
        rivalidades_conteudo = []
        em_rivalidades = False
        
        secoes_ignorar = [
            'uniformes', 'hino', 'torcida', 'títulos oficiais', 'títulos', 
            'estatísticas', 'participações', 'confrontos nacionais', 'jogadores',
            'maiores artilheiros', 'campanhas de destaque', 'competições oficiais',
            'competições oficiais (extintas)', 'última atualização'
        ]
        
        for linha in linhas:
            linha = linha.strip()
            
            if linha.startswith('===') and linha.endswith('==='):
                if secao_atual and conteudo_atual:
                    titulo_limpo = secao_atual.lower()
                    if not any(ignorar in titulo_limpo for ignorar in secoes_ignorar):
                        if em_rivalidades:
                            rivalidades_conteudo.extend(conteudo_atual)
                        else:
                            secoes.append({
                                'titulo': secao_atual,
                                'conteudo': '\n'.join(conteudo_atual).strip(),
                                'icone': obter_icone_secao(secao_atual)
                            })
                
                secao_atual = linha.replace('=', '').strip()
                conteudo_atual = []
                
                if 'rival' in secao_atual.lower():
                    em_rivalidades = True
                    rivalidades_conteudo = []
                else:
                    em_rivalidades = False
            
            elif linha.startswith('====') and linha.endswith('===='):
                if secao_atual and conteudo_atual:
                    titulo_limpo = secao_atual.lower()
                    if not any(ignorar in titulo_limpo for ignorar in secoes_ignorar):
                        if em_rivalidades:
                            rivalidades_conteudo.extend(conteudo_atual)
                        else:
                            secoes.append({
                                'titulo': secao_atual,
                                'conteudo': '\n'.join(conteudo_atual).strip(),
                                'icone': obter_icone_secao(secao_atual)
                            })
                
                secao_atual = linha.replace('=', '').strip()
                conteudo_atual = []
            
            elif secao_atual and linha:
                conteudo_atual.append(linha)
        
        if secao_atual and conteudo_atual:
            titulo_limpo = secao_atual.lower()
            if not any(ignorar in titulo_limpo for ignorar in secoes_ignorar):
                if em_rivalidades:
                    rivalidades_conteudo.extend(conteudo_atual)
                else:
                    secoes.append({
                        'titulo': secao_atual,
                        'conteudo': '\n'.join(conteudo_atual).strip(),
                        'icone': obter_icone_secao(secao_atual)
                    })
        
        if rivalidades_conteudo:
            secoes.append({
                'titulo': 'Rivalidades',
                'conteudo': '\n'.join(rivalidades_conteudo).strip(),
                'icone': 'fas fa-fist-raised'
            })
        
        return secoes

    def obter_icone_secao(titulo):
        titulo_lower = titulo.lower()
        
        if 'história' in titulo_lower or 'historia' in titulo_lower:
            return 'fas fa-history'
        elif 'títulos' in titulo_lower or 'titulos' in titulo_lower:
            return 'fas fa-trophy'
        elif 'estatísticas' in titulo_lower or 'estatisticas' in titulo_lower:
            return 'fas fa-chart-bar'
        elif 'jogadores' in titulo_lower:
            return 'fas fa-users'
        elif 'rival' in titulo_lower or 'vs' in titulo_lower:
            return 'fas fa-fist-raised'
        elif 'século' in titulo_lower or 'seculo' in titulo_lower:
            return 'fas fa-calendar-alt'
        elif 'confrontos' in titulo_lower:
            return 'fas fa-handshake'
        else:
            return 'fas fa-info-circle'

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
                
        page = request.args.get('page', 1, type=int)
        per_page = 5
        
        santos = Time.query.filter_by(nome='Santos FC').first()
        
        if not santos:
            santos = Time('Santos FC', 'Santos', 'SP', 1912)
            db.session.add(santos)
            db.session.commit()
        
        partidas = Partida.query.filter(
            (Partida.time_mandante_id == santos.id) | 
            (Partida.time_visitante_id == santos.id)
        ).order_by(Partida.data.desc()).paginate(page=page, per_page=per_page)
        
        return render_template('estatisticas.html', 
                              estatisticas=estatisticas, 
                              partidas=partidas,
                              santos_id=santos.id)
    
    # CRUD para Times
    @app.route('/times', methods=['GET', 'POST'])
    @app.route('/times/delete/<int:id>')
    def times(id=None):
        if id:
            time = Time.query.get(id)
            if time:
                db.session.delete(time)
                db.session.commit()
            return redirect(url_for('times'))
            
        if request.method == 'POST':
            nome = request.form.get('nome')
            cidade = request.form.get('cidade')
            estado = request.form.get('estado')
            fundacao = request.form.get('fundacao')
            
            if nome and cidade and estado and fundacao:
                novo_time = Time(nome, cidade, estado, fundacao)
                db.session.add(novo_time)
                db.session.commit()
                return redirect(url_for('times'))
        
        page = request.args.get('page', 1, type=int)
        per_page = 5
        times = Time.query.paginate(page=page, per_page=per_page)
        
        return render_template('times.html', times=times)
    
    @app.route('/times/edit/<int:id>', methods=['GET', 'POST'])
    def edit_time(id):
        time = Time.query.get(id)
        
        if not time:
            return redirect(url_for('times'))
            
        if request.method == 'POST':
            time.nome = request.form.get('nome')
            time.cidade = request.form.get('cidade')
            time.estado = request.form.get('estado')
            time.fundacao = request.form.get('fundacao')
            
            db.session.commit()
            return redirect(url_for('times'))
            
        return render_template('edit_time.html', time=time)
    
    # CRUD para Jogadores
    @app.route('/jogadores_db', methods=['GET', 'POST'])
    @app.route('/jogadores_db/delete/<int:id>')
    def jogadores_db(id=None):
        if id:
            jogador = Jogador.query.get(id)
            if jogador:
                db.session.delete(jogador)
                db.session.commit()
            return redirect(url_for('jogadores_db'))
            
        if request.method == 'POST':
            nome = request.form.get('nome')
            posicao = request.form.get('posicao')
            numero = request.form.get('numero')
            time_id = request.form.get('time_id')
            
            if nome and posicao and numero and time_id:
                novo_jogador = Jogador(nome, posicao, numero, time_id)
                db.session.add(novo_jogador)
                db.session.commit()
                return redirect(url_for('jogadores_db'))
        
        page = request.args.get('page', 1, type=int)
        per_page = 10
        jogadores_lista = Jogador.query.paginate(page=page, per_page=per_page)
        times = Time.query.all()
        
        return render_template('jogadores_db.html', jogadores=jogadores_lista, times=times, posicoes=posicoes)

    @app.route('/jogadores/all')
    def jogadores_all():
        page = request.args.get('page', 1, type=int)
        per_page = 10
        jogadores_lista = Jogador.query.order_by(Jogador.nome.asc()).paginate(page=page, per_page=per_page)
        return render_template('jogadores_all.html', jogadores=jogadores_lista)
    
    @app.route('/jogadores_db/edit/<int:id>', methods=['GET', 'POST'])
    def edit_jogador(id):
        jogador = Jogador.query.get(id)
        
        if not jogador:
            return redirect(url_for('jogadores_db'))
            
        if request.method == 'POST':
            jogador.nome = request.form.get('nome')
            jogador.posicao = request.form.get('posicao')
            jogador.numero = request.form.get('numero')
            jogador.time_id = request.form.get('time_id')
            
            db.session.commit()
            return redirect(url_for('jogadores_db'))
            
        times = Time.query.all()
        return render_template('edit_jogador.html', jogador=jogador, times=times, posicoes=posicoes)
    
    # CRUD para Partidas
    @app.route('/partidas', methods=['GET', 'POST'])
    @app.route('/partidas/delete/<int:id>')
    def partidas(id=None):
        if id:
            partida = Partida.query.get(id)
            if partida:
                db.session.delete(partida)
                db.session.commit()
            return redirect(url_for('partidas'))
            
        if request.method == 'POST':
            data_str = request.form.get('data')
            competicao = request.form.get('competicao')
            time_mandante_id = request.form.get('time_mandante_id')
            time_visitante_id = request.form.get('time_visitante_id')
            gols_mandante = request.form.get('gols_mandante', 0)
            gols_visitante = request.form.get('gols_visitante', 0)
            
            if data_str and competicao and time_mandante_id and time_visitante_id:
                data = datetime.strptime(data_str, '%Y-%m-%d').date()
                nova_partida = Partida(data, competicao, time_mandante_id, time_visitante_id, gols_mandante, gols_visitante)
                db.session.add(nova_partida)
                db.session.commit()
                return redirect(url_for('partidas'))
        
        page = request.args.get('page', 1, type=int)
        per_page = 5
        partidas_lista = Partida.query.order_by(Partida.data.desc()).paginate(page=page, per_page=per_page)
        times = Time.query.all()
        
        return render_template('partidas.html', partidas=partidas_lista, times=times)
    
    @app.route('/partidas/edit/<int:id>', methods=['GET', 'POST'])
    def edit_partida(id):
        partida = Partida.query.get(id)
        
        if not partida:
            return redirect(url_for('partidas'))
            
        if request.method == 'POST':
            data_str = request.form.get('data')
            partida.data = datetime.strptime(data_str, '%Y-%m-%d').date()
            partida.competicao = request.form.get('competicao')
            partida.time_mandante_id = request.form.get('time_mandante_id')
            partida.time_visitante_id = request.form.get('time_visitante_id')
            partida.gols_mandante = request.form.get('gols_mandante', 0)
            partida.gols_visitante = request.form.get('gols_visitante', 0)
            
            db.session.commit()
            return redirect(url_for('partidas'))
            
        times = Time.query.all()
        return render_template('edit_partida.html', partida=partida, times=times)
    
    # Rota para visualizar jogadores de um time específico
    @app.route('/time/<int:id>/jogadores')
    def time_jogadores(id):
        time = Time.query.get(id)
        
        if not time:
            return redirect(url_for('times'))
            
        page = request.args.get('page', 1, type=int)
        per_page = 10
        jogadores = Jogador.query.filter_by(time_id=id).paginate(page=page, per_page=per_page)
        
        return render_template('time_jogadores.html', time=time, jogadores=jogadores)
    
    @app.route('/historia')
    def historia():
        try:
            url = "https://pt.wikipedia.org/w/api.php?action=query&format=json&prop=extracts&titles=Santos_Futebol_Clube&explaintext=true"
            req = urllib.request.Request(url)
            req.add_header('User-Agent', 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36')

            response = urllib.request.urlopen(req)
            data = response.read()
            dados = json.loads(data)

            pages = dados['query']['pages']
            page_id = list(pages.keys())[0]
            page_data = pages[page_id]
            
            extract = page_data.get('extract', '')
            title = page_data.get('title', 'Santos Futebol Clube')
            
            # Processar seções do texto
            secoes = processar_secoes(extract)
            
            return render_template('historia.html', 
                                 titulo=title, 
                                 extract=extract,
                                 secoes=secoes,
                                 dados={'title': title, 'extract': extract})

        except urllib.error.HTTPError as e:
            return render_template('historia.html', erro=f'Erro HTTP {e.code}: {e.reason}')
        except urllib.error.URLError as e:
            return render_template('historia.html', erro=f'Erro de conexão: {e.reason}')
        except json.JSONDecodeError as e:
            return render_template('historia.html', erro=f'Erro ao processar resposta da API: {e}')
        except Exception as e:
            return render_template('historia.html', erro=f'Erro inesperado: {e}')
            