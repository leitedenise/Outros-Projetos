from datetime import datetime

import mysql.connector
con = mysql.connector.connect(host='local', user='usuario', password='senha', database='nome do banco')
cursor = con.cursor()

if not con.is_connected():
    print('Falha ao conectar ao banco de dados.')

def criarBD():
    try:
        db = """CREATE DATABASE agenda"""

        cursor.execute(db)
        print('Banco de dados criado com sucesso.')

    except mysql.connector.Error as erro:
        print(erro)


def criarTabela():
    try:
        tabela = """CREATE TABLE agendamentos (
                        id int not null auto_increment,
                        data date not null,
                        horario varchar (10) not null,
                        nome varchar (30) not null,
                        telefone varchar (15) not null,
                        servico text not null,
                        primary key(id) 
                        )                  
                        """

        cursor.execute(tabela)
        print('Tabela de agendamentos criada com sucesso.')

    except mysql.connector.Error as erro:
        print(erro)

criarBD()
criarTabela()

def agendamento():
    while True:
        print('\nInforme os dados para o agendamento: ')
        data = input('Data (no formato (0000-00-00): ')
        horario = input('Horário (no formato 00:00): ')
        nome = input('Nome completo: ')
        telefone = input('Telefone com DDD (00) 00000-0000: ')
        servico = input('Serviço a ser agendado: ')


        try:
            dados = "INSERT INTO agendamentos values (default, '"+data+"','"+horario+"','"+nome+"','"+telefone+"','"+servico+"')"
            cursor.execute(dados)
            print('\nAgendamento realizado com sucesso.')
            cursor.execute("select max(id) from agendamentos")
            id = cursor.fetchall()

            print(f'Identificador do agendamento (Guarde o número do agendamento): {id}')


        except mysql.connector.Error as erro:
            print(erro)


        opc = input('\nDeseja agendar outro serviço? (s/n): ').upper()
        if opc == 'N':
            break

def alteraAgendamento():
    while True:
        print('\nInforme a opção de alteração que deseja realizar no agendamento: ')
        print('1- Data '
              '\n2- Horário '
              '\n3- Serviço ')
        op = int(input('Opção: '))

        if op == 1:
            diaAtual = int(datetime.today().strftime('%d'))
            diaAgendamento = int(input('Informe o dia do seu horário já agendado (no formato 00): '))

            if diaAgendamento - diaAtual >= 2:
                identificador = input('informe o número identificador do seu agendamento: ')
                dataMod = input('Informe a nova data em que deseja realizar o agendamento (no formato 0000-00-00): ')

                cursor.execute("update agendamentos set data = '"+dataMod+"' where id= '"+identificador+"'")
                print('\nAlteração realizada com sucesso.')

            else:
                print('\nAlteração de horário permitida somente por telefone. Favor entrar em contato com o salão.')

        elif op == 2:
            diaAtual = int(datetime.today().strftime('%d'))
            diaAgendamento = int(input('Informe o dia do seu horário já agendado (no formato 00): '))

            if diaAgendamento - diaAtual >= 2:
                identificador = input('informe o número identificador do seu agendamento: ')
                hora = input('Informe o horário para o qual deseja alterar seu atendimento: ')

                cursor.execute("update agendamentos set horario = '"+hora+"' where id = '"+identificador+"'")
                print('\nAlteração realizada com sucesso.')

            else:
                print('\nAlteração de horário permitida somente por telefone. Favor entrar em contato com o salão.')

        elif op == 3:
            diaAtual = int(datetime.today().strftime('%d'))
            diaAgendamento = int(input('Informe o dia do seu horário já agendado (no formato 00): '))

            if diaAgendamento - diaAtual >= 2:
                identificador = input('informe o número identificador do seu agendamento: ')
                servico = input('Informe o serviço que deseja agendar: ')

                cursor.execute("update agendamentos set servico = '" + servico + "' where id = '" + identificador + "'")
                print('\nAlteração realizada com sucesso.')

            else:
                print('\nAlteração de horário permitida somente por telefone. Favor entrar em contato com o salão.')

        opc = input('\nDeseja realizar mais alguma alteração? (s/n): ').upper()
        if opc == 'N':
            break

def historicoAgendamento():
        dataI = input('Informe a data inicial do período que deseja consultar (no formato 0000-00-00): ')
        dataF = input('Informe a data final do período que deseja consultar (no formato 0000-00-00): ')

        cursor.execute("select * from agendamentos where data between '"+dataI+"' and '"+dataF+"' order by data")
        print(f'{cursor.fetchall()}\n')

while True:
    print('\nBem vindo ao sistema de agendamento On-line do salão da Leila\n\nEscolha uma das opções: ')
    print('1-Agendamento'
         '\n2- Alteração do agendamento'
        '\n3- Histórico de agendamentos'
        )
    op = int(input('Opção: '))
    if op == 1:
        agendamento()
    elif op == 2:
        alteraAgendamento()
    elif op ==3:
        historicoAgendamento()
    else:
        print('opção inválida.')

    opc = input('\nDeseja voltar ao menu inicial?(s/n): ').upper()
    if opc == 'N':
        print('Sistema finalizado com sucesso.')
        break


con.close()
cursor.close()


