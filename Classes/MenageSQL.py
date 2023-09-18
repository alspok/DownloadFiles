import mysql.connector

class MenageSQL():

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
    
    def createTable(self, conn: object, table_name: str) -> None:
        table_columns = f"(id INT(11) NOT NULL AUTO_INCREMENT PRIMARY KEY," \
                        "company char(255)," \
                        "ean char(255)," \
                        "sku char(255)," \
                        "category char(255)," \
                        "manufacturer varchar(500)," \
                        "title varchar(2000)," \
                        "stock char(255), " \
                        "price char(255)," \
                        "weight char(255)," \
                        "time_stamp TIMESTAMP DEFAULT CURRENT_TIMESTAMP);"
        
        cursor = conn.cursor()
        query = f"Create table if not exists {table_name} {table_columns}"
        cursor.execute(query)
        conn.commit()

        pass
    
    def createLinkTable(self, conn: object, table_name: str) -> None:
        table_columns = f"(id INT(11) NOT NULL AURO_INCREMENT PRIMARY KEY," \
                        "company char(255)," \
                        "margin char(255)," \
                        "min_price char(255)," \
                        "stock char(255)," \
                        "time_stamp TIMESTAMP DEFAULT CURRENT_TIMESTAMP);"
                        
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

    def insertTable(self, conn: object, table_name: str, path: str) -> None:
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
                        row[5] = row[5].replace(';', '').replace('&', '')
                        query = f"insert into {table_name} (company, ean, sku, category, manufacturer, title, stock, price, weight) values (%s,%s,%s,%s,%s,%s,%s,%s,%s)"
                        cursor.execute(query, row)
                    conn.commit()

        cursor.close()

        pass