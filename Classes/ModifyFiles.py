import csv
import xmltodict
import pprint
from xml.etree import ElementTree as ET

class ModifyFiles():
   
#---------------------------- CSV Files modification ----------------------------

    def verkkokouppaMod(self):
        in_file_name = "/var/pythonapps/DataFiles/Verkkokouppa.csv"
        out_file_name = "/var/pythonapps/ModDataFiles/Verkkokouppa.mod.csv"
        min_stock = 1

        dict_list = []
        with open(in_file_name, mode='r', encoding='utf-8', errors='ignore') as csvfh:
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
                'price': item['price_wotax'],
                'stock': item['availability_jatkasaari'],
                'weight': item['weight']
                }
            for ean in ean_list:
                ean_dict = {'ean': ean}
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

    def apolloMod(self) -> None:
        in_file_name = "/var/pythonapps/DataFiles/Apollo.csv"
        out_file_name = "/var/pythonapps/ModDataFiles/Apollo.mod.csv"
        min_stock = 1

        dict_list = []
        with open(in_file_name, mode='r', encoding='utf-8', errors='ignore') as csvfh:
            next(csvfh)
            csv_reader = csv.DictReader(csvfh, delimiter=';')
            for row in csv_reader:
                dict_list.append(row)

        subst_dict_list = []
        for item in dict_list:
            subst_dict = {}
            subst_dict['ean'] = item['EAN']
            subst_dict['sku'] = item['Part Number']
            subst_dict['manufacturer'] = item['Vendor']
            subst_dict['title'] = item['Name']
            subst_dict['stock'] = item['Qty']
            subst_dict['price'] = item['EUR EXW']
            subst_dict['weight'] = ''

            subst_dict_list.append(subst_dict)

        unique_ean_list = []
        unique_item_dict = []
        for item in subst_dict_list:
            try:
                if int(item['ean']) not in unique_ean_list and int(item['stock']) >= min_stock:
                    unique_item_dict.append(item)
            except:
                pass

        fieldnames = unique_item_dict[0].keys()

        with open(f"{out_file_name}", mode='w', encoding='utf-8', newline='') as mcsvfh:
            writer = csv.DictWriter(mcsvfh, fieldnames=fieldnames, delimiter=';')
            writer.writeheader()
            writer.writerows(unique_item_dict)

        pass

    def actionMod(self) -> None:
        in_file_name = "/var/pythonapps/DataFiles/Action.csv"
        out_file_name = "/var/pythonapps/ModDataFiles/Action.mod.csv"
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
                if int(item['ean']) not in unique_ean_list and int(item['stock']) >= min_stock:
                    unique_item_dict.append(item)
            except:
                pass

        fieldnames = unique_item_dict[0].keys()

        with open(f"{out_file_name}", mode='w', encoding='utf-8', newline='') as mcsvfh:
            writer = csv.DictWriter(mcsvfh, fieldnames=fieldnames, delimiter=';')
            writer.writeheader()
            writer.writerows(unique_item_dict)

        pass

#---------------------------- XML Files modification ----------------------------

    def domitechMod(self) -> None:
        in_file_name = "/var/pythonapps/DataFiles/Domitech.xml"
        out_file_name = "/var/pythonapps/ModDataFiles/Domitech.mod.csv"
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

    def gitanaMod(self) -> None:
        in_file_name = "/var/pythonapps/DataFiles/Gitana.xml"
        out_file_name = "/var/pythonapps/ModDataFiles/Gitana.mod.csv"
        company = 'Gitana'
        min_stock = 1

        xml_file = ET.parse(in_file_name)
        with open(f"{out_file_name}", mode='w', encoding='utf-8') as csvfh:
            csvfile_writer = csv.writer(csvfh, delimiter=';')

            csvfile_writer.writerow(['company', 'ean', 'sku', 'manufacturer', 'title', 'stock', 'price', 'weight'])

            ean_unique = []
            for item in xml_file.findall('article'):
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

    def nzdMod() -> None:
        in_file_name = "/var/pythonapps/DataFiles/Nzd.xml"
        out_file_name = "/var/pythonapps/ModDataFiles/Nzd.mod.csv"
        company = 'NZD'
        min_stock = 1
        
        xml_file = ET.parse(in_file_name)
        with open(f"{out_file_name}", mode='w', encoding='utf-8') as csvfh:
            csvfile_writer = csv.writer(csvfh, delimiter=';')

        csvfile_writer.writerow(['company', 'ean', 'sku', 'manufacturer', 'title', 'stock', 'price', 'weight'])

        for item in xml_file.findall(''):
                if item:
                    ean = item.find('EAN').text
                    sku = item.find('SKU').text
                    manufacturer = item.find('PRODUCER').text
                    title = ''
                    stock = item.find('STOCK').text
                    if float(stock) <= min_stock:
                        continue
                    price = item.find('PRICE').text
                    weight = ''
                    csv_line = [ean, sku, manufacturer, title, stock, price, weight]

                    csvfile_writer.writerow(csv_line)

        pass

   


if __name__ == '__main__':
    # ModifyFiles().verkkokouppaMod()
    # ModifyFiles().apolloMod()
    # ModifyFiles().actionMod()
    ModifyFiles().domitechMod()
    # ModifyFiles().gitanaMod()