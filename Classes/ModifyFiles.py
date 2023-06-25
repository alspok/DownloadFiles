import csv

class ModifyFiles():
    def verkkokouppaMod(self) -> None:
        in_file_name = "/var/pythonapps/DataFiles/Verkkokouppa.csv"
        out_file_name = "/var/pythonapps/ModDataFiles/Verkkokouppa.mod.csv"
        with open(f"{in_file_name}", mode='r', encoding='utf-8', errors='ignore') as rfh, \
             open(f"{out_file_name}", mode='w', encoding='utf-8', newline='') as wfh:
            for line in rfh:
                if line.strip():
                    mod_line = line.replace(',', '.').replace(';', ',')
                    wfh.write(mod_line)

        with open(f"{out_file_name}", mode='r', encoding='utf=8', errors='ignore') as rfh:
            csv_dict = csv.DictReader(rfh)
            dict_list = []
            for item in csv_dict:
                dict_list.append(item)
        
        eans_list = []
        for item in dict_list:
            for key, value in item.items():
                if key == 'eans':
                    eans_list.append(value)

        ean_list = []
        for item in eans_list:
            ean_list.extend(item.split(':'))

        pass

    def verkkokouppaModCSV(self):
        in_file_name = "/var/pythonapps/DataFiles/Verkkokouppa.csv"
        min_stock = 5
        out_file_name = "/var/pythonapps/ModDataFiles/Verkkokouppa.mod.csv"

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
                if int(tail_dict['stock']) > min_stock:
                    subst_dict_list.append(ean_dict)

        pass


    def gitanaMod() -> None:

        pass

    def domitechcMod() -> None:

        pass

    def nzdMod() -> None:

        pass

    def actioNod() -> None:

        pass

    def apolloMod() -> None:

        pass

if __name__ == '__main__':
    ModifyFiles().verkkokouppaModCSV()