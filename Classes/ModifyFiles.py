import os
import sys
import csv
import xmltodict
# import pandas as pd
from xml.etree import ElementTree as ET
from bigxml import Parser, xml_handle_element, xml_handle_text

class ModifyFiles():
    cwd = os.getcwd()
    path = f"{cwd}/_downloadFiles.out"
    sys.stdout = open(f"{path}", 'a')

    #---------------------------- CSV Files modification ----------------------------
    # 1
    def verkkokouppaMod(self):
        in_file_name = f"{self.cwd}/DataFiles/Verkkokouppa.csv"
        out_file_name = f"{self.cwd}/ModDataFiles/Verkkokouppa.mod.csv"
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
                'category': item['category'],
                'manufacturer': item['brand'],
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

        fieldnames = ["company","ean", "sku", "category", "manufacturer", "title", "stock", "price", "weight"]

        with open(f"{out_file_name}", mode='w', encoding='utf-8', newline='') as mcsvfh:
            writer = csv.DictWriter(mcsvfh, fieldnames=fieldnames, delimiter=';')
            writer.writeheader()
            writer.writerows(unique_item_dict)

        pass

    # 2
    def apolloMod(self) -> None:
        in_file_name = f"{self.cwd}/DataFiles/Apollo.csv"
        out_file_name = f"{self.cwd}/ModDataFiles/Apollo.mod.csv"
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
            subst_dict['sku'] = item['Part Number']
            subst_dict['category'] = ''
            # item['Vendor'] = item['\ufeffVendor'].replace('\ufeff', '')
            subst_dict['manufacturer'] = item['\ufeffVendor']
            subst_dict['title'] = item['Name']
            subst_dict['stock'] = item['Qty']
            subst_dict['price'] = item['EUR EXW']
            subst_dict['weight'] = '0'

            subst_dict_list.append(subst_dict)

        unique_ean_list = []
        unique_item_dict = []
        for item in subst_dict_list:
            try:
                if int(item['ean']) not in unique_ean_list or int(item['stock']) >= min_stock:
                    unique_item_dict.append(item)
            except:
                pass

        fieldnames = ["company","ean", "sku", "category", "manufacturer", "title", "stock", "price", "weight"]

        with open(f"{out_file_name}", mode='w', encoding='utf-8-sig', newline='') as mcsvfh:
            writer = csv.DictWriter(mcsvfh, fieldnames=fieldnames, delimiter=';')
            writer.writeheader()
            writer.writerows(unique_item_dict)

        pass

    # 3
    def actionMod(self) -> None:
        in_file_name = f"{self.cwd}/DataFiles/Action.csv"
        out_file_name = f"{self.cwd}/ModDataFiles/Action.mod.csv"
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
            subst_dict['category'] = item['\ufeff"Product group"']
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

        fieldnames = ["company","ean", "sku", "category", "manufacturer", "title", "stock", "price", "weight"]
        with open(f"{out_file_name}", mode='w', encoding='utf-8', newline='') as mcsvfh:
            writer = csv.DictWriter(mcsvfh, fieldnames=fieldnames, delimiter=';')
            writer.writeheader()
            writer.writerows(unique_item_dict)

        pass

    def cyberportMod(self) -> None:
        in_file_name = f"{self.cwd}/DataFiles/Cyberport.csv"
        out_file_name = f"{self.cwd}/ModDataFiles/Cyberport.mod.csv"
        company = 'Cyberport'
        min_stock = 1

        dict_list = []
        with open(in_file_name, mode='r', encoding='utf-8', errors='ignore') as csvfh:
            # next(csvfh)
            csv_reader = csv.DictReader(csvfh, delimiter='|')
            for row in csv_reader:
                dict_list.append(row)

        subst_dict_list = []
        for item in dict_list:
            subst_dict = {}
            subst_dict['company'] = company
            subst_dict['ean'] = item['EAN']
            subst_dict['sku'] = item['HBNR']
            subst_dict['category'] = item['Produktgruppe']
            subst_dict['manufacturer'] = item['Hersteller']
            subst_dict['title'] = item['Artikelname']
            subst_dict['stock'] = item['Menge']
            subst_dict['price'] = item['Preis']
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

        fieldnames = ["company","ean", "sku", "category", "manufacturer", "title", "stock", "price", "weight"]
        with open(f"{out_file_name}", mode='w', encoding='utf-8', newline='') as mcsvfh:
            writer = csv.DictWriter(mcsvfh, fieldnames=fieldnames, delimiter=';')
            writer.writeheader()
            writer.writerows(unique_item_dict)

        pass

    def eetMod(self) -> None:
        in_file_name = f"{self.cwd}/DataFiles/EETeuroparts.csv"
        out_file_name = f"{self.cwd}/ModDataFiles/EETeuroparts.mod.csv"
        company = 'EETeuroparts'
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
            subst_dict['sku'] = item['Item Nr']
            subst_dict['category'] = item['Web Category Name']
            subst_dict['manufacturer'] = item['Brand Name']
            subst_dict['title'] = item['Description']
            subst_dict['stock'] = item['Available for sale']
            subst_dict['price'] = item['Price'].replace(',', '.')
            subst_dict['weight'] = item['Gross Weight']
            subst_dict['check_for'] = item['Beskrivelse 2']
            if "Refurbished" in item['Beskrivelse 2']:
                continue
            else:
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

        fieldnames = ["company","ean", "sku", "category", "manufacturer", "title", "stock", "price", "weight"]
        with open(f"{out_file_name}", mode='w', encoding='utf-8', newline='') as mcsvfh:
            writer = csv.DictWriter(mcsvfh, fieldnames=fieldnames, delimiter=';')
            writer.writeheader()
            writer.writerows(unique_item_dict)

        pass

    # 4
    # 5
    def domitechMod(self) -> None:
        # cwd = os.getcwd()
        in_file_name = f"{self.cwd}/DataFiles/Domitech.xml"
        out_file_name = f"{self.cwd}/ModDataFiles/Domitech.mod.csv"
        company = 'Domitech'
        min_stock = 1

        xml_file = ET.parse(in_file_name)
        with open(f"{out_file_name}", mode='w', encoding='utf-8') as csvfh:
            csvfile_writer = csv.writer(csvfh, delimiter=';')

            fieldnames = ["company","ean", "sku", "category", "manufacturer", "title", "stock", "price", "weight"]

            ean_unique = []
            for item in xml_file.findall('KARTOTEKA'):
                if item:
                    ean = item.find('EAN').text
                    if ean == None or ean in ean_unique:
                        continue
                    else:
                        ean_unique.append(ean)
                        sku = item.find('SKU').text
                        category = ''
                        manufacturer = item.find('PRODUCER').text
                        title = ''
                        stock = item.find('STOCK').text
                        if float(stock) <= min_stock:
                            continue
                        price = item.find('PRICE').text
                        weight = '0'
                        csv_line = [company, ean, sku, category, manufacturer, title, stock, price, weight]

                        csvfile_writer.writerow(csv_line)

        pass

    # 6
    def gitanaMod(self) -> None:
        # cwd = os.getcwd()
        in_file_name = f"{self.cwd}/DataFiles/Gitana.xml"
        out_file_name = f"{self.cwd}/ModDataFiles/Gitana.mod.csv"
        company = 'Gitana'
        min_stock = 1

        xml_tree = ET.parse(in_file_name)
        xml_root = xml_tree.getroot()

        with open(f"{out_file_name}", mode='w', encoding='utf-8') as csvfh:
            csvfile_writer = csv.writer(csvfh, delimiter=';')

            fieldnames = ["company","ean", "sku", "category", "manufacturer", "title", "stock", "price", "weight"]

            ean_unique = []
            for item in xml_tree.iter('article'):
                if item:
                    ean = item.find('ean').text
                    if ean == None or ean in ean_unique:
                        continue
                    else:
                        ean_unique.append(ean)
                        sku = item.find('artnum').text
                        category = item.find('category').text
                        manufacturer = item.find('manufacturer').text
                        title = item.find('title').text
                        stock = item.find('stock').text
                        if float(stock) <= min_stock:
                            continue
                        price = item.find('price').text
                        weight = '0'
                        csv_line = [company, ean, sku, category, manufacturer, title, stock, price, weight]

                        csvfile_writer.writerow(csv_line)

        pass

    # 7
    def nzdMod(self) -> None:
        from xml.etree.ElementTree import iterparse
        #from cElementTree import iterparse
        import pandas as pd
        import csv

        # cwd = os.getcwd()
        in_file_name = f"{self.cwd}/DataFiles/Nzd.xml"
        out_file_name = f"{self.cwd}/ModDataFiles/Nzd.mod.csv"
        company = 'NZD'
        min_stock = 1

        dict_list = []
        dict_tag = {}

        for _, elem in iterparse(in_file_name, events=("end",)):
            if elem.tag == 'kod_kreskowy':
                dict_tag['ean'] = elem.text
            if elem.tag == 'indeks_handlowy':
                dict_tag['sku'] = elem.text
            if elem.tag == 'kategoria_wielopoziomowa':
                dict_tag['category'] = elem.text
            if elem.tag == 'producent':
                dict_tag['manufacturer'] = elem.text
            if elem.tag == 'nazwa':
                dict_tag['title'] = elem.text
            if elem.tag == 'stan_liczbowy':
                dict_tag['stock'] = elem.text
            if elem.tag == 'cena_waluta':
                dict_tag['price'] = elem.text
            if elem.tag == 'waga':
                dict_tag['weight'] = elem.text
            if elem.tag == 'produkt':
                dict_tag['company'] = company
                dict_list.append(dict_tag)
                dict_tag = {}
            elem.clear()

        fdict_list = []
        for item in dict_list:
            if ('ean' not in item) or (int(item['stock']) < min_stock):
                continue
            else:
                fdict_list.append(item)

        # fdict_list = [item for item in dict_list if ((item['ean'] is not None) or (int(item['stock']) < min_stock))]

        with open(out_file_name, mode='w', encoding='utf-8') as csvfh:
            csv_header = ['company', 'ean', 'sku', 'category', 'manufacturer', 'title', 'stock', 'price', 'weight']
            writer = csv.DictWriter(csvfh, fieldnames=csv_header, delimiter=';')
            writer.writeheader()
            writer.writerows(fdict_list)

        pass

        
    
if __name__ == '__main__':
        # ModifyFiles().b2bsportsMod()
    # ModifyFiles().verkkokouppaMod()
    # ModifyFiles().apolloMod()
    # ModifyFiles().actionMod()
    # ModifyFiles().domitechMod()
    # ModifyFiles().gitanaMod()
    # ModifyFiles().nzdMod()
    ModifyFiles().eeteuropartsMod()
        # ModifyFiles().jacobMod()
        # ModifyFiles().daskJacobMod()