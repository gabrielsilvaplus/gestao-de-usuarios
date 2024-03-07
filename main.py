from flask import Flask, url_for, render_template

app = Flask(__name__)

@app.route('/')
def ola_mundo():
    titulo = "Gestão de Usuários"
    usuarios = [
        {"nome": "Gabriel", "membro_ativo": True},
        {"nome": "Luiz", "membro_ativo": False},
        {"nome": "Adriano", "membro_ativo": False},
        ]
    return render_template('index.html', titulo=titulo, usuarios=usuarios)

@app.route('/sobre')
def pagina_sobre():
    return """ 
        <b> Programador Gabriel Pereira</b>: entre no meu github <a href="https://github.com/gabrielsilvaplus"> My GIT Hub</a>
 """

app.run(debug=True)

