# Banco de dados criado com xampp

# usuário 'root'
# senha ''

# query padrão: INSERT INTO `mostra` (`Dia`, `Url`) VALUES (current_timestamp(), 'AQUI VAI A URL');

#banco de dados: Mostra
# tabela: mostra

import mysql.connector

def save_in_db(url, rating):
    try:
        cnx = mysql.connector.connect(
            host='127.0.0.1',
            user='root',
            password='',
            database='Mostra'
        )
        print("Conexão bem sucedida!")

        cursor = cnx.cursor()
        cursor.execute(f"INSERT INTO `mostra` (`Dia`, `Url`, `Rating`, `Id`) VALUES (current_timestamp(), '{url}', '{rating}', NULL);")

        cnx.commit()  # <- ESSENCIAL!
        print("Inserção realizada com sucesso!")

    except mysql.connector.Error as err:
        print(f"Ocorreu um erro: {err}")

    finally:
        if 'cursor' in locals() and cursor:
            cursor.close()
        if 'cnx' in locals() and cnx.is_connected():
            cnx.close()
            print("Fechando conexão com o banco!")
