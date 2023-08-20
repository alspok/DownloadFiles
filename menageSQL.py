from Classes.MenageSQL import MenageSQL as msql
from datetime import datetime

def menageSQL() -> None:
    table_name = "e_deals_tbl"
    path = "/var/DownloadFiles/ModDataFiles/"

    conn = msql().connectDB()
    msql().dropTable(conn, table_name)
    msql().createTable(conn, table_name)

    msql().insertTable(conn, table_name, path)
    # MenageSQL().dropTable(conn, table_name)
    conn.close()

    pass

def menageAmazonSQL() -> None:
    table_name = "e_amazon_tbl"
    path = "/var/DownloadFiles/AmazonFiles"
    /var/DownloadFiles/AmazonFiles

if __name__ == '__main__':
    menageSQL()