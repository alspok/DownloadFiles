import os
import sys
import pycron
import ftplib
import requests
from datetime import datetime
import pytz

@pycron.cron('*/1 * * * *')
async def downloadFile(timestamp: datetime) -> None:
    sys.stdout = open("/var/pythonapps/_downloadFiles.out", 'a')
    print(f"Cron job running at {datetime.now(pytz.timezone('Europe/Vilnius')): %Y-%m-%d  %H:%M:%S}", end='   ')

    # Download FTP VERKKOKAUPA file pricelist-107377840.csv output file Verkkokouppa.csv
    try:
        HOSTNAME = "18.195.203.145"
        USERNAME = "yht004"
        PASSWORD = "Hmyhv5pLA70Wbn732T4a"
        ftp_server = ftplib.FTP(HOSTNAME, USERNAME, PASSWORD)
        ftp_server.encoding = "utf-8"
        filename = "pricelist-107377840.csv"
        os.chdir("/var/pythonapps/DataFiles")
        with open(filename, "wb") as file:
            ftp_server.retrbinary(f"RETR {filename}", file.write)
        os.rename(filename, "Verkkokouppa.csv")
        ftp_server.close()
    except Exception as e:
        print(e)
        pass

    # Download FTP DOMITECH file KARTOTEKI.XML output file Domitech.xml
    try:
        HOSTNAME = "194.163.128.173"
        USERNAME = "UABAdemi"
        PASSWORD = "uygvuyi*(YDuiouiy78cyc8T&***YD(*7867987yttTFDDS"
        ftp_server = ftplib.FTP(HOSTNAME, USERNAME, PASSWORD)
        ftp_server.encoding = "utf-8"
        filename = "KARTOTEKI.XML"
        os.chdir("/var/pythonapps/DataFiles")
        with open(filename, "wb") as file:
            ftp_server.retrbinary(f"RETR {filename}", file.write)
        os.rename(filename, "Domitech.xml")
        ftp_server.close()
    except Exception as e:
        print(e)
        pass

    # Download FTP EETEUROPARTS file eeteuroparts.csv output file Eeteuroparts.csv
    # try:
    #     HOSTNAME = "ftp.eetgroup.com"
    #     USERNAME = "Ledynas"
    #     PASSWORD = "I1Um77Ignl9Fh172y7DPRjMf"
    #     PORT = 22

    #     ftps = ftplib.FTP_TLS(HOSTNAME)
    #     ftps.login(USERNAME, PASSWORD)
    #     ftps.prot_p()

    #     # ftp_server = ftplib.FTP_TLS(HOSTNAME, USERNAME, PASSWORD, PORT)
    #     # ftp_server.encoding = "utf-8"
    #     filename = "/eeteuroparts.csv"
    #     os.chdir("/var/pythonapps/DataFiles")
    #     with open(filename, "wb") as file:
    #         ftps.retrbinary(f"RETR {filename}", file.write)
    #         # ftp_server.retrbinary(f"RETR {filename}", file.write)
    #     # os.rename(filename, "Eeteuroparts.csv")
    #     del filename
    #     ftp_server.close()
    # except Exception as e:
    #     print(e)
        # pass

    # Donwload FTP APOLO file /MD%20FTP/Apollo%20offer%20CSV.csv
    try:
        HOSTNAME = "apollowroclawnas.myqnapcloud.com"
        USERNAME = "zygimantas@ledynas.eu"
        PASSWORD = "kt9ii427C4PWsyHRNU2G"
        ftp_server = ftplib.FTP(HOSTNAME, USERNAME, PASSWORD)
        ftp_server.encoding = "utf-8"
        ftp_server.cwd('/MD FTP')
        filename = "Apollo offer CSV.csv"
        with open(filename, "wb") as file:
            ftp_server.retrbinary(f"RETR {filename}", file.write)
        os.rename(filename, "Apollo.csv")
        ftp_server.close()
    except Exception as e:
        print(e)
        pass


    # Download URL GITANA file Gitana.xml outputfile Gitana.xml
    try:
        url = "https://www.gitana.lt/modules/exportproducts/out/g7mnFLTUvvPJixYf.xml"
        request = requests.get(url, allow_redirects=True)
        open("Gitana.xml", 'wb').write(request.content)
    except Exception as e:
        print(e)
        pass

    # Download URL NZD file Nzd.xml output file Nzd.xml
    try:
        url = "https://aw-narzedzia.com.pl/xlm/AW-Narzedzia-XML-45635674.xml"
        request = requests.get(url, allow_redirects=True)
        open("Nzd.xml", 'wb').write(request.content)
    except Exception as e:
        print(e)
        pass

    # Download URL ACTION file Action.csv output file Action.csv
    try:
        url = "http://xml.action.pl/Export_CSV.aspx?ActionCustomerId=80827&ActionUserName=ledynas8812&ActionXmlAuthKey=v3OFlXRDoDaIe8TlbONFccfxjqd81g9AH%2baiwxgGDyI%3d&Language=en&Currency=EUR"
        request = requests.get(url, allow_redirects=True)
        open("Action.csv", 'wb').write(request.content)
    except Exception as e:
        print(e)
        pass

    print(f"{os.listdir()}")
    sys.stdout.close()

if __name__ == '__main__':
    pycron.start()
