from flask import Flask, render_template

app = Flask(__name__, template_folder='views')


@app.route('/')
def home(): 
    return render_template('index.html')


@app.route('/games')
def games(): 
    title = 'Call of Duty'
    year = 2008
    category = 'Shooter'
    players = ['Yan', 'Ferrari', 'Valéria', 'Amanda']
    console = {'name' : 'Playstation 5',
               'manufacturer': 'Sony',
               'year': 2020}
    return render_template('games.html',
                            title=title,
                            year=year,
                            category=category,
                            players=players,
                            console=console)


if __name__ == '__main__':
    app.run(host='localhost', port=5000, debug=True)