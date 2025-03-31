import cx_Oracle

def pega_credenciais():
    # em vez de pegar por input, pode colocar suas credenciais aqui direto
    print('Insira suas credenciais no Oracle da FIAP!')
    user =  'RM560088'
    senha = '061005'
    return user, senha

def abre_conexao(user, senha):
    # dsn é "data source name", um descritor de onde vamos acessar o BD
    dsn = cx_Oracle.makedsn(host='oracle.fiap.com.br', port=1521, service_name='ORCL')
    return cx_Oracle.connect(user, senha, dsn)

def busca_tudo(cursor, tabela):
    query = f'SELECT * FROM {tabela}'
    cursor.execute(query)
    return cursor.fetchall() # pega todos os resultados da query acima!

def insere_dado(conexao, cursor, pessoa, tabela):
    # pessoa é dicionário com campos "id", "nome" e "ano_ingresso"
    query = f"""
        INSERT INTO {tabela} (id, nome, ano_ingresso)
        VALUES (:1, :2, :3)
    """
    cursor.execute(query, (pessoa['id'], pessoa['nome'], pessoa['ano_ingresso']))
    conexao.commit() # preciso dar commit após alterações na tabela

def main():
    user, senha = pega_credenciais()
    conexao = abre_conexao(user, senha)
    print(f'Conexão bem-sucedida com user {conexao.username} do BD.')

    cursor = conexao.cursor()

    pessoa = {
        'id' : 321,
        'nome' : 'Luiza',
        'ano_ingresso' : 1998
    }
    insere_dado(conexao, cursor, pessoa, 'funcionarios')

    resultados = busca_tudo(cursor, 'funcionarios')
    for resultado in resultados:
        print(resultado)
    
    cursor.close()
    conexao.close()

main()