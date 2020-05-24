from flask import Flask


app = Flask(__name__)
app.config.from_object(__name__)

app.config.update(
    DATABASE = 'banco.db',
    DEBUG = True,
    SECRET_KEY = 'development key',
    USERNAME = 'admin',
    PASSWORD = 'default',
)

