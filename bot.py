import os
import sys
import time
import requests
from colorama import *
from datetime import datetime

red = Fore.LIGHTRED_EX
yellow = Fore.LIGHTYELLOW_EX
green = Fore.LIGHTGREEN_EX
black = Fore.LIGHTBLACK_EX
blue = Fore.LIGHTBLUE_EX
white = Fore.LIGHTWHITE_EX
reset = Style.RESET_ALL

# Get the directory where the script is located
script_dir = os.path.dirname(os.path.realpath(__file__))

# Construct the full paths to the files
data_file = os.path.join(script_dir, "data.txt")


# Clear the terminal
def clear_terminal():
    # For Windows
    if os.name == "nt":
        _ = os.system("cls")
    # For macOS and Linux
    else:
        _ = os.system("clear")


class ArixDEX:
    def arix_claimer(self, telegram_id):
        url = f"https://miner-webapp-pi.vercel.app/api/claim?id={telegram_id}"

        headers = {
            "authority": "miner-webapp-pi.vercel.app",
            "medthod": "POST",
            "path": f"/api/claim?id={telegram_id}",
            "scheme": "https",
            "Accept": "application/json, text/plain, */*",
            "Accept-Encoding": "gzip, deflate, br, zstd",
            "Accept-Language": "en-US,en;q=0.9",
            "Cache-Control": "no-cache",
            "Content-Length": "0",
            "Content-Type": "application/x-www-form-urlencoded",
            "Origin": "https://miner-webapp-pi.vercel.app",
            "Pragma": "no-cache",
            "Priority": "u=1, i",
            "Referer": "https://miner-webapp-pi.vercel.app/",
            "Sec-Ch-Ua": '"Google Chrome";v="125", "Chromium";v="125", "Not.A/Brand";v="24"',
            "Sec-Ch-Ua-Mobile": "?0",
            "Sec-Ch-Ua-Platform": '"Windows"',
            "Sec-Fetch-Dest": "empty",
            "Sec-Fetch-Mode": "cors",
            "Sec-Fetch-Site": "same-site",
            "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/125.0.0.0 Safari/537.36",
        }

        response = requests.post(url, headers=headers)
        if response.status_code == 200:
            print(f"{green}Claim: Done")
        else:
            print(f"{red}Error! Try again")

    def main(self):
        clear_terminal()
        banner = f"""
    {blue}Smart Airdrop {white}ArixDEX Auto Claimer
    t.me/smartairdrop2120
    
        """
        print(banner)
        data = open(data_file, "r").read().splitlines()
        while True:
            for no, telegram_id in enumerate(data):
                now = datetime.now().strftime("%d/%m/%Y %H:%M:%S")
                print(f"{black}[{now}] {white}--- Account Number: {no+1} ---")
                self.arix_claimer(telegram_id=telegram_id)
                print()
            wait_time = 30 * 60
            print(f"{yellow}Wait for {int(wait_time/60)} minutes!")
            time.sleep(wait_time)


if __name__ == "__main__":
    try:
        arix = ArixDEX()
        arix.main()
    except KeyboardInterrupt:
        sys.exit()
