import requests
import time
from colorama import Fore, Style, init

# Inisialisasi colorama
init(autoreset=True)

# URL API
detail_url = "https://terplayer.org/bot/user/detail"
spin_url = "https://terplayer.org/bot/user/luckAward"

def load_tokens(filename="tokens.txt"):
    with open(filename, 'r') as file:
        lines = file.readlines()
        tokens = [line.strip() for line in lines]
        return tokens

def get_user_details(id_token):
    headers = {
        "Authorization": "Bearer merlinadmin",
        "Id-Token": id_token
    }
    response = requests.get(detail_url, headers=headers)
    if response.status_code == 200:
        user_detail = response.json()
        if user_detail.get("code") == 0 and user_detail.get("success"):
            data = user_detail.get("data", {})
            return data
        else:
            print(Fore.RED + "Failed to retrieve user details: ", user_detail.get("msg", "Unknown error"))
    else:
        print(Fore.RED + "Failed to retrieve user details. Status Code:", response.status_code)
        print(Fore.RED + "Response:", response.text)
    return None

def perform_spin(id_token):
    headers = {
        "Authorization": "Bearer merlinadmin",
        "Id-Token": id_token
    }
    spin_response = requests.post(spin_url, headers=headers)
    if spin_response.status_code == 200:
        spin_result = spin_response.json()
        print(Fore.GREEN + f"Spin result: {spin_result}")
    else:
        print(Fore.RED + "Failed to perform spin. Status Code:", spin_response.status_code)
        print(Fore.RED + "Response:", spin_response.text)

def main():
    print(Fore.GREEN + f"==============================")
    print(Fore.CYAN + Style.BRIGHT + "Terpolly Auto Spin")
    print(Fore.CYAN + "Channel: https://t.me/ugdairdrop")
    print(Fore.GREEN + f"==============================")
    print(Fore.YELLOW + "Boleh Kalian Recode Scrip Tapi Sertakan Source!!!!!\n")
    
    tokens = load_tokens()
    while True:
        for id_token in tokens:
            user_data = get_user_details(id_token)
            if user_data:
                bot_user_name = user_data.get("botUserName", "N/A")
                tpusd = user_data.get("tpusd", "N/A")
                sync_invite_count = user_data.get("syncInviteCount", 0)

                print(Fore.BLUE + f"\nAccount performing spin: {bot_user_name}")
                print(Fore.BLUE + f"Balance: {tpusd}")
                print(Fore.BLUE + f"Spin Avaible: {sync_invite_count}")
                print(Fore.YELLOW + f"==============================")

                # Melakukan spin sebanyak 3 kali atau sesuai syncInviteCount jika tersedia
                spins_to_perform = min(3, sync_invite_count)
                for _ in range(spins_to_perform):
                    perform_spin(id_token)

        # Tunggu 6 jam sebelum melakukan pengecekan dan spin lagi
        print(Fore.RED + "\nWaiting for 6 hours before next round...")
        time.sleep(6 * 3600)

if __name__ == "__main__":
    main()
