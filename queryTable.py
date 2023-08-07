from Classes.MenageSQL import MenageSQL as msql

def queryTable(table_name: str, output_filename: str) -> None:
    conn = msql().connectDB()
    query = f"select manufacturer from {table_name}"
    cursor = conn.cursor()
    cursor.execute(query)
    result = cursor.fetchall()
    set_result = list(set(result))

    duplicate_result = {}
    for i in set(result):
        duplicate_result[i] = result.count(i)

    with open(output_filename, mode='w', encoding='utf-8') as outfh:
        i = 1
        for key, value in duplicate_result.items():
            outfh.write(f"{i}\t{key}\t{value}\n")
            i += 1


if __name__ == '__main__':
    queryTable('e_deals_tbl', 'Temp/data.txt')
    
