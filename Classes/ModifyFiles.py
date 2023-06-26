import csv

class ModifyFiles():
   
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
            csv_reader = csv.DictReader(csvfh, delimiter=';')
            next(csv_reader)
            for row in csv_reader:
                dict_list.append(row)

        pass


    def gitanaMod() -> None:

        pass

    def domitechcMod() -> None:

        pass

    def nzdMod() -> None:

        pass

    def actioNod() -> None:

        pass


if __name__ == '__main__':
    # ModifyFiles().verkkokouppaMod()
    ModifyFiles().apolloMod()