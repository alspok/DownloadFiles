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
    ModifyFiles().verkkokouppaMod()