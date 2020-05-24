<<<<<<< HEAD
# Projeto base - Flask

# Inicialização

Copie esse repositório para usar como base de projetos Flask

No Git Bash podemos executar o comando:

```
git clone https://github.com/fabiogoro/flask-base
```

Isso irá copiar o repositório na pasta flask-base.

Depois entramos na pasta do projeto:

```
cd flask-base
```

Então criamos o ambiente virtual com os pacotes necessário para esse projeto:

```
virtualenv venv
source venv/Scripts/activate
pip install -r requirements.python cria_bd.py
```

A partir daí podemos executar e visualizar o projeto.
Para executar:

```
python controllers.py
```

,,
## Estrutura

Esse projeto contém a seguinte estrutura:

### aplicacao.py

Inicializa e configura a aplicação Flask.

### controllers.py

Contém os controllers e rotas da aplicação.

### models.py

Contém os models da aplicação. A conexão da aplicação com o banco é feita dentro de models.

### static/

Contém arquivos estáticos, como css.

### templates/

Contém as views da aplicação. O arquivo base.html é usado como arquivo principal, herdado por todos os templates.

### banco.py

Contém as funções necessárias para conectar no banco.

### cria_bd.py

Script para criação do banco.

### esquema.sql
Contém a estrutura do banco de dados. Para alterar o ba
=======
Nome: Leandro de Lima Monteiro RA: 1901699 
Nome: Lucas dos Santos Sousa RA: 1902348 
Nome: Kennedy da Silva Cardoso RA: 1901697 
Nome: Maria Vitoria Ferreira da Silva RA: 1901934
>>>>>>> 07d35e629919e75102471ad1fe1f468161380ec5
