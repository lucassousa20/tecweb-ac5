from aplicacao import app
from flask import render_template
from flask import redirect
from flask import request
from models import Presenca


@app.route('/')
def index():
    ## Insere opções no menu
    menu = []
    ## Cada opção no menu é um dicionário
    menu.append({'active': True, # active informa se a opção está ativa, e se estiver, destaca ela na página
                'href': '/', # href é o caminho que deve ser aberto pela opção
                'texto': 'Página principal'}) # texto é o texto exibido no menu para a opção
    menu.append({'active': False,
                'href': '/presenca',
                'texto': 'Presença'})
    menu.append({'active': False,
                'href': '/presencas',
                'texto': 'Presenças Computadas'})

    ## Inserimos tudo que foi criado no dicionário context, ele será passado para a view
    context = {'titulo': 'Integrantes',
            'menu': menu}

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
                 'href': '/presencas',
                 'texto': 'Presenças Computadas'})

    context = {'titulo': 'Presença',
               'menu': menu}
    return render_template('presenca.html', **context)


@app.route('/presencas')
def presencas():
    presencas = Presenca.recupera_todas()
    menu = []
    menu.append({'active': False,
                'href': '/',    
                'texto': 'Página principal'})
    menu.append({'active': False,
                'href': '/presenca',
                'texto': 'Presença'})
    menu.append({'active': True,
                'href': '/presencas',
                'texto': 'Presenças Computadas'})

    context = {'titulo': 'Presenças Computadas',
            'menu': menu,
            'presencas': presencas}

    return render_template('presencas.html', **context)


@app.route('/presenca/gravar', methods=['POST'])
def gravar_presenca():
    presenca = Presenca(request.form['email'], request.form['presenca'], request.form['resposta'], request.form['comentario'])
    presenca.gravar_presenca()
    return redirect('/')

@app.route('/lucas')
def lucas():
    ## Insere opções no menu
    menu = []
    ## Cada opção no menu é um dicionário
    menu.append({'active': True, # active informa se a opção está ativa, e se estiver, destaca ela na página
                'href': '/', # href é o caminho que deve ser aberto pela opção
                'texto': 'Página principal'}) # texto é o texto exibido no menu para a opção
    menu.append({'active': False,
                'href': '/mensagem',
                'texto': 'Escrever mensagem'})

    context = {'titulo': 'Lucas Sousa'}

    return render_template('lucas.html', **context)


app.run()
