from flask import Flask, request, jsonify, send_from_directory
import json

app = Flask(__name__)

# Lista de tarefas em memória
lista_tarefas = []

@app.route('/')
def homepage():
    return send_from_directory('.', 'index.html')

@app.route('/blog')
def blog():
    return send_from_directory('.', 'blog.html')

@app.route('/adicionar_tarefa', methods=['POST'])
def adicionar_tarefa():
    data = request.get_json()
    tarefa = data.get('tarefa')
    if tarefa:
        lista_tarefas.append(tarefa)
    return jsonify({'lista_tarefas': lista_tarefas})

@app.route('/deletar/<int:posicao>', methods=['DELETE'])
def deletar(posicao):
    if len(lista_tarefas) > posicao:
        lista_tarefas.pop(posicao)
    return jsonify({'lista_tarefas': lista_tarefas})

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
