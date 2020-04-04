#!/usr/bin/env python3
import requests
import os
import ale_py
import zipfile
import hashlib

def main(license_accepted=False):
    install_dir = ale_py.__file__
    install_dir = install_dir[:-11] + "ROM/"

    __location__ = os.path.realpath(os.path.join(os.getcwd(), os.path.dirname(__file__)))
    new_link_file = "link_map.txt"
    f = open(os.path.join(__location__, new_link_file), "r")
    extension_map = {}
    final_map = {}
    for x in f:
        payload = x.split("^^^")
        if len(payload[1]) > 1:
            game_name = payload[0].strip()
            game_url = payload[1].strip()
            extension = ".zip"
            final_map[game_name] = game_url
            extension_map[game_name] = extension
    f.close()

    checksum_file = "checksums.txt"
    ch = open(os.path.join(__location__, checksum_file), "rb")
    checksum_map = {}
    for c in ch:
        payload = c.split()
        payload[1] = payload[1].decode("utf-8")
        payload[0] = payload[0].decode("utf-8")
        checksum_map[payload[1]] = payload[0]

    print("AutoROM will download the Atari 2600 ROMs in link_map.txt from",
        "\ngamulator.com, atarimania.com and s2roms.cc, and put them into\n",
        install_dir, " \nfor use with ALE-Py (and Gym). Existing ROMS will be overwritten.")
    if not license_accepted:
        ans = input("I own a license to these Atari 2600 ROMs, agree not to "+
            "distribute these ROMS, \nagree to the terms of service for gamulator.com" +
            ", atarimania.com and s2roms.cc, and wish to proceed (Y or N).")


        if ans != "Y" and ans != "y":
            quit()

    if not os.path.exists(install_dir):
        os.mkdir(install_dir)
    failed_checksum_count = 0
    missing_checksum_count = 0
    for game_name in final_map:
        download = requests.get(final_map[game_name])
        file_title = install_dir + game_name + extension_map[game_name]
        new_file = open(file_title, "wb")
        new_file.write(download.content)
        new_file.close()
        sub_dir = install_dir + game_name + "/"
        if not os.path.exists(sub_dir):
            os.mkdir(sub_dir)
        sub_files = os.listdir(sub_dir)
        for s in sub_files:
            print("Removing old ",s)
        with zipfile.ZipFile(file_title, "r") as zip_ref:
            zip_ref.extractall(sub_dir)
        os.remove(file_title)
        # rename extracted files to .bin
        sub_files = os.listdir(sub_dir)
        for s in sub_files:
            new_s = game_name+".bin"
            os.rename(sub_dir+s, sub_dir+new_s)

        # print md5 hash
        hash_md5 = hashlib.md5()
        with open(sub_dir+new_s, "rb") as f:
            for chunk in iter(lambda: f.read(4096), b""):
                hash_md5.update(chunk)
        d = hash_md5.hexdigest()
        print("Installed ", game_name)
        hash_game_name = game_name+".bin" 
        if hash_game_name in checksum_map:
            if d != checksum_map[hash_game_name]:
                #print(game_name," checksum fail. Needed ", checksum_map[hash_game_name], "\nfound:", d)
                failed_checksum_count += 1
        else:
            missing_checksum_count += 1



if __name__ == "__main__":
    import sys
    license_accept = False
    if len(sys.argv) > 1:
        if sys.argv[1] == "-v":
            license_accept = True
    main(license_accept)