import sqlite3

# Conectando ao banco de dados
conn = sqlite3.connect('equipamentos_eletromédico.db')
conexao = conn.cursor()

# Criando a tabela de equipamentos
conexao.execute('''
    CREATE TABLE IF NOT EXISTS equipamentos_eletromédico (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        nome TEXT NOT NULL,
        descricao TEXT,
        quantidade INTEGER NOT NULL
    )
''')

# Função para criar um novo equipamento


def create_equipment(nome, descricao, quantidade):
    conexao.execute('''
        INSERT INTO equipamentos_eletromédico (nome, descricao, quantidade)
        VALUES (?, ?, ?)
    ''', (nome, descricao, quantidade))
    conn.commit()
    print("Equipamento criado com sucesso!")

# Função para listar todos os equipamentos


def read_equipment():
    conexao.execute('SELECT * FROM equipamentos_eletromédico')
    equipamentos = conexao.fetchall()
    if len(equipamentos) > 0:
        for equipamento in equipamentos:
            print(f"ID: {equipamento[0]}")
            print(f"Nome: {equipamento[1]}")
            print(f"Descrição: {equipamento[2]}")
            print(f"Quantidade: {equipamento[3]}")
            print("==============================")
    else:
        print("Nenhum equipamento encontrado.")

# Função para atualizar um equipamento


def update_equipment(equipamento_id, nome, descricao, quantidade):
    conexao.execute('''
        UPDATE equipamentos_eletromédico
        SET nome = ?, descricao = ?, quantidade = ?
        WHERE id = ?
    ''', (nome, descricao, quantidade, equipamento_id))
    conn.commit()
    print("Equipamento atualizado com sucesso!")

# Função para deletar um equipamento


def delete_equipment(equipamento_id):
    conexao.execute(
        'DELETE FROM equipamentos_eletromédico WHERE id = ?', (equipamento_id,))
    conn.commit()
    print("Equipamento deletado com sucesso!")


# Exemplo de uso
create_equipment("Monitor", "Monitor Cardiaco Philips Efficia", 15)
create_equipment("Eletrocardiógrafo", "Eletrocardiógrafo EP3 Dixtal", 10)
create_equipment("Oximetro de Pulso", "Oximetro de Pulso OXP-10 Emai", 5)
create_equipment("Aparelho de pressão", "Aparelho de pressão UNITEC", 50)
create_equipment("Eletroencefalograma", "Eletroencefalograma Neurovirtual", 2)
create_equipment("Bisturi Elétrico", "Bisturi Elétrico Wen", 10)
read_equipment()
update_equipment(1, "", "", 8)
delete_equipment(2)

# Fechando a conexão com o banco de dados
conn.close()
