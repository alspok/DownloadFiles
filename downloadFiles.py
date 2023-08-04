import os
import sys
import time
import pycron
import ftplib
import requests
from datetime import datetime
import pytz
from Classes.ModifyFiles import ModifyFiles
from Classes.MenageSQL import MenageSQL
from menageSQL import menageSQL
from urllib.request import urlretrieve

@pycron.cron('*/40 * * * *')
async def downloadFiles(timestamp: datetime) -> None:
# def downloadFiles() -> None:
    cwd = os.getcwd()
    print_out = f"{cwd}/_downloadFiles.out"
    sys.stdout = open(print_out, 'a')
    print(f"Cron job running at {datetime.now(pytz.timezone('Europe/Vilnius')): %Y-%m-%d  %H:%M:%S}", end='   ')
    sys.stdout.flush()

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

    print(downloadedFiles)
    sys.stdout.flush()

    # start = time.time()
    ModifyFiles().verkkokouppaMod() # 1
    # elapsed_time = time.time() - start
    # print(f"Verkkokouppa modified in {elapsed_time} sec")
    # sys.stdout.flush()
    
    # start = time.time()
    ModifyFiles().apolloMod() # 2
    # elapsed_time = time.time() - start
    # print(f"Apollo modified in {elapsed_time} sec")
    # sys.stdout.flush()

    # start = time.time()
    ModifyFiles().actionMod() # 3
    # elapsed_time = time.time() - start
    # print(f"Action modified in {elapsed_time} sec")

    # start = time.time()
    ModifyFiles().domitechMod() # 4
    # elapsed_time = time.time() - start
    # print(f"Domitech modified in {elapsed_time} sec")
    # sys.stdout.flush()

    # start = time.time()
    ModifyFiles().gitanaMod() # 5
    # elapsed_time = time.time() - start
    # print(f"Gitana modified in {elapsed_time} sec")
    # sys.stdout.flush()

    # start = time.time()
    ModifyFiles().nzdMod() # 6
    # elapsed_time = time.time() - start
    # print(f"Nzd modified in {elapsed_time} sec")
    # sys.stdout.flush()

    # start = time.time()
    ModifyFiles().jacobMod() # 7
    # elapsed_time = time.time() - start
    # print(f"Jacob modified in {elapsed_time} sec")
    # sys.stdout.flush()

    # ModifyFiles().b2bsportsMod() # 8
    # ModifyFiles().eeteuropartsMod()

    pass

    start =time.time()
    menageSQL()
    elapsed_time = time.time() - start
    print(f"DB made in {elapsed_time} sec")
    sys.stdout.flush()

if __name__ == '__main__':
    pycron.start()
    # downloadFiles()