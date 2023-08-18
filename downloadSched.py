import downloadFiles
import schedule
import time
from datetime import datetime

def downloadSched() -> None:
    downloadFiles.downloadFiles()
    # dt = datetime.now()
    # fdt = dt.strftime("%Y-%m-%d %H:%M:%S")
    # print(f"downloadSched.py runs at: {fdt}")

schedule.every().day.at("04:00").do(downloadSched)

while True:
    schedule.run_pending()
    time.sleep(1)
