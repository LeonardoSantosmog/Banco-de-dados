import sqlite3 as sq

DB_PATH = 'alunos.db'

def get_connection():
    return sq.connect(DB_PATH)

def inserir_aluno(nome, idade, email, curso):
    with get_connection() as conn:
        cur = conn.cursor()
        cur.execute('''
            INSERT INTO alunos (nome, idade, email, curso)
            VALUES (?, ?, ?, ?);
        ''', (nome, idade, email, curso))
        conn.commit()
        return cur.lastrowid
    
if __name__ == '__main__':
    #Bem vindo ao banco de dados
    print("### Bem vindo ao banco de dados ###")
    nome = input("Nome do aluno: ")
    idade = int(input("Idade do aluno: "))
    email = input("Email do aluno: ")
    curso = input("Curso do aluno: ")
   
    novo_id = inserir_aluno(nome, idade, email, curso)