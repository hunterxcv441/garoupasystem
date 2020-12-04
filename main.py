import sqlite3
import time
import pandas as pd
import sys
#import back
#from back import write
import pyfiglet
# conectando...
dbase = sqlite3.connect('estacionamento.db')
c = dbase.cursor()
linha = '-' * 77
print("\n" * 10)
ascii_banner = pyfiglet.figlet_format("GAROUPA")
print(ascii_banner)
inicio = input('Iniciar Programa(S/N): ')

def menu():
    try:
        if (inicio == 'S' or 's'):
            print(ascii_banner)
            print('\n')
            print("1) Cadastrar Clientes")
            print("2) Editar registro de caixa")
            print("3) Sair \n")
            menu1 = input('>: ')
            if (menu1 == '1'):
                print('Cadastro \n')
                cadclientes = input('Voltar para o Menu(S/N): ')
                if (cadclientes == 'S'):
                    print("\n" * 130)
                    menu()
            if (menu1 == '2'):
                print("\n" * 130)
                print(ascii_banner)
                print('\n')
                print('Editar registro:\n')
                print('1) Inserir registros: ')
                print('2) Excluir registros: ')
                print('3) Visualizar registros: ')
                print('\n')
            if (menu1 == '3'):
                print('Saindo...')
                dbase.close()
                time.sleep(3)
                exit()
            ############################## MENU 2 #################################
            menu2 = input('>: ')
            if (menu2 == '1'):  ##  1) Inserir registros
                print("\n" * 130)
                print(ascii_banner)
                print('\n')
                try:
                    id = input('ID: ')
                    criado_em = input('Data(AAAA-MM-DD): ')
                    prod = input('Produto: ')
                    obs = input('OBS: ')
                    formapag = input('Forma de pagamento: ')
                    valor = input('Valor: ')
                    funcr = input('funcionário: ')
                    c.execute(
                        ''' INSERT into estacionamento(id, criado_em, prod, obs, formapag, valor, funcr) VALUES(?, ?, ?, ?, ?, ?, ?)''',
                        (id, criado_em, prod, obs, formapag, valor, funcr))
                    dbase.commit()
                    print("\n")
                    print('Produto registrado!')
                    cadclientes = input('Voltar para o Menu(S/N): ')
                    if (cadclientes == 'S'):
                        print("\n" * 130)
                        menu()
                except:
                    print('ERROR!')
                    menu()
                cadclientes = input('Voltar para o Menu(S/N): ')
                if (cadclientes == 'S' or 's'):
                    print("\n" * 130)
                    menu()
            if (menu2 == '2'):  ##2) Excluir registros
                print("\n" * 130)
                print(ascii_banner)
                print('\n')
                delid = input('Digite o Codigo do produto a ser excluido:> ')
                c.execute(''' DELETE FROM estacionamento WHERE id = ?''', (delid))
                ###inpt
                dbase.commit()
                print('Produto excluido!\n')
                cadclientes = input('Voltar para o Menu(S/N): ')
                if (cadclientes == 'S' or 's'):
                    print("\n" * 130)
                    menu()
            if (menu2 == '3'):  ## 3) Visualizar registros
                print("\n" * 130)
                print(ascii_banner)
                print('\n')
                print('1) Visualizar Todos os registros:')
                print('2) Visualizar registros ordenados por data:')
                print('3) Visualizar registros ordenados por funcionário:')
                print('4) Visualizar registros ordenados por obs:')
                menuvis1 = input('>: ')
                if (menuvis1 == '1'):
                    print("\n" * 130)
                    print(ascii_banner)
                    print('\n')
                    print(pd.read_sql_query(
                        "SELECT id, criado_em, prod, obs, formapag, valor, funcr FROM estacionamento",
                        dbase))
                    dbase.commit()
                    print("\n")
                if (menuvis1 == '2'):
                    print("\n" * 130)
                    print(ascii_banner)
                    print('\n')
                    print('Buscar registros por data:\n')
                    data1 = input('De(AAAA-MM-DD): ')
                    data2 = input('Até(AAAA-MM-DD): ')
                    print("\n" * 2)
                    # df = pd.read_sql_query( "SELECT * FROM estacionamento WHERE criado_em BETWEEN 2020/10/1 AND 2020/10/30", dbase)
                    sql = """SELECT * FROM estacionamento WHERE criado_em BETWEEN ? AND ?"""
                    df1 = pd.read_sql_query(sql, dbase, params=[data1, data2])
                    print(df1)
                    dbase.commit()
                    print("\n")
                if (menuvis1 == '3'):
                    print("\n" * 130)
                    print(ascii_banner)
                    print('\n')
                    print('Buscar registros por Funcionário:\n')
                    func = input('Funcionário(PGG,PGA,PGT): ')
                    print("\n" * 2)
                    sql2 = """SELECT * FROM estacionamento WHERE funcr = ?"""
                    df2 = pd.read_sql_query(sql2, dbase, params=[func])
                    print(df2)
                    dbase.commit()
                    print("\n")
                if (menuvis1 == '4'):
                    print("\n" * 130)
                    print(ascii_banner)
                    print('\n')
                    print('Buscar registros por OBS:\n')
                    obsinpt = input('Buscar registros por nome do produto/obs: ')
                    print("\n" * 2)
                    sql3 = """SELECT * FROM estacionamento WHERE obs = ?"""
                    df3 = pd.read_sql_query(sql3, dbase, params=[obsinpt])
                    print(df3)
                    dbase.commit()
                    print("\n")
                cadclientes = input('Voltar para o Menu(S/N): ')
                if (cadclientes == 'S' or 's'):
                    print("\n" * 130)
                    menu()  #
    except:
        print('ERROR: COD:1\n Reniciando Módulo')
        time.sleep(3)
        print("\n" * 130)
        menu()

def exit():
    print('TESTANDO')
    sys.exit()
print("\n" * 130)
menu()





