# 🧑‍🎓 Sistema de Gerenciamento de Alunos (SQLite + Python)

Este projeto é um sistema simples em Python para gerenciar um banco de dados de alunos utilizando **SQLite**.  
Ele permite **criar a tabela**, **inserir**, **atualizar** e **deletar** registros de forma fácil e interativa.

---

## 📁 Estrutura do Projeto

```
📦 alunos_db/
├── alunos.db         # Banco de dados SQLite
├── create.py         # Criação da tabela
├── insert.py         # Inserção de alunos
├── update.py         # Atualização de alunos
├── delete.py         # Exclusão de alunos
```

---

## ⚙️ Pré-requisitos

- Python 3.x instalado
- Biblioteca `sqlite3` (já inclusa no Python por padrão)

---

## 🚀 Como usar

1. **Clone este repositório:**
   ```bash
   git clone https://github.com/seu-usuario/alunos_db.git
   cd alunos_db
   ```

2. **Crie o banco e a tabela:**
   ```bash
   python create.py
   ```

3. **Inserir um novo aluno:**
   ```bash
   python insert.py
   ```

4. **Atualizar dados de um aluno:**
   ```bash
   python update.py
   ```

5. **Deletar um aluno:**
   ```bash
   python delete.py
   ```

---

## 📜 Códigos Fonte

### 🛠️ create.py
```python
import sqlite3 as sq

DB_PATH = 'alunos.db'

def get_connection():
    return sq.connect(DB_PATH)

def criar_tabela():
    with get_connection() as conn:
        conn.execute('''
            CREATE TABLE IF NOT EXISTS alunos (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                nome TEXT NOT NULL,
                idade INTEGER NOT NULL,
                email TEXT UNIQUE NOT NULL,
                curso TEXT NOT NULL
            );     
        ''')

criar_tabela()
```

---

### ✍️ insert.py
```python
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
    print("### Bem vindo ao banco de dados ###")
    nome = input("Nome do aluno: ")
    idade = int(input("Idade do aluno: "))
    email = input("Email do aluno: ")
    curso = input("Curso do aluno: ")
   
    novo_id = inserir_aluno(nome, idade, email, curso)
    print(f"Aluno inserido com ID: {novo_id}")
```

---

### 🔄 update.py
```python
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
```

---

### ❌ delete.py
```python
import sqlite3 as sq

DB_PATH = 'alunos.db'

def get_connection():
    return sq.connect(DB_PATH)

def deletar_aluno(id):
    with get_connection() as conn:
        cursor = conn.execute(
            '''
            DELETE FROM alunos
            WHERE id = ?
            ''',
            (id,)
        )
        return cursor.rowcount > 0
    
if __name__ == '__main__':
    print("### Bem vindo ao banco de dados ###")
    id = int(input("ID do aluno a ser deletado: "))
   
    if deletar_aluno(id):
        print("Aluno deletado com sucesso!")
    else:
        print("Nenhum aluno encontrado com esse ID.")
```

---

## 📄 Licença

Este projeto é de uso livre para fins educacionais e pessoais. ✌️
