import ftplib
import os
import ssl

def test():
    try:
        HOSTNAME = "ftp.eetgroup.com"
        USERNAME = "Ledynas"
        PASSWORD = "I1Um77Ignl9Fh172y7DPRjMf"
        
        ftp = ftplib.FTP_TLS()
        ftp.debugging = 2
        ftp.prot_p
        ftp.ssl_version = ssl.PROTOCOL_SSLv23
        ftp.connect(HOSTNAME)
        ftp.login(USERNAME, PASSWORD)

        os.chdir("/var/pythonapps/DataFiles")
        with open(filename, "wb") as file:
            ftp.retrbinary(f"RETR {filename}", file.write)
            # ftp_server.retrbinary(f"RETR {filename}", file.write)
        # os.rename(filename, "Eeteuroparts.csv")
        del filename
        ftp.close()
    except Exception as e:
        print(e)

if __name__ == '__main__':
     test()