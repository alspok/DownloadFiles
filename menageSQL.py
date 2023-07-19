from Classes.MenageSQL import MenageSQL as msql
import os

def menageSQL() -> None:
    table_name = 'e_deals_tbl'
    path = '/var/pythonapps/ModDataFiles/'

    modFiles = []
    conn = msql().connectDB()
    msql().dropTable(conn, table_name)
    msql().createTable(conn, table_name)

    modFiles = msql().insertTable(conn, table_name, path)
    # MenageSQL().dropTable(conn, table_name)
    conn.close()

    return modFiles

if __name__ == '__main__':
    menageSQL()