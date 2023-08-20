import mysql.connector

class MenageAmazonSQL():

    def connectDB(self) -> object:
        conn = mysql.connector.connect(
            user = 'doadmin',
            password = 'AVNS_IzETuacH57EOU-TThcJ',
            host = 'db-mysql-fra1-42194-do-user-14106707-0.b.db.ondigitalocean.com',
            port = 25060,
            database = 'e_deals_db'
        )
        
        cursor = conn.cursor()
        cursor.execute("set time_zone = 'Europe/Vilnius'")

        return conn

    def createAmazonTable(self, conn: object, table_name: str) -> None:
        table_columns = f"(id INT(11) )NOT NULL AUTO_INCREMENT PRIMARY KEY," \
                        "ean char(255)," \
                        "asins char(255)," \
                        "name varchar(2000)," \
                        "cost char(255));"

        cursor = conn.cursor()
        query = f"Create table if not exists {table_name} {table_columns}"
        cursor.execute(query)
        conn.commit()

        pass

    def dropTable(self, conn: object, table_name: str) -> None:
        query = f"drop table if exists {table_name}"
        cursor = conn.cursor()
        cursor.execute(query)
        conn.commit()

        cursor.close()

        pass

    def insertAmazon
    Table(self, conn: object, table_name: str, path: str) -> None:
        import csv
        import os

        dir_list = os.listdir(path)

        for file in dir_list:
            if file == ".gitkeep":
                continue
            else:
                with open(f"{path}{file}", mode='r', encoding='utf-8', errors='ignore') as csvfh:
                    next(csvfh)
                    reader = csv.reader(csvfh, delimiter=';')
                    cursor = conn.cursor()
                    for row in reader:
                        query = f"insert into {table_name} (ean, asins, name, cost) values (%s,%s,%s,%s)"
                        cursor.execute(query, row)
                    conn.commit()

        cursor.close()

        pass

