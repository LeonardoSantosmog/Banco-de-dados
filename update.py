import sqlite3 as sq

DB_PATH = 'alunos.db'

def get_connection():
    return sq.connect(DB_PATH)

def atualizar_aluno(nome, idade, email, curso, id):
    with get_connection() as conn:
        cursor = conn.cursor()
        cursor.execute(
            '''
            UPDATE alunos
            SET nome = ?, idade = ?, email = ?, curso = ?
            WHERE id = ?
            ''',
            (nome, idade, email, curso, id)
        )
        conn.commit()
        return cursor.rowcount

if __name__ == '__main__':
    print("### Bem vindo ao banco de dados ###")
    id = int(input("ID do aluno a ser atualizado: "))
    nome = input("Novo nome do aluno: ")
    idade = int(input("Nova idade do aluno: "))
    email = input("Novo email do aluno: ")
    curso = input("Novo curso do aluno: ")
   
qtd = atualizar_aluno(nome, idade, email, curso, id)
if qtd:
    print(f"{qtd} aluno(s) atualizado(s) com sucesso!")
else:
    print("Nenhum aluno encontrado com esse ID.")