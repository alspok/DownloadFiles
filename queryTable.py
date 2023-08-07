from Classes.MenageSQL import MenageSQL as msql

def queryTable(table_name: str, output_filename: str) -> None:
    conn = msql().connectDB()
    query = f"select manufacturer from {table_name}"
    cursor = conn.cursor()
    result = cursor.execute(query)
    conn.commit()
    cursor.close()

    with open(output_filename, mode='w', encoding='utf-8') as outfh:
        for row in result:
            outfh.writeline(row)

    pass

if '__name__' == '__main':
    queryTable('e_deals_tbl', 'Temp/data.txt')
    
