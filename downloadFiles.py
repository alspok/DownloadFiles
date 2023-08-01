import os
import sys
import pycron
import ftplib
import requests
from datetime import datetime
import pytz
from Classes.ModifyFiles import ModifyFiles
from Classes.MenageSQL import MenageSQL
import menageSQL
from urllib.request import urlretrieve

@pycron.cron('*/10 * * * *')
async def downloadFiles(timestamp: datetime) -> None:
# def downloadFiles() -> None:
    cwd = os.getcwd()
    sys.stdout = open(f"{cwd}/_downloadFiles.out", 'a')
    print(f"Cron job running at {datetime.now(pytz.timezone('Europe/Vilnius')): %Y-%m-%d  %H:%M:%S}", end='   ')

    downloadedFiles = []
# def downloadFiles() -> None:
#     sys.stdout = open("/var/pythonapps/_downloadFiles.out", 'a')
    # Download FTP VERKKOKAUPA file pricelist-107377840.csv output file Verkkokouppa.csv
    try:
        HOSTNAME = "18.195.203.145"
        USERNAME = "yht004"
        PASSWORD = "Hmyhv5pLA70Wbn732T4a"
        ftp_server = ftplib.FTP(HOSTNAME, USERNAME, PASSWORD, timeout=3600)
        ftp_server.encoding = "utf-8"
        filename = "pricelist-107377840.csv"
        os.chdir(f"{cwd}/DataFiles")
        with open(filename, "wb") as file:
            ftp_server.retrbinary(f"RETR {filename}", file.write)
        ren_filename = "Verkkokouppa.csv"
        os.rename(filename, ren_filename)
        downloadedFiles.append(ren_filename)
        ftp_server.close()
    except Exception as e:
        print(e)
        pass

    # Download FTP DOMITECH file KARTOTEKI.XML output file Kartoteki.xml
    try:
        HOSTNAME = "194.163.128.173"
        USERNAME = "UABAdemi"
        PASSWORD = "uygvuyi*(YDuiouiy78cyc8T&***YD(*7867987yttTFDDS"

        ftp_server = ftplib.FTP(HOSTNAME, USERNAME, PASSWORD, timeout=3600)
        ftp_server.encoding = "utf-8"
        filename = "KARTOTEKI.XML"
        os.chdir(f"{cwd}/DataFiles")
        with open(filename, "wb") as file:
            ftp_server.retrbinary(f"RETR {filename}", file.write)
        ren_filename = "Domitech.xml"
        os.rename(filename, ren_filename)
        downloadedFiles.append(ren_filename)
        ftp_server.close()
    except Exception as e:
        print(e)
        pass

    #Download FTP EETEUROPARTS file eeteuroparts.csv output file Eeteuroparts.csv
    # try:
    #     HOSTNAME = "ftp.eetgroup.com"
    #     USERNAME = "Ledynas"
    #     PASSWORD = "I1Um77Ignl9Fh172y7DPRjMf"
    #     PORT = 22

    #     ftp_server = ftplib.FTP(HOSTNAME, USERNAME, PASSWORD, PORT, timeout=3600)
    #     ftp_server.encoding = "utf-8"
    #     filename = "eeteuroparts.csv"
    #     os.chdir(f"{cwd}/DataFiles")
    #     with open(filename, "wb") as file:
    #         ftp_server.retrbinary(f"RETR {filename}", file.write)
    #     ren_filename = "Eeteuroparts.csv"
    #     os.rename(filename, ren_filename)
    #     downloadedFiles.append(ren_filename)
    #     ftp_server.close()
    # except Exception as e:
    #     print(e)
    #     pass

    # Donwload FTP APOLO file /MD%20FTP/Apollo%20offer%20CSV.csv
    try:
        HOSTNAME = "apollowroclawnas.myqnapcloud.com"
        USERNAME = "zygimantas@ledynas.eu"
        PASSWORD = "kt9ii427C4PWsyHRNU2G"
        ftp_server = ftplib.FTP(HOSTNAME, USERNAME, PASSWORD, timeout=3600)
        ftp_server.encoding = "utf-8"
        ftp_server.cwd('/MD FTP')
        filename = "Apollo_pricelist.csv"
        os.chdir(f"{cwd}/DataFiles")
        with open(filename, "wb") as file:
            ftp_server.retrbinary(f"RETR {filename}", file.write)
        ren_filename = "Apollo.csv"
        os.rename(filename, ren_filename)
        downloadedFiles.append(ren_filename)
        ftp_server.close()
    except Exception as e:
        print(e)
        pass

    # Download URL GITANA file Gitana.xml outputfile Gitana.xml
    try:
        url = "https://www.gitana.lt/modules/exportproducts/out/g7mnFLTUvvPJixYf.xml"
        filename = "Gitana.xml"
        os.chdir(f"{cwd}/DataFiles")
        urlretrieve(url, filename)
        downloadedFiles.append(filename)
    except Exception as e:
        print(e)
        pass

    # Download URL NZD file Nzd.xml output file Nzd.xml
    try:
        url = "https://aw-narzedzia.com.pl/xlm/AW-Narzedzia-XML-45635674.xml"
        filename = "Nzd.xml"
        os.chdir(f"{cwd}/DataFiles")
        urlretrieve(url, filename)
        downloadedFiles.append(filename)
    except Exception as e:
        print(e)
        pass

    # Download URL NZD file Nzd.xml output file Nzd.xml
    # try:
    #     url = "https://aw-narzedzia.com.pl/xlm/AW-Narzedzia-XML-45635674.xml"
    #     request = requests.get(url, allow_redirects=True, timeout=3600)
    #     filename = "Nzd.xml"
    #     os.chdir(f"{cwd}/DataFiles")
    #     open(filename, 'wb').write(request.content)
    #     downloadedFiles.append(filename)
    # except Exception as e:
    #     print(e)
    #     pass

    # Download URL ACTION file Action.csv output file Action.csv
    try:
        url = "http://xml.action.pl/Export_CSV.aspx?ActionCustomerId=80827&ActionUserName=ledynas8812&ActionXmlAuthKey=v3OFlXRDoDaIe8TlbONFccfxjqd81g9AH%2baiwxgGDyI%3d&Language=en&Currency=EUR"
        filename = "Action.csv"
        os.chdir(f"{cwd}/DataFiles")
        urlretrieve(url, filename)
        downloadedFiles.append(filename)
    except Exception as e:
        print(e)
        pass

    # Download URL JACOB file haendler_netto.csv output file Jacob.csv
    try:
        url = "https://www.jacob.de/content/csvTool/haendler_netto.csv"
        filename = "Jacob.csv"
        os.chdir(f"{cwd}/DataFiles")
        urlretrieve(url, filename)
        downloadedFiles.append(filename)
    except Exception as e:
        print(e) 
        pass
    
    # try:
    #     url = "https://www.jacob.de/content/csvTool/haendler_netto.csv"
    #     request = requests.get(url, allow_redirects=True, timeout=3600)
    #     filename = "Jacob.csv"
    #     os.chdir(f"{cwd}/DataFiles")
    #     open(filename, 'wb').write(request.content)
    #     downloadedFiles.append(filename)
    # except Exception as e:
    #     print(e)
    #     pass

    # Download URL B2B_SPORTS_WHOLESALE partner_b2b_full.xml output file B2B_full.xml
    # try:
    #     url = "https://b2bsportswholesale.net/v2/xml/download/format/partner_b2b_full/key/78d2afad8f1fa4c0098dc6b9721f63df/lang/en"
    #     filename = "B2B_sports.xml"
    #     os.chdir(f"{cwd}/DataFiles")
    #     urlretrieve(url, filename)
    #     downloadedFiles.append(filename)
    # except Exception as e:
    #     print(e) 
    #     pass
    
        
        
    #     request = requests.get(url, allow_redirects=True, timeout=3600)
    #     filename = "B2B_full.xml"
    #     os.chdir(f"{cwd}/DataFiles")
    #     open(filename, 'wb').write(request.content)
    #     downloadedFiles.append(filename)
    # except Exception as e:
    #     print(e)
    #     pass

    print(downloadedFiles)
    sys.stdout.close()

    # 
    ModifyFiles().verkkokouppaMod() # 1
    ModifyFiles().apolloMod() # 2
    ModifyFiles().actionMod() # 3
    ModifyFiles().domitechMod() # 4
    ModifyFiles().gitanaMod() # 5
    ModifyFiles().nzdMod() # 6
    ModifyFiles().jacobMod() # 7
    # ModifyFiles().b2bsportsMod() # 8
    # ModifyFiles().eeteuropartsMod()

    menageSQL()


if __name__ == '__main__':
    pycron.start()
    # downloadFiles()