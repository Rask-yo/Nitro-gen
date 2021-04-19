import discord
from discord import *
import discord.ext.commands
import urllib3
urllib3.disable_warnings()
import string
import random
import requests
import colorama
from colorama import *
import os
import subprocess
import time
import threading
from threading import Thread
from time import sleep

def entreprogram():
    print ("""
██████╗░░█████╗░░██████╗██╗░░██╗██╗░░░██╗░█████╗░
██╔══██╗██╔══██╗██╔════╝██║░██╔╝╚██╗░██╔╝██╔══██╗
██████╔╝███████║╚█████╗░█████═╝░░╚████╔╝░██║░░██║
██╔══██╗██╔══██║░╚═══██╗██╔═██╗░░░╚██╔╝░░██║░░██║
██║░░██║██║░░██║██████╔╝██║░╚██╗░░░██║░░░╚█████╔╝
╚═╝░░╚═╝╚═╝░░╚═╝╚═════╝░╚═╝░░╚═╝░░░╚═╝░░░░╚════╝░
     Made  By rask""")


    print("""
    [1] Discord Nitro Generator
    [2] Discord Nitro Checker
    [3] Disocrd nitro Generator & Checker (Sheeeeesh)
    [4] Exit
    """)

    choise = int(input('[?]: '))
    if choise == 1:
        codelen = 16
        letters = "ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789"
        lp = int(input("Enter The Number Of Unchecked Codes You Need: "))
        k = open('unchcekedcodes.txt', 'w')
        for i in range(lp):
            k.write('' .join(random.choice(letters) for i in range(codelen))  + '\n' )
        k.close()
        entreprogram()

    elif choise == 2:
        k = input("Enter The Code To Check: ")
        url = "https://discordapp.com/api/v6/entitlements/gisft-codes/" + k + "?with_application=false&with_subscription_plan=true"
        s = requests.session()
        response = s.get(url)
        if 'subscription_plan' in response.text:
            print(Fore.GREEN + "[VALID CODE] " + Fore.RESET)
            time.sleep(2)
        elif 'Access denied' in response.text:
            print(Fore.YELLOW + "Proxy Problem" + Fore.RESET)
            time.sleep(2)
        else:
            print(Fore.RED + "[INVALID CODE] " + k + Fore.RESET)
            time.sleep(2)
        entreprogram()

    elif choise == 3:
        os.system("cls")

        amount = int(input(
            f"\n{Fore.WHITE}[ {Fore.YELLOW}> {Fore.WHITE}] {Fore.LIGHTBLACK_EX}How much codes will be generated: {Fore.WHITE}"))
        print(
            f"\n{Fore.WHITE}[ {Fore.YELLOW}? {Fore.WHITE}] {Fore.LIGHTBLACK_EX}Classic Nitro is 16chars and Boost Nitro is 24chars")
        nitro = input(
            f"{Fore.WHITE}[ {Fore.YELLOW}> {Fore.WHITE}] {Fore.LIGHTBLACK_EX}Boost codes or Classic codes {Fore.WHITE}(boost or classic){Fore.LIGHTBLACK_EX}: {Fore.WHITE}")

        if "boost" in nitro or "classic" in nitro:
            pass
        else:
            print(
                f"{Fore.WHITE}[ {Fore.RED}! {Fore.WHITE}] {Fore.LIGHTBLACK_EX}Answer must be {Fore.WHITE}boost {Fore.LIGHTBLACK_EX}or {Fore.WHITE}classic")
            exit()

        checker = input(
            f"{Fore.WHITE}[ {Fore.YELLOW}> {Fore.WHITE}] {Fore.LIGHTBLACK_EX}Enable Checker {Fore.WHITE}(yes or no){Fore.LIGHTBLACK_EX}: {Fore.WHITE}")

        def scrape():
            scraped = 0
            f = open("proxies.txt", "a+")
            f.truncate(0)
            r = requests.get('https://api.proxyscrape.com/?request=displayproxies&proxytype=http&timeout=1500&ssl=yes')
            proxies = []
            for proxy in r.text.split('\n'):
                proxy = proxy.strip()
                if proxy:
                    proxies.append(proxy)
            for p in proxies:
                scraped = scraped + 1
                f.write((p) + "\n")
            f.close()
            print(
                f"{Fore.WHITE}[ {Fore.YELLOW}? {Fore.WHITE}] {Fore.LIGHTBLACK_EX}Scraped {Fore.WHITE}{scraped} {Fore.LIGHTBLACK_EX}proxies.")

        if checker == "yes":
            scrapep = input(
                f"{Fore.WHITE}[ {Fore.YELLOW}> {Fore.WHITE}] {Fore.LIGHTBLACK_EX}Auto proxy scrape {Fore.WHITE}(yes or no){Fore.LIGHTBLACK_EX}: {Fore.WHITE}")
            print(
                f"\n{Fore.WHITE}[ {Fore.YELLOW}? {Fore.WHITE}] {Fore.LIGHTBLACK_EX}If no, every check will be on random proxy.")
            mult = input(
                f"{Fore.WHITE}[ {Fore.YELLOW}> {Fore.WHITE}] {Fore.LIGHTBLACK_EX}Multiple checks for proxy {Fore.WHITE}(yes or no){Fore.LIGHTBLACK_EX}: {Fore.WHITE}")
            if scrapep == "yes":
                scrape()
        else:
            print(
                f"\n{Fore.WHITE}[ {Fore.YELLOW}? {Fore.WHITE}] {Fore.LIGHTBLACK_EX}If true, before code will be {Fore.WHITE}discord.gift/")
            prefix = input(
                f"{Fore.WHITE}[ {Fore.YELLOW}> {Fore.WHITE}] {Fore.LIGHTBLACK_EX}Prefix before codes {Fore.WHITE}(yes or no){Fore.LIGHTBLACK_EX}: {Fore.WHITE}")
            if "yes" in prefix or "no" in prefix:
                pass
            else:
                print(
                    f"{Fore.WHITE}[ {Fore.RED}! {Fore.WHITE}] {Fore.LIGHTBLACK_EX}Answer must be {Fore.WHITE}yes {Fore.LIGHTBLACK_EX}or {Fore.WHITE}no")
                exit()

        print(
            f"\n{Fore.WHITE}[ {Fore.YELLOW}? {Fore.WHITE}] {Fore.LIGHTBLACK_EX}Generating {Fore.WHITE}{amount}{Fore.LIGHTBLACK_EX} codes!")
        if checker != "yes":
            sleep(1)

        fulla = amount
        f = open("codes.txt", "w+", encoding="UTF-8")
        try:
            p = open("proxies.txt", encoding="UTF-8")
        except FileNotFoundError:
            p = open("proxies.txt", "w+", encoding="UTF-8")
            print(
                f"{Fore.WHITE}[{Fore.RED} ! {Fore.WHITE}]{Fore.LIGHTBLACK_EX} No proxies found in {Fore.WHITE}proxies.txt!{Fore.WHITE}")
            raise SystemExit

        rproxy = p.read().split('\n')
        for i in rproxy:
            if i == "" or i == " ":
                index = rproxy.index(i)
                del rproxy[index]
        p.close()

        if not rproxy:
            print(
                f"{Fore.WHITE}[{Fore.RED} ! {Fore.WHITE}]{Fore.LIGHTBLACK_EX} No proxies found in {Fore.WHITE}proxies.txt!{Fore.WHITE}")
            raise SystemExit

        if checker != "yes":
            while amount > 0:
                amount = amount - 1
                if "boost" in nitro:
                    code = ''.join([random.choice(string.ascii_letters + string.digits) for i in range(24)])
                else:
                    code = ''.join([random.choice(string.ascii_letters + string.digits) for i in range(16)])
                if prefix == "yes":
                    print(
                        f"{Fore.WHITE}[ {Fore.GREEN}+ {Fore.WHITE}] {Fore.LIGHTBLACK_EX}Generated code {Fore.WHITE}{code}")
                    f.write(f"discord.gift/{code}\n")
                else:
                    print(
                        f"{Fore.WHITE}[ {Fore.GREEN}+ {Fore.WHITE}] {Fore.LIGHTBLACK_EX}Generated code {Fore.WHITE}{code}")
                    f.write(f"{code}\n")

        else:
            while amount > 0:
                f = open(f"working-codes.txt", "a", encoding="UTF-8")
                try:
                    if not rproxy[0]:
                        print(
                            f"{Fore.WHITE}[ {Fore.RED}! {Fore.WHITE}] {Fore.LIGHTBLACK_EX}All proxies are invalid!{Fore.WHITE}")
                        exit()
                except:
                    print(
                        f"{Fore.WHITE}[ {Fore.RED}! {Fore.WHITE}] {Fore.LIGHTBLACK_EX}All proxies are invalid!{Fore.WHITE}")
                    exit()
                if mult == "yes":
                    proxi = rproxy[0]
                else:
                    proxi = random.choice(rproxy)
                proxies = {
                    "https": proxi
                }
                amount = amount - 1
                if "boost" in nitro:
                    code = ''.join([random.choice(string.ascii_letters + string.digits) for i in range(24)])
                else:
                    code = ''.join([random.choice(string.ascii_letters + string.digits) for i in range(16)])
                try:
                    url = requests.get(f"https://discordapp.com/api/v6/entitlements/gift-codes/{code}", proxies=proxies,
                                       timeout=3)
                    if url.status_code == 200:
                        print(
                            f"{Fore.WHITE}[ {Fore.GREEN}+ {Fore.WHITE}] {Fore.LIGHTBLACK_EX}Working Code {Fore.WHITE}{code}{Fore.WHITE}")
                        f.write(f"\ndiscord.gift/{code}")
                        f.close()
                    elif url.status_code == 404:
                        fulla = fulla - 1
                        print(
                            f"{Fore.WHITE}[ {Fore.RED}- {Fore.WHITE}] {Fore.LIGHTBLACK_EX}Invalid Code {Fore.WHITE}{code}")
                    elif url.status_code == 429:
                        fulla = fulla - 1
                        if mult == "yes":
                            print(
                                f"{Fore.WHITE}[ {Fore.RED}- {Fore.WHITE}] {Fore.LIGHTBLACK_EX}Proxy {Fore.WHITE}{proxi}{Fore.LIGHTBLACK_EX} is ratelimited! | Switching proxy")
                        else:
                            print(
                                f"{Fore.WHITE}[ {Fore.RED}- {Fore.WHITE}] {Fore.LIGHTBLACK_EX}Proxy {Fore.WHITE}{proxi}{Fore.LIGHTBLACK_EX} is ratelimited!")
                        index = rproxy.index(proxi)
                        del rproxy[index]
                    else:
                        fulla = fulla - 1
                        print(
                            f"{Fore.WHITE}[ {Fore.RED}! {Fore.WHITE}] {Fore.LIGHTBLACK_EX}Invalid Error! | Status code {Fore.WHITE}{url.status_code}")
                except:
                    index = rproxy.index(proxi)
                    del rproxy[index]
                    pw = open(f"proxies.txt", "w", encoding="UTF-8")
                    for i in rproxy:
                        pw.write(i + "\n")
                    pw.close()
                    fulla = fulla - 1
                    print(
                        f"{Fore.WHITE}[ {Fore.RED}- {Fore.WHITE}] {Fore.LIGHTBLACK_EX}Failed connecting to proxy {Fore.WHITE}{proxi}{Fore.LIGHTBLACK_EX} | Removing from list!")

        f.close()
        print(
            f"{Fore.WHITE}[ {Fore.YELLOW}? {Fore.WHITE}] {Fore.LIGHTBLACK_EX}Successfully generated {Fore.WHITE}{fulla} {Fore.LIGHTBLACK_EX}codes!{Fore.WHITE}")

        input()
        entreprogram()

    elif choise == 4:
        x = 4
    else:
        print("Invalid Choice!")
        time.sleep(2)
        entreprogram()






entreprogram()



