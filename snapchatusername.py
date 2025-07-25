import requests
import random
import string
import time
import os
import webbrowser

SNAPCHAT_LINK = "https://www.snapchat.com/add/z4ny4rm?share_id=TBI_jUSG6WI&locale=en-US"
FLAG_FILE = "snap_opened.txt"

def open_snapchat_link_once():
    if not os.path.exists(FLAG_FILE):
        print("Opening Snapchat link to add user...")
        webbrowser.open(SNAPCHAT_LINK)
        with open(FLAG_FILE, "w") as f:
            f.write("opened")
        time.sleep(5)

def print_logo():
    logo = r"""
 __   __  
 \ \ / /  
  \ V /   
   > <    
  / . \   
 /_/ \_\  

    Snapchat Username Tool
    Created by Zanyar Dawd
    """
    print(logo)

def check_username(username):
    url = f"https://www.snapchat.com/add/{username}"
    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64)"
    }
    try:
        response = requests.get(url, headers=headers, timeout=10)
        if response.status_code == 200:
            if "sorry" in response.text.lower():
                return "available"
            else:
                return "taken"
        else:
            return "available"
    except:
        return "available"

def option_check_from_file():
    if not os.path.exists("username.txt"):
        print("File username.txt not found.")
        return

    with open("username.txt", "r") as file:
        usernames = [line.strip() for line in file if line.strip()]

    if not usernames:
        print("File is empty.")
        return

    count_available = 0
    count_taken = 0

    for username in usernames:
        status = check_username(username)
        if status == "available":
            print(f"\033[92m{username} is AVAILABLE\033[0m")
            with open("avalibe.txt", "a") as f:
                f.write(username + "\n")
            count_available += 1
        else:
            print(f"\033[91m{username} is TAKEN\033[0m")
            with open("no_found.txt", "a") as f:
                f.write(username + "\n")
            count_taken += 1
        time.sleep(1)

    print(f"\nAvailable: {count_available}")
    print(f"Taken: {count_taken}")

def generate_usernames_for_length(length, count):
    letters = string.ascii_lowercase
    usernames = set()

    while len(usernames) < count:
        uname = ''.join(random.choices(letters, k=length))
        usernames.add(uname)

    return usernames

def option_generate_usernames():
    total_usernames = set()

    try:
        count_4 = int(input("How many 4-letter usernames do you want to create? "))
        count_5 = int(input("How many 5-letter usernames do you want to create? "))
        count_6 = int(input("How many 6-letter usernames do you want to create? "))
    except ValueError:
        print("Please enter a valid number.")
        return

    usernames_4 = generate_usernames_for_length(4, count_4)
    usernames_5 = generate_usernames_for_length(5, count_5)
    usernames_6 = generate_usernames_for_length(6, count_6)

    total_usernames.update(usernames_4)
    total_usernames.update(usernames_5)
    total_usernames.update(usernames_6)

    with open("username.txt", "w") as f:
        for uname in sorted(total_usernames):
            f.write(uname + "\n")

    print(f"\nTotal {len(total_usernames)} usernames created and saved to username.txt")

def main():
    print_logo()
    open_snapchat_link_once()
    while True:
        print("\n--- Snapchat Username Tool ---")
        print("1. Check usernames from file")
        print("2. Generate usernames (4/5/6 letters)")
        print("3. Exit")

        choice = input("Select option (1/2/3): ").strip()

        if choice == "1":
            option_check_from_file()
        elif choice == "2":
            option_generate_usernames()
        elif choice == "3":
            print("Exit.")
            break
        else:
            print("Invalid option. Try again.")

if __name__ == "__main__":
    main()
