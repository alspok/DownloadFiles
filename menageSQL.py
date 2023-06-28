from Classes.MenageSQL import MenageSQL as msql
from Classes.InitValues import InitValues as iv
import os

def menageSQL() -> None:
    table_name = 'e_deals_tbl'
    path = '/var/pythonapps/ModDataFiles'

    conn = msql().connectDB()
    msql().createTable(conn, table_name)

    file_list = os.listdir(path)
    for file in file_list:
        msql().insertTable(conn, table_name, file)
    # MenageSQL().dropTable(conn, table_name)

    pass

if __name__ == '__main__':
    menageSQL()