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
        min_stock = 1

        with open(f"{in_file_name}", mode='r', encoding='utf-8', errors='ignore') as xfh:
            xml_file = xfh.read()

        xml_dict = xmltodict.parse(xml_file)
        pprint.pprint(xml_dict, indent=2)

        pass

    def gitanaMod() -> None:

        pass

    

    def nzdMod() -> None:

        pass

   


if __name__ == '__main__':
    # ModifyFiles().verkkokouppaMod()
    # ModifyFiles().apolloMod()
    # ModifyFiles().actionMod()
    ModifyFiles().domitechMod()