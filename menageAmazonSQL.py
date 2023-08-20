from Classes.MenageAmazonSQL import MenageAmazonSQL as msql
from datetime import datetime

def menageAmazonSQL() -> None:
    table_name = "e_amazon_tbl"
    path = "/var/DownloadFiles/AmazonFiles"

    conn = msql().connectDB()
    msql().dropAmazonTable(conn, table_name)
    msql().createAmazonTable(conn, table_name)

    msql().insertAmazonTable(conn, table_name, path)

    conn.close()

    pass

if __name__ == '__main__':
    menageAmazonSQL()