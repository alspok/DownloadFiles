import csv
import xmltodict
import pprint
from xml.etree import ElementTree as ET

class ModifyFiles():
   
#---------------------------- CSV Files modification ----------------------------
    # 1
    def verkkokouppaMod(self):
        cwd = os.getcwd()
        in_file_name = f"{cwd}/DataFiles/Verkkokouppa.csv"
        out_file_name = f"{cwd}/ModDataFiles/Verkkokouppa.mod.csv"
        company = 'Verkkokouppa'
        min_stock = 1

        dict_list = []
        with open(in_file_name, mode='r', encoding='utf-8', errors='ignore') as csvfh:
            # next(csvfh)
            csv_reader = csv.DictReader(csvfh, delimiter=';')
            for row in csv_reader:
                dict_list.append(row)

        subst_dict_list = []
        for item in dict_list:
            ean_list = item['eans'].split(':')
            tail_dict = {
                'sku': item['manufsku'],
                'manufcturer': item['brand'],
                'title': item['description'],
                'stock': item['availability_jatkasaari'],
                'price': item['price_wotax'],
                'weight': item['weight']
                }
            for ean in ean_list:
                ean_dict = {}
                ean_dict.update({'company': company})
                ean_dict.update({'ean': ean})
                ean_dict.update(tail_dict)
                subst_dict_list.append(ean_dict)

        unique_ean_list = []
        unique_item_dict = []
        for item in subst_dict_list:
            if int(item['ean']) not in unique_ean_list and int(item['stock']) >= min_stock :
                unique_item_dict.append(item)

        fieldnames = unique_item_dict[0].keys()

        with open(f"{out_file_name}", mode='w', encoding='utf-8', newline='') as mcsvfh:
            writer = csv.DictWriter(mcsvfh, fieldnames=fieldnames, delimiter=';')
            writer.writeheader()
            writer.writerows(unique_item_dict)

        pass

    # 2
    def apolloMod(self) -> None:
        cwd = os.getcwd()
        in_file_name = f"{cwd}/DataFiles/Apollo.csv"
        out_file_name = f"{cwd}/ModDataFiles/Apollo.mod.csv"
        company = 'Apollo'
        min_stock = 1

        dict_list = []
        with open(in_file_name, mode='r', encoding='utf-8', errors='ignore') as csvfh:
            # next(csvfh)
            csv_reader = csv.DictReader(csvfh, delimiter=';')
            for row in csv_reader:
                dict_list.append(row)

        subst_dict_list = []
        for item in dict_list:
            subst_dict = {}
            subst_dict['company'] = company
            subst_dict['ean'] = item['EAN']
            subst_dict['sku'] = item['\ufeffPart number']
            subst_dict['manufacturer'] = item['Producer']
            subst_dict['title'] = item['Name']
            subst_dict['stock'] = item['Quantity']
            subst_dict['price'] = item['Price EURO EXW']
            subst_dict['weight'] = ''

            subst_dict_list.append(subst_dict)

        unique_ean_list = []
        unique_item_dict = []
        for item in subst_dict_list:
            try:
                if int(item['ean']) not in unique_ean_list or int(item['stock']) >= min_stock:
                    unique_item_dict.append(item)
            except:
                pass

        fieldnames = unique_item_dict[0].keys()

        with open(f"{out_file_name}", mode='w', encoding='utf-8', newline='') as mcsvfh:
            writer = csv.DictWriter(mcsvfh, fieldnames=fieldnames, delimiter=';')
            writer.writeheader()
            writer.writerows(unique_item_dict)

        pass

    # 3
    def actionMod(self) -> None:
        cwd = os.getcwd()
        in_file_name = f"{cwd}/DataFiles/Action.csv"
        out_file_name = f"{cwd}/ModDataFiles/Action.mod.csv"
        company = 'Action'
        min_stock = 1

        dict_list = []
        with open(in_file_name, mode='r', encoding='utf-8', errors='ignore') as csvfh:
            # next(csvfh)
            csv_reader = csv.DictReader(csvfh, delimiter=',')
            for row in csv_reader:
                dict_list.append(row)

        subst_dict_list = []
        for item in dict_list:
            subst_dict = {}
            subst_dict['company'] = company
            subst_dict['ean'] = item['EAN']
            subst_dict['sku'] = item['Manufacturer\'s code']
            subst_dict['manufacturer'] = item['Producer']
            subst_dict['title'] = item['Name of product']
            subst_dict['stock'] = item['Stock']
            subst_dict['price'] = item['Net price EUR']
            subst_dict['weight'] = '0'

            subst_dict_list.append(subst_dict)

        unique_ean_list = []
        unique_item_dict = []
        for item in subst_dict_list:
            try:
                if (item['ean'] != '') and (int(item['ean']) not in unique_ean_list) and (int(item['stock']) >= min_stock):
                    unique_item_dict.append(item)
            except Exception as e:
                print(e)
                pass

        fieldnames = unique_item_dict[0].keys()

        with open(f"{out_file_name}", mode='w', encoding='utf-8', newline='') as mcsvfh:
            writer = csv.DictWriter(mcsvfh, fieldnames=fieldnames, delimiter=';')
            writer.writeheader()
            writer.writerows(unique_item_dict)

        pass

    # 4
    def eeteuropartsMod(self) -> None:
        cwd = os.getcwd()
        in_file_name = f"{cwd}/DataFiles/Eeteuroparts.csv"
        out_file_name = f"{cwd}/ModDataFiles/Eeteuroparts.mod.csv"
        company = 'Eeteuroparts'
        min_stock = 1.0

        dict_list = []
        with open(in_file_name, mode='r', encoding='utf-8', errors='ignore') as csvfh:
            # next(csvfh)
            csv_reader = csv.DictReader(csvfh, delimiter=';')
            for row in csv_reader:
                dict_list.append(row)

        subst_dict_list = []
        for item in dict_list:
            subst_dict = {}
            subst_dict['company'] = company
            subst_dict['ean'] = item['EAN/UPC']
            if subst_dict['ean'] == '':
                continue
            subst_dict['sku'] = item['Item Nr']
            subst_dict['manufacturer'] = item['Brand Name']
            subst_dict['title'] = item['Description']
            subst_dict['stock'] = item['Available for sale'].replace(',', '.')
            if float(subst_dict['stoce']) < min_stock:
                continue
            subst_dict['price'] = item['Price'].replace(',', '.')
            subst_dict['weight'] = item['Gross Weight'].replace(',', '.')

            subst_dict_list.append(subst_dict)

        unique_ean_list = []
        unique_item_dict = []
        for item in subst_dict_list:
            try:
                if int(item['ean']) not in unique_ean_list:
                    unique_item_dict.append(item)
            except Exception as e:
                print(e)
                pass

        fieldnames = unique_item_dict[0].keys()

        with open(f"{out_file_name}", mode='w', encoding='utf-8', newline='') as mcsvfh:
            writer = csv.DictWriter(mcsvfh, fieldnames=fieldnames, delimiter=';')
            writer.writeheader()
            writer.writerows(unique_item_dict)

            dict_list = []
            with open(in_file_name, mode='r', encoding='utf-8', errors='ignore') as csvfh:
                csv_reader = csv.DictReader(csvfh, delimiter=';')
                for row in csv_reader:
                    dict_list.append(row)

        pass

    def jacobMod(self) -> None:
        cwd = os.getcwd()
        in_file_name = f"{cwd}/DataFiles/Jacob.csv"
        out_file_name = f"{cwd}/ModDataFiles/Jacob.mod.csv"
        company = "Jacob"
        min_stock = 1

        dict_list = []
        with open(in_file_name, mode='r', encoding='utf-8', errors='ignore') as csvfh:
            # next(csvfh)
            csv_reader = csv.DictReader(csvfh, delimiter=';')
            for row in csv_reader:
                dict_list.append(row)

        subst_dict_list = []
        for item in dict_list:
            subst_dict = {}
            subst_dict['company'] = company
            subst_dict['ean'] = item['EAN/UPC']
            if subst_dict['ean'] == '':
                continue
            subst_dict['sku'] = item['\ufeffSku']
            subst_dict['manufacturer'] = item['Hersteller']
            subst_dict['title'] = item['Kurzbezeichnung']
            subst_dict['stock'] = item['Bestand']
            if float(subst_dict['stock']) < min_stock:
                continue
            subst_dict['price'] = item['Preis netto']
            subst_dict['weight'] = '0'

            subst_dict_list.append(subst_dict)

        unique_ean_list = []
        unique_item_dict = []
        for item in subst_dict_list:
            try:
                if int(item['ean']) not in unique_ean_list:
                    unique_item_dict.append(item)
            except Exception as e:
                print(e)
                pass

        fieldnames = unique_item_dict[0].keys()

        with open(f"{out_file_name}", mode='w', encoding='utf-8', newline='') as mcsvfh:
            writer = csv.DictWriter(mcsvfh, fieldnames=fieldnames, delimiter=';')
            writer.writeheader()
            writer.writerows(unique_item_dict)

            dict_list = []
            with open(in_file_name, mode='r', encoding='utf-8', errors='ignore') as csvfh:
                csv_reader = csv.DictReader(csvfh, delimiter=';')
                for row in csv_reader:
                    dict_list.append(row)

        pass

#---------------------------- XML Files modification ----------------------------

    # 5
    def domitechMod(self) -> None:
        cwd = os.getcwd()
        in_file_name = f"{cwd}/DataFiles/Domitech.xml"
        out_file_name = f"{cwd}/ModDataFiles/Domitech.mod.csv"
        company = 'Domitech'
        min_stock = 1

        xml_file = ET.parse(in_file_name)
        with open(f"{out_file_name}", mode='w', encoding='utf-8') as csvfh:
            csvfile_writer = csv.writer(csvfh, delimiter=';')

            csvfile_writer.writerow(['company', 'ean', 'sku', 'manufacturer', 'title', 'stock', 'price', 'weight'])

            ean_unique = []
            for item in xml_file.findall('KARTOTEKA'):
                if item:
                    ean = item.find('EAN').text
                    if ean == None or ean in ean_unique:
                        continue
                    else:
                        ean_unique.append(ean)
                        sku = item.find('SKU').text
                        manufacturer = item.find('PRODUCER').text
                        title = ''
                        stock = item.find('STOCK').text
                        if float(stock) <= min_stock:
                            continue
                        price = item.find('PRICE').text
                        weight = ''
                        csv_line = [company, ean, sku, manufacturer, title, stock, price, weight]

                        csvfile_writer.writerow(csv_line)

        pass

    # 6
    def gitanaMod(self) -> None:
        cwd = os.getcwd()
        in_file_name = f"{cwd}/DataFiles/Gitana.xml"
        out_file_name = f"{cwd}/ModDataFiles/Gitana.mod.csv"
        company = 'Gitana'
        min_stock = 1

        xml_tree = ET.parse(in_file_name)
        xml_root = xml_tree.getroot()

        with open(f"{out_file_name}", mode='w', encoding='utf-8') as csvfh:
            csvfile_writer = csv.writer(csvfh, delimiter=';')

            csvfile_writer.writerow(['company', 'ean', 'sku', 'manufacturer', 'title', 'stock', 'price', 'weight'])

            ean_unique = []
            for item in xml_tree.iter('article'):
                if item:
                    ean = item.find('ean').text
                    if ean == None or ean in ean_unique:
                        continue
                    else:
                        ean_unique.append(ean)
                        sku = item.find('artnum').text
                        manufacturer = item.find('manufacturer').text
                        title = item.find('title').text
                        stock = item.find('stock').text
                        if float(stock) <= min_stock:
                            continue
                        price = item.find('price').text
                        weight = ''
                        csv_line = [company, ean, sku, manufacturer, title, stock, price, weight]

                        csvfile_writer.writerow(csv_line)

        pass

    # 7
    def nzdMod(self) -> None:
        cwd = os.getcwd()
        in_file_name = f"{cwd}/DataFiles/Nzd.xml"
        out_file_name = f"{cwd}/ModDataFiles/Nzd.mod.csv"
        company = 'NZD'
        min_stock = 1
        
        try:
            xml_tree = ET.parse(in_file_name)
            xml_root = xml_tree.getroot()
        except Exception as e:
            print(e)

        with open(f"{out_file_name}", mode='w', encoding='utf-8') as csvfh:
            csvfile_writer = csv.writer(csvfh, delimiter=';')

            csvfile_writer.writerow(['company', 'ean', 'sku', 'manufacturer', 'title', 'stock', 'price', 'weight'])

            ean_unique = []
            for item in xml_root.findall('produkt'):
                if item[5].text in ean_unique or item[5].text == None or float(item[9].text.replace(',', '.')) <= min_stock:
                        continue
                else:
                    ean_unique.append(item[5].text)
                    ean = item[5].text
                    sku = item[2].text
                    manufacturer = item[8].text
                    title = item[6].text
                    stock = item[9].text
                    price = item[0].text
                    weight = item[10].text
                    csv_line = [company, ean, sku, manufacturer, title, stock, price, weight]

                    csvfile_writer.writerow(csv_line)

        pass
   
    # 8
    def b2bsportsMod(self) -> None:
        cwd = os.getcwd()
        in_file_name = f"{cwd}/DataFiles/B2B_full.xml"
        out_file_name = f"{cwd}/ModDataFiles/B2B_full.mod.csv"
        company = "B2B_sports"
        min_stock = 1

        try:
            xml_tree = ET.parse(in_file_name)
            xml_root = xml_tree.getroot()
        except Exception as e:
            print(e)

        with open(f"{out_file_name}", mode='w', encoding='utf-8') as csvfh:
            csvfile_writer = csv.writer(csvfh, delimiter=';')

            csvfile_writer.writerow(['company', 'ean', 'sku', 'manufacturer', 'title', 'stock', 'price', 'weight'])

            ean_unique = []

            for stock in xml_root.iter('stock'):
                for item in stock.iter('item'):
                    if((item.attrib['ean'] in ean_unique) or (float(item.attrib['quantity']) <= min_stock)):
                        continue
                    else:
                        ean_unique.append(item.attrib['ean'])
                        print(item.attrib['ean'], item.attrib['quantity'])
                
                pass

                    # if ean == None or ean in ean_unique:
                    #     continue
                    # else:
                    #     ean_unique.append(ean)

        pass

# if __name__ == '__main__':
    # ModifyFiles().b2bsportsMod()
    # ModifyFiles().verkkokouppaMod()
    # ModifyFiles().apolloMod()
    # ModifyFiles().actionMod()
    # ModifyFiles().domitechMod()
    # ModifyFiles().gitanaMod()
    # ModifyFiles().nzdMod()
    # ModifyFiles().eeteuropartsMod()
    # ModifyFiles().jacobMod()