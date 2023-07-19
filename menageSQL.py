from Classes.MenageSQL import MenageSQL as msql
from datetime import datetime

def menageSQL() -> None:
    table_name = 'e_deals_tbl'
    path = '/var/pythonapps/ModDataFiles/'

    start_time = datetime.now()

    modFiles = []
    conn = msql().connectDB()
    msql().dropTable(conn, table_name)
    msql().createTable(conn, table_name)

    modFiles = msql().insertTable(conn, table_name, path)
    # MenageSQL().dropTable(conn, table_name)
    conn.close()

    end_time = datetime.now()
    diff_time = end_time - start_time
    print (f"Time of mysql proccess: {diff_time}")

    return modFiles

if __name__ == '__main__':
    menageSQL()