import sqlite3 as sq

DB_PATH = 'alunos.db'

def get_connection():
    return sq.connect(DB_PATH)

def deletar_aluno(id):
    with get_connection() as conn:
        cursor = conn.execute(
            '''
            DELETE FROM alunos
            WHERE id + ?
            ''',
            (id,)
        )
        return cursor.rowcount > 0
    
if __name__ == '__main__':
    print("### Bem vindo ao banco de dados ###")
    id = int(input("ID do aluno a ser deletado: "))
   
deletar_aluno(id)