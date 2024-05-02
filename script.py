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
    return df

def aprovar():
    conn = conexao()  
    if conn is None:
        return  

    cursor = conn.cursor()

    cursor.execute("insert into  * from user_new_loan;")


def analise():
    df = dataframe()   
    

    for i, row in df.iterrows():
        salario = row['salario']
        idade = int((row['idade']))
        if idade > 65:
            # margem_loan = str(salario * 0.45)
            # margem = []
            # margem.append(margem_loan)
            # print(margem)
            # print(margem_loan)
            print(f'O empréstimo do {row['nome']} não foi aprovado')
        else:
            print(f'O empréstimo do {row['nome']} foi aprovado')


analise()  