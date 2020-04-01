#!/usr/bin/env python
import requests
from bs4 import BeautifulSoup
import os
import ale_py
import zipfile

install_dir = ale_py.__file__
install_dir = install_dir[:-11] + "ROM/"

game_list = ["Adventure", "AirRaid", "Alien", "Amidar", "Assault", "Asterix", "Asteroids", "Atlantis",
"BankHeist", "BattleZone", "BeamRider", "Berzerk", "Bowling", "Boxing", "Breakout","Carnival",
"Centipede", "ChopperCommand","CrazyClimber","Defender","DemonAttack","DonkeyKong",
"DoubleDunk","ElevatorAction","Enduro", "FishingDerby","Freeway","Frogger","Frostbite",
"Galaxian","Gopher","Gravitar","Hero","IceHockey","JamesBond","JourneyEscape","Kaboom",
"Kangaroo","KeystoneKapers","Kingkong","Koolaid","Krull","KungFuMaster","LaserGates",
"LostLuggage","MontezumaRevenge","MrDo","MsPacman","NameThisGame","Phoenix","Pitfall",
"Pong","Pooyan","PrivateEye","QBert", "RiverRaid","RoadRunner","RoboTank","Seaques",
"SirLancelot","Skiing","Solaris","SpaceInvaders","StarGunner","Tennis",
"Tetris","TimePilot","Trondead","Turmoil","Tutankham","UpNDown","Venture",
"VideoPinball","WizardOfWor","YarsRevenge","Zaxxon", "Atlantis2", "Backgammon",
"BasicMath", "Blackjack", "Casino", "Crossbow", "DarkChambers", "Earthworld",
"Entombed", "ET", "FlagCapture", "Hangman", "HauntedHouse", "HumanCannonball",
"Klax", "MarioBros", "MiniatureGolf", "Othello", "Pacman", "Pitfall2", "SpaceWar",
"Superman", "Surround", "TicTacToe3D", "VideoCheckers", "VideoChess", "VideoCube",
"WordZapper"]

total_sublink_list = []

new_link_file = "link_map.txt"
f = open(new_link_file, "r")
extension_map = {}
final_map = {}
for x in f:
    payload = x.split("^^^")
    if len(payload[1]) > 1:
        game_name = payload[0].strip()
        game_url = payload[1].strip()
        extension = game_url[-4:]
        final_map[game_name] = game_url
        extension_map[game_name] = extension 
f.close()

print("AutoROM will download the Atari 2600 ROMs in link_map.txt from gamulator.com and s2roms.cc, and put them into " + install_dir + " for use with ALE-Py (and Gym).")
ans = input("I own a license to these Atari 2600 ROMs, agree not to distribute these ROMS, agree to the terms of service for gamulator.com and s2roms.cc, and wish to proceed (Y or N).")
if ans != "Y" and ans != "y":
    quit()

os.mkdir(install_dir)
for game_name in final_map:
    download = requests.get(final_map[game_name])
    file_title = install_dir +game_name + extension_map[game_name]
    new_file = open(file_title, "wb")
    new_file.write(download.content)
    new_file.close()
    sub_dir = install_dir + game_name + "/"
    os.mkdir(sub_dir)
    with zipfile.ZipFile(file_title, "r") as zip_ref:
        zip_ref.extractall(sub_dir)
    os.remove(file_title)
    print("Installed ",game_name)

