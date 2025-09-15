from flask import render_template, request, redirect, url_for
import urllib
import json

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
        
        # Seções que devem ser ignoradas
        secoes_ignorar = [
            'uniformes', 'hino', 'torcida', 'títulos oficiais', 'títulos', 
            'estatísticas', 'participações', 'confrontos nacionais', 'jogadores',
            'maiores artilheiros', 'campanhas de destaque', 'competições oficiais',
            'competições oficiais (extintas)', 'última atualização'
        ]
        
        for linha in linhas:
            linha = linha.strip()
            
            # Detectar seções (=== Título ===)
            if linha.startswith('===') and linha.endswith('==='):
                # Salvar seção anterior se existir
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
                
                # Nova seção
                secao_atual = linha.replace('=', '').strip()
                conteudo_atual = []
                
                # Verificar se é seção de rivalidades
                if 'rival' in secao_atual.lower():
                    em_rivalidades = True
                    rivalidades_conteudo = []
                else:
                    em_rivalidades = False
            
            # Detectar subseções (==== Título ====)
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
            
            # Adicionar conteúdo à seção atual
            elif secao_atual and linha:
                conteudo_atual.append(linha)
        
        # Adicionar última seção
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
        
        # Adicionar seção consolidada de rivalidades se existir
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
        return render_template('estatisticas.html', estatisticas=estatisticas)
    
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
            