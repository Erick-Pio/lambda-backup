import psycopg2
import pandas as pd

def conexao():
    dbname = 'autoprovision'
    user = 'autoprovision_adm'
    password = 'urubu100'
    host = 'localhost'

    try:
        connection = psycopg2.connect(dbname=dbname, user=user, password=password, host=host)
        print("Conexão bem sucedida")
        return connection
    except psycopg2.Error as e:
        print("Erro: ", e)
        return None

def dataframe():
    conn = conexao()  
    if conn is None:
        return  

    cursor = conn.cursor()

    cursor.execute("select * from user_info;")

    rows = cursor.fetchall()

    columns = [desc[0] for desc in cursor.description]

    df = pd.DataFrame(rows, columns=columns)
    print(df)

    cursor.close()
    conn.close()

    return df

def aprovar():

    conn = conexao()  
    if conn is None:
        return  

    cursor = conn.cursor()

    inserir_aprovar = cursor.execute(f'''insert into user_new_loan (user_id, parcelas)
                   values({user_id}, {parcelas} )''')
    
    cursor.close()
    conn.close()
    
    return inserir_aprovar

def reprovar():

    conn = conexao()
    if conn is None:
        return
    
    cursor = conn.cursor()

    inserir_desaprovar = cursor.execute(f'''insert into user_new_loan (user_id, parcelas)
                                            values({user_id}, {ultimo_pedido} )''')

    cursor.close()
    conn.close()

    return inserir_desaprovar

def analise():
    df = dataframe()   
    
    for i, row in df.iterrows():

        idade = int((row['idade']))
        valor_emprestado = row['valor_emprestado']
        margem_loan = row['margem_loan']

        if idade < 65 and valor_emprestado > margem_loan:
            match row['convenio']:
                case 'basico':
                    parcelas = 3
                case 'intermediario':
                    parcelas = 5
                case 'premium':
                    parcelas = 7
                case _:
                    parcelas = 10
            aprovar()

            print(f'O empréstimo do {row['nome']} não foi aprovado')
        else:
            reprovar()
            print(f'O empréstimo do {row['nome']} foi aprovado')


analise()  