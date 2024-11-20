from flask import Flask, render_template, request, redirect, url_for
import sqlite3
from datetime import datetime
import pytz

app = Flask(__name__, static_folder='static')

# Configuração do banco de dados
DB_NAME = 'barbearia.db'

def add_servico():
    funcionario_id = request.form['funcionario']
    servico_id = request.form['servico']

    # Configurar o fuso horário de Brasília
    brasilia_tz = pytz.timezone('America/Sao_Paulo')
    
    # Obter a hora atual e ajustar para o fuso horário de Brasília
    data_atual = datetime.now(brasilia_tz).strftime('%Y-%m-%d %H:%M:%S')

    # Insira os dados no banco de dados
    conn = sqlite3.connect(DB_NAME)
    cursor = conn.cursor()
    
    cursor.execute("""
        INSERT INTO historico (funcionario_id, servico_id, data)
        VALUES (?, ?, ?)
    """, (funcionario_id, servico_id, data_atual))
    
    conn.commit()
    conn.close()

    return redirect(url_for('index'))  # Redireciona de volta para a página principal


# Página inicial
@app.route('/')
def index():
    # Pega o número da página, se não existir, começa na página 1
    page = int(request.args.get('page', 1))
    items_per_page = 10  # Número de itens por página

    # Conectar ao banco de dados
    conn = sqlite3.connect(DB_NAME)
    cursor = conn.cursor()
    
    # Buscar funcionários e serviços
    cursor.execute("SELECT * FROM funcionarios")
    funcionarios = cursor.fetchall()
    
    cursor.execute("SELECT * FROM servicos")
    servicos = cursor.fetchall()

    # Consultar o histórico com paginação
    offset = (page - 1) * items_per_page
    cursor.execute("""
        SELECT r.id_relacao, f.nome, s.descricao, s.valor, r.data
        FROM relacoes r
        JOIN funcionarios f ON r.id_funcionario = f.id_funcionario
        JOIN servicos s ON r.id_servico = s.id_servico
        ORDER BY r.data DESC
        LIMIT ? OFFSET ?
    """, (items_per_page, offset))
    historico = cursor.fetchall()

    # Pega o total de registros para calcular o número de páginas
    cursor.execute("""
        SELECT COUNT(*) FROM relacoes
    """)
    total_registros = cursor.fetchone()[0]
    total_paginas = (total_registros // items_per_page) + (1 if total_registros % items_per_page > 0 else 0)

    conn.close()
    
    return render_template('index.html', funcionarios=funcionarios, servicos=servicos, historico=historico, page=page, total_paginas=total_paginas)


# Rota para adicionar uma relação
@app.route('/add', methods=['POST'])
def add():
    funcionario_id = request.form['funcionario']
    servico_id = request.form['servico']
    
    # Inserir no banco de dados
    conn = sqlite3.connect(DB_NAME)
    cursor = conn.cursor()
    cursor.execute("""
        INSERT INTO relacoes (id_funcionario, id_servico) VALUES (?, ?)
    """, (funcionario_id, servico_id))
    conn.commit()
    conn.close()

    return redirect(url_for('index'))

# Rota para relatório de caixa por funcionário
@app.route('/relatorio')
def relatorio():
    conn = sqlite3.connect(DB_NAME)
    cursor = conn.cursor()
    
    cursor.execute("""
        SELECT f.nome, SUM(s.valor) AS total_caixa
        FROM relacoes r
        JOIN funcionarios f ON r.id_funcionario = f.id_funcionario
        JOIN servicos s ON r.id_servico = s.id_servico
        GROUP BY f.nome
    """)
    relatorio_caixa = cursor.fetchall()
    
    conn.close()
    return render_template('relatorio.html', relatorio_caixa=relatorio_caixa)

@app.route('/reset-historico', methods=['POST'])
def reset_historico():
    # Conectar ao banco e apagar o histórico
    conn = sqlite3.connect(DB_NAME)
    cursor = conn.cursor()
    
    # Apagar todos os registros da tabela relacoes
    cursor.execute("DELETE FROM relacoes")
    conn.commit()  # Confirma a mudança
    conn.close()
    
    # Redireciona de volta para a página inicial
    return redirect(url_for('index'))

if __name__ == '__main__':
    app.run(debug=True)
