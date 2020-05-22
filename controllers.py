from aplicacao import app
from flask import render_template
from flask import redirect
from flask import request
from models import Presenca


@app.route('/')
def index():
    presencas = Presenca.recupera_todas()
    menu = []
    ## Cada opção no menu é um dicionário
    menu.append({'active': True, # active informa se a opção está ativa, e se estiver, destaca ela na página
                'href': '/', # href é o caminho que deve ser aberto pela opção
                'texto': 'Página principal'}) # texto é o texto exibido no menu para a opção
    menu.append({'active': False,
                'href': '/presenca',
                'texto': 'Presença'})
    menu.append({'active': False,
                'href':'/lucas',
                'texto': 'Lucas Souza'})
    menu.append({'active': False,
                'href':'/lucas',
                'texto': 'Maria Vitoria'})

    ## Inserimos tudo que foi criado no dicionário context, ele será passado para a view
    context = {'titulo': 'Página principal',
            'menu': menu,
            'presencas': presencas}

    return render_template('index.html', **context)

@app.route('/presenca')
def presenca():
    menu = []
    menu.append({'active': False,
                 'href': '/',
                 'texto': 'Página principal'})
    menu.append({'active': True,
                 'href': '/presenca',
                 'texto': 'Presença'})
    menu.append({'active': False,
                'href':'/lucas',
                'texto': 'Lucas Souza'})
    menu.append({'active': False,
                'href':'/maria',
                'texto': 'Maria Vitoria'})

    context = {'titulo': 'Presença',
               'menu': menu}
    return render_template('presenca.html', **context)

@app.route('/presenca/gravar', methods=['POST'])
def gravar_presenca():
    presencas = Presenca(request.form['email'], request.form['presenca'], request.form['resposta'], request.form['comentario'])
    presencas.gravar_presenca()
    return redirect('/')


@app.route('/lucas')
def lucas():
    menu = []
    menu.append({'active': False,
                 'href': '/',
                 'texto': 'Página principal'})
    menu.append({'active': False,
                 'href': '/presenca',
                 'texto': 'Presença'})
    menu.append({'active': True,
                'href':'/lucas',
                'texto': 'Lucas Souza'})
    menu.append({'active': False,
                'href':'/maria',
                'texto': 'Maria Vitoria'})

    context = {'titulo': 'Lucas Sousa',
                'menu': menu}

    return render_template('lucas.html', **context)

@app.route('/maria')
def maria():
    menu = []
    menu.append({'active': False,
                 'href': '/',
                 'texto': 'Página principal'})
    menu.append({'active': False,
                 'href': '/presenca',
                 'texto': 'Presença'})
    menu.append({'active': False,
                'href':'/lucas',
                'texto': 'Lucas Souza'})
    menu.append({'active': True,
                'href':'/maria',
                'texto': 'Maria Vitoria'})

    context = {'titulo': 'Maria Vitoria',
                'menu': menu}

    return render_template('Maria.html', **context)


app.run()
