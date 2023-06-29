from Classes.MenageSQL import MenageSQL as msql
import os

def menageSQL() -> None:
    table_name = 'e_deals_tbl'
    path = '/var/pythonapps/ModDataFiles/'

    conn = msql().connectDB()
    msql().createTable(conn, table_name)

    file_list = os.listdir(path)
    for file in file_list:
        msql().insertTable(conn, table_name, path, file)
    # MenageSQL().dropTable(conn, table_name)
    conn.close()

    pass

if __name__ == '__main__':
    menageSQL()