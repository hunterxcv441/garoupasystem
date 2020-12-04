import sqlite3
dbase = sqlite3.connect('estacionamento.db')
# Criar a e ativa a nossa database
c = dbase.cursor()
dbase.execute("""
CREATE TABLE IF NOT EXISTS estacionamento (
        id INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,
        criado_em DATE NOT NULL,
        prod TEXT NOT NULL,
        obs TEXT,
        formapag TEXT NOT NULL,
        valor INTEGER NOT NULL,
        funcr TEXT NOT NULL
);
""")
print('Tabela criada com sucesso.')

# Aplica todas as mudanças na nossa database
dbase.commit()


# Função que escreve ID NAME dentro da database
#def write(id,criado_em,prod,obs,formapag,valor,funcr):
    #def write(id, criado_em, prod, obs, formapag, valor, funcr):
        #id = input('ID: ')
        #criado_em = input('Data: ')
        #prod = input('Produto: ')
        #obs = input('OBS: ')
       # formapag = input('Forma de pagamento: ')
       # valor = input('Valor: ')
      #  funcr = input('funcionário: ')
      #  c.execute(
       #     ''' INSERT into estacionamento(id, criado_em, prod, obs, formapag, valor, funcr) VALUES(?, ?, ?, ?, ?, ?, ?)''',
       #     (id, criado_em, prod, obs, formapag, valor, funcr))
      #  dbase.close()


#def delete(x):
  #  c.execute('''delete from estacionamento where NAME=?''', x)
   # dbase.commit()


def read_task():
    c = dbase.cursor()
    c.execute('''SELECT * FROM estacionamento''')
    data = c.fetchall()
    dbase.commit()
    return data

def testando():
    for linha in c.fetchall():
        print(linha)
    dbase.close()