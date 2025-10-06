# Santos Futebol Clube - Aplicação Flask (MVC + CRUD + MySQL)

## Descrição
Aplicação Flask desenvolvida para a atividade avaliativa sobre o Santos Futebol Clube. A aplicação demonstra o uso de padrão MVC (Model-View-Controller) com Flask e apresenta informações atualizadas sobre o elenco 2025 e estatísticas históricas.

## Funcionalidades

### 🏠 Página Inicial
- Apresentação do clube com cards informativos e imagens
- Destaques da temporada 2025
- Conquistas históricas destacadas
- Situação atual do clube (2025)
- Navegação para outras seções
- Design responsivo com Bootstrap
- Imagens em todos os cards principais e secundários
- **Background preto e branco** com efeitos visuais

### ⚽ Elenco Atual (Jogadores)
- **Lista organizada por posição**: Goleiros, Zagueiros, Laterais, Meio-Campo e Ataque
- **Formulário inteligente**: Campo de nome + caixinha de seleção para posição
- **Interface moderna**: Cards do Bootstrap com cores temáticas por posição
- **Elenco 2024**: Inclui jogadores como Neymar Jr., Tiquinho Soares, Benjamín Rollheiser
- **Posições disponíveis**: 10 posições diferentes para seleção

### 📊 Estatísticas Atualizadas
- **Tabela de dados**: Exibição das estatísticas em formato tabular
- **Formulário de inclusão**: Permite adicionar novas estatísticas
- **Dados estruturados**: Uso de dicionários para organizar as informações
- **Histórico completo**: Desde conquistas históricas até o desempenho atual
- **Recordes históricos**: Pentacampeonato, tricampeonato invicto, 8 títulos brasileiros
- **Situação atual**: Performance no Brasileirão 2025 e campanha na Série B 2024

## Tecnologias Utilizadas
- **Backend**: Python Flask, Flask-SQLAlchemy
- **Banco de Dados**: MySQL (SQLAlchemy URI `mysql+pymysql://`)
- **Driver**: PyMySQL
- **Frontend**: HTML5, CSS3, Bootstrap 5.3.3
- **Padrão**: MVC (Model-View-Controller)
- **Porta**: 4000
- **Host**: 0.0.0.0 (acesso externo)
- **Debug**: Ativo

## Estrutura do Projeto
```
mvc-SantosFutebolClube-CRUD-MYSQL/
├── app.py                 # Arquivo principal da aplicação
├── controllers/
│   └── routes.py         # Rotas: home, jogadores, estatísticas, CRUD times/jogadores/partidas, história (Wikipedia)
├── models/
│   └── database.py       # Modelos SQLAlchemy: Time, Jogador, Partida
├── static/
│   ├── css/
│   │   └── style.css     # Estilos personalizados incluindo form-select, imagens e background
│   └── images/
│       ├── README.md     # Guia de imagens implementadas
│       ├── background.jpg # Background principal com filtro preto e branco
│       ├── Santos_Logo.png
│       ├── elenco.jpeg
│       ├── estatisticas.jpg
│       └── historia.jpg
├── views/
│   ├── base.html         # Template base com navbar e logo
│   ├── index.html        # Página inicial
│   ├── jogadores.html    # Elenco (lista manual + formulário)
│   ├── jogadores_db.html # CRUD de Jogadores (DB)
│   ├── times.html        # CRUD de Times
│   ├── partidas.html     # CRUD de Partidas
│   ├── edit_time.html    # Editar Time
│   ├── edit_jogador.html # Editar Jogador
│   ├── edit_partida.html # Editar Partida
│   ├── time_jogadores.html # Lista jogadores por time
│   ├── estatisticas.html # Estatísticas + Paginação de Partidas
│   └── historia.html     # História (conteúdo extraído da Wikipedia)
└── README.md             # Este arquivo
```

## Como Executar

1. **Instalar dependências**:
   ```bash
   pip install flask flask_sqlalchemy pymysql
   ```

2. **Imagens já implementadas**:
   - ✅ Background preto e branco em toda a aplicação
   - ✅ Logo do Santos na navbar
   - ✅ Imagens em todos os cards principais
   - ✅ Imagens nos cards secundários

3. **Executar a aplicação**:
   ```bash
   python app.py
   ```

4. **Acessar no navegador**:
   - Local: http://localhost:4000
   - Rede: http://[seu-ip]:4000

## Rotas da Aplicação

- **GET /**: Página inicial
- **GET/POST /jogadores**: Elenco manual e formulário (não persiste no DB)
- **GET/POST /estatisticas**: Estatísticas estáticas + Paginação das partidas do Santos via banco
- **GET/POST /times** | **GET /times/delete/<id>**: CRUD de Times com paginação
- **GET/POST /jogadores_db** | **GET /jogadores_db/delete/<id>**: CRUD de Jogadores
- **GET/POST /partidas** | **GET /partidas/delete/<id>**: CRUD de Partidas
- **GET /times/edit/<id>**, **GET /jogadores_db/edit/<id>**, **GET /partidas/edit/<id>**: Edição
- **GET /time/<id>/jogadores**: Lista jogadores de um time específico
- **GET /historia**: Integração com Wikipedia (API) para exibir a história do clube com seções processadas

## Características Técnicas

- ✅ **CRUD completo**: Times, Jogadores e Partidas com paginação
- ✅ **Integração Wikipedia**: consumo da API com user-agent e tratamento de erros
- ✅ **Navbar** com navegação entre páginas e logo
- ✅ **Lista organizada** para exibição de jogadores por posição
- ✅ **Tabela** para exibição de estatísticas
- ✅ **Formulários** para inclusão de dados
- ✅ **Caixinha de seleção** para escolha de posição
- ✅ **Imagens integradas** em todos os cards principais
- ✅ **Logo do Santos** na navbar
- ✅ **Background preto e branco** com filtros CSS
- ✅ **Estatísticas atualizadas** até 2025
- ✅ **Recordes históricos** destacados
- ✅ **Bootstrap** para interface moderna
- ✅ **Arquivos estáticos** (CSS e imagens personalizados)
- ✅ **Porta 4000** com acesso externo
- ✅ **Modo debug** ativo
- ✅ **Padrão MVC** implementado
- ✅ **Elenco atualizado** com jogadores recentes

## Dados do Elenco

A aplicação inclui informações sobre:
- **Goleiros**: Gabriel Brazão, Diógenes
- **Zagueiros**: Zé Ivaldo, Basso, Luan Peres, Luisão, Gil
- **Laterais**: Souza, Gonzalo Escobar, Vinicius Lira, JP Chermont, Mayke, Igor Vinícius
- **Meio-Campo**: Willian Arão, João Schmidt, Tomás Rincón, Gabriel Bontempo, Zé Rafael, Hyan, Neymar, Thaciano
- **Ataque**: Álvaro Barreal, Guilherme, Gustavo Caballero, Mateus Xavier, Robinho Junior, Benjamín Rollheiser, Andrey Quintino, Deivid Washington, Tiquinho Soares

## Posições Disponíveis

O formulário de adição de jogadores oferece as seguintes posições:
1. **Goleiro** - Protetor do gol
2. **Zagueiro** - Defensor central
3. **Lateral Esq.** - Defensor lateral esquerdo
4. **Lateral Dir.** - Defensor lateral direito
5. **Volante** - Meio-campista defensivo
6. **Meia Central** - Meio-campista central
7. **Meia Ofensivo** - Meio-campista ofensivo
8. **Ponta Esquerda** - Atacante pela esquerda
9. **Ponta Direita** - Atacante pela direita
10. **Centroavante** - Atacante central

## Estatísticas Atualizadas

### Conquistas Históricas
- **8 títulos brasileiros**: 1961, 1962, 1963, 1964, 1965, 1968, 2002, 2004
- **Pentacampeonato consecutivo**: 1961-1965 (único clube brasileiro)
- **Tricampeonato invicto**: 1963, 1964, 1965
- **Seis finais consecutivas**: 1961-1966
- **3 Copas Libertadores**: 1962, 1963, 2011
- **2 Copas Intercontinentais**: 1962, 1963
- **Recorde de gols**: 103 gols em 46 jogos (2004)

### Desempenho Recente
- **2021**: Brasileirão Série A - 10º lugar
- **2022**: Brasileirão Série A - 12º lugar
- **2023**: Brasileirão Série A - 17º lugar (Rebaixamento)
- **2024**: Brasileirão Série B - 1º lugar (Campeão e Acesso)
- **2025**: Brasileirão Série A - 15º lugar (Em Andamento)

## Imagens Implementadas

A aplicação já possui todas as imagens necessárias implementadas:
- ✅ `background.jpg` - Background principal com filtro preto e branco
- ✅ `Santos_Logo.png` - Logo do Santos FC na navbar
- ✅ `elenco.jpeg` - Foto do elenco atual nos cards principais e secundários
- ✅ `estatisticas.jpg` - Imagem relacionada a conquistas
- ✅ `historia.jpg` - Imagem histórica do clube

## Efeitos Visuais

### Background
- **Filtro preto e branco**: Grayscale 100% aplicado via CSS
- **Escurecimento**: Brightness 30% para melhor contraste
- **Overlay escuro**: Camada adicional para legibilidade
- **Posicionamento fixo**: Não rola com o conteúdo

### Interface
- **Cards semi-transparentes**: Com backdrop-filter blur
- **Navbar e footer**: Semi-transparentes com efeito blur
- **Texto principal**: Branco com sombra para contraste
- **Hover effects**: Transições suaves nos elementos

## Autor
Lucas Gomes Fagundes.
Desenvolvido para a atividade avaliativa de Laboratorio de Desenvolvimento Web do Professor Diego, com tema do Santos Futebol Clube.
