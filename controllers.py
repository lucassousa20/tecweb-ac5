from app import app
from flask import render_template
from flask import redirect
from flask import request
from models import Presenca


@app.route('/')
def index():
    presencas = Presenca.recupera_todas()
    menu = []
    menu.append({'active': True,
                 'href': '/',
                 'texto': 'Página principal'})
    menu.append({'active': False,
                 'href': '/presenca',
                 'texto': 'Presença'})
    menu.append({'active': False,
                 'href': '/integrantes',
                 'texto': 'Integrantes'})

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
                 'href': '/integrantes',
                 'texto': 'Integrantes'})

    context = {'titulo': 'Presença',
               'menu': menu}
    return render_template('presenca.html', **context)


@app.route('/presenca/gravar', methods=['POST'])
def gravar_presenca():
    presencas = Presenca(request.form['email'], request.form['presenca'], request.form['resposta'], request.form['comentario'])
    presencas.gravar_presenca()
    return redirect('/')


@app.route('/integrantes')
def integrantes():
    menu = []
    menu.append({'active': False,
                 'href': '/',
                 'texto': 'Página principal'})
    menu.append({'active': False,
                 'href': '/presenca',
                 'texto': 'Presença'})
    menu.append({'active': True,
                 'href': '/integrantes',
                 'texto': 'Integrantes'})

    context = {'titulo': 'Integrantes',
               'menu': menu}

    return render_template('integrantes.html', **context)


@app.route('/lucas')
def lucas():
    menu = []
    menu.append({'active': False,
                 'href': '/',
                 'texto': 'Página principal'})
    menu.append({'active': False,
                 'href': '/presenca',
                 'texto': 'Presença'})
    menu.append({'active': False,
                 'href': '/integrantes',
                 'texto': 'Integrantes'})

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
                 'href': '/integrantes',
                 'texto': 'Integrantes'})

    context = {'titulo': 'Maria Vitoria',
               'menu': menu}

    return render_template('Maria.html', **context)

@app.route('/leandro')
def leandro():
    menu = []
    menu.append({'active': False,
                 'href': '/',
                 'texto': 'Página principal'})
    menu.append({'active': False,
                 'href': '/presenca',
                 'texto': 'Presença'})
    menu.append({'active': False,
                 'href': '/integrantes',
                 'texto': 'Integrantes'})

    context = {'menu': menu}

    return render_template('leandro.html', **context)


@app.route('/kennedy')
def kennedy():
    menu = []
    menu.append({'active': False,
                 'href': '/',
                 'texto': 'Página principal'})
    menu.append({'active': False,
                 'href': '/presenca',
                 'texto': 'Presença'})
    menu.append({'active': False,
                'href':'/integrantes',
                'texto': 'Integrantes'})

    context = {'titulo': 'Kennedy Silva',
                'menu': menu}

    return render_template('kennedy.html', **context)



    return render_template('leandro.html', **context)


app.run()
