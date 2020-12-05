#!/usr/bin/env python3
import requests
import os
import platform
import zipfile
import hashlib
from pyunpack import Archive
import shutil
from tqdm import tqdm

def test_unrar(test_loc, test_file):
    try:
        rar_file = Archive(test_file)
        rar_file.extractall(test_loc)
        os.remove(test_loc+"/README.md")
        return True
    except Exception as ex:
        if "Permission denied" in str(ex):
            print("Permission denied. Please retry with sudo AutoROM")
            exit()
        else:
            partial_ex_end = str(ex).find("patool error")
            print(str(ex)[:partial_ex_end])
        return False

# simply download rar file to specified dir
def download_rar(installation_dirs):
    install_dir = installation_dirs[0]
    rar_link = "http://www.atarimania.com/roms/Roms.rar"
    downloaded_rar = requests.get(rar_link, stream=True)
    rar_file_title = install_dir + "ROMs.rar"
    rar_file = open(rar_file_title, "wb")
    total_file_size = int(downloaded_rar.headers['Content-Length'])
    bars = 100
    download_chunk_size = int(total_file_size / bars)
    pbar_format = "{desc}:{percentage:3.0f}%|{bar}|{elapsed}{postfix}"
    for chunk in tqdm(downloaded_rar.iter_content(chunk_size=download_chunk_size), bar_format=pbar_format, total=bars, desc="Downloading ROMs", leave=False):
        rar_file.write(chunk)
    rar_file.close()
 
# given the location of a ROMs.rar file, extract its contents into a singular folder
def extract_rar_content(installation_dirs):
    # extract rar files
    # unzip each zip
    # calculate checksum of each RAR file
    install_dir = installation_dirs[0]
    rar_file_title = install_dir + "ROMs.rar"
    rar_file = Archive(rar_file_title)
    if os.path.exists(install_dir + "ROMS.zip"):
        os.remove(install_dir + "ROMS.zip")
    rar_file.extractall(install_dir)
    first_zip_title = install_dir + "ROMS.zip"
    zip_sub_dir = install_dir
    with zipfile.ZipFile(first_zip_title, "r") as zip_ref:
        zip_ref.extractall(zip_sub_dir)
    

def transfer_rom_files(installation_dirs, checksum_map):
    # go through every ROM in install_dir/delete/
    # if the ROM file matches a checksum, store in install dir
    install_dir = installation_dirs[0]
    zip_dir = install_dir + "ROMS/"
    for subdir, _, files in os.walk(zip_dir):
        for file in files:
            hash_md5 = hashlib.md5()
            with open(os.path.join(subdir, file), "rb") as f:
                for chunk in iter(lambda: f.read(4096), b""):
                    hash_md5.update(chunk)
                d = str(hash_md5.hexdigest())
                if d in checksum_map:
                    # transfer file here to name in checksum map
                    game_name = checksum_map[d][0:-4]
                    game_subdir = install_dir+game_name+"/"
                    if not os.path.exists(game_subdir):
                        os.mkdir(game_subdir)
                    os.rename(os.path.join(subdir, file), os.path.join(game_subdir, checksum_map[d]))
                    del checksum_map[d]

def clean_rar_files(installation_dirs):
    # delete Roms.rar
    # delete extracted HC ROMS.zip
    # delete extracted ROMS.zip
    # delete unzipped delete folder
    install_dir = installation_dirs[0]
    if os.path.exists(os.path.join(install_dir, "ROMS.rar")):
        os.remove(os.path.join(install_dir, "ROMS.rar"))
    if os.path.exists(os.path.join(install_dir, "ROMS.zip")):
        os.remove(os.path.join(install_dir, "ROMS.zip"))
    if os.path.exists(os.path.join(install_dir, "HC ROMS.zip")):
        os.remove(os.path.join(install_dir, "HC ROMS.zip"))
    if os.path.exists(os.path.join(install_dir, "ROMS/")):
        shutil.rmtree(os.path.join(install_dir, "ROMS/"))

def manual_downloads(installation_dirs, manual_map, checksum_map):
    install_dir = installation_dirs[0]
    for manual in manual_map:
        link = manual_map[manual]
        download = requests.get(link)
        file_title = install_dir + manual + ".zip"
        new_file = open(file_title, "wb")
        new_file.write(download.content)
        new_file.close()

        game_subdir = install_dir+manual+"/"
        if not os.path.exists(game_subdir):
            os.mkdir(game_subdir)
        with zipfile.ZipFile(file_title, "r") as zip_ref:
            zip_ref.extractall(game_subdir)
        os.remove(file_title)
        for sub in os.listdir(game_subdir):
            os.rename(game_subdir+sub, game_subdir+manual+".bin")

        hash_md5 = hashlib.md5()
        new_file = open(game_subdir+manual+".bin", "rb")
        for chunk in iter(lambda: new_file.read(4096), b""):
            hash_md5.update(chunk)
        d = str(hash_md5.hexdigest())
        new_file.close()

        if d in checksum_map:
            del checksum_map[d]
        else:
            print(d)

def main(license_accepted=False, specific_dir=None):
    ale_installed = True
    multi_ale_installed = True
    try:
        import ale_py
    except ImportError:
        ale_installed = False
    try:
        import multi_agent_ale_py
    except ImportError:
        multi_ale_installed = False


    installation_dirs = []

    if ale_installed:
        ale_install_dir = ale_py.__file__
        if ale_install_dir is not None:
            ale_install_dir = ale_install_dir[:-11] + "ROM/"
            installation_dirs.append(ale_install_dir)
        else:
            ale_installed = False 
    else:
        ale_install_dir = None 

    if multi_ale_installed:
        mulit_ale_install_dir = multi_agent_ale_py.__file__
        if mulit_ale_install_dir  is not None:
            mulit_ale_install_dir = mulit_ale_install_dir[:-11] + "ROM/"
            installation_dirs.append(mulit_ale_install_dir)
        else:
            multi_ale_installed = False
    else:
        mulit_ale_install_dir = None

    if not ale_installed and not multi_ale_installed:
        print("Neither ale_py or multi_ale_py installed, quitting.")
        quit()

    if specific_dir:
        dir_path = os.path.abspath(os.path.join(specific_dir, "ROM/")) + "/"
        installation_dirs = [dir_path]
        ale_install_dir = dir_path
        mulit_ale_install_dir = dir_path

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
        checksum_map[payload[0]] = payload[1]

    rar_installed = test_unrar(__location__, __location__ + "/test.rar")
    if not rar_installed:
        print("Unable to extract rar file, please make sure that you have unrar installed.")
        print("unrar can be installed with the following command: ")
        if platform.system() == "Darwin":
            print("brew install unrar")
        elif platform.system() == "Linux":
            print("sudo apt-get install unrar")
        quit()

    license_text = ""
    if ale_installed:
        license_text += ale_install_dir + "\nfor use with ALE-Py (and Gym)"
    if ale_installed and multi_ale_installed:
        license_text += " and also\n\t"
    if multi_ale_installed:
        license_text += mulit_ale_install_dir + "\nfor use with Multi-Agent-ALE-py."
    print("AutoROM will download the Atari 2600 ROMs in link_map.txt from",
        "atarimania.com and s2roms.cc. \nThey will be installed to\n\t" + 
        license_text + " Existing ROMS will be overwritten.")
    if not license_accepted:
        ans = input("\nI own a license to these Atari 2600 ROMs, agree not to "+
            "distribute these ROMS, \nagree to the terms of service for " +
            "atarimania.com and s2roms.cc, and wish to proceed (Y or N). ")


        if ans != "Y" and ans != "y":
            quit()

    if not os.path.exists(installation_dirs[0]):
        os.makedirs(installation_dirs[0])
    else:
        shutil.rmtree(installation_dirs[0])
        os.makedirs(installation_dirs[0])

    download_rar(installation_dirs)
    extract_rar_content(installation_dirs)
    transfer_rom_files(installation_dirs, checksum_map)
    clean_rar_files(installation_dirs)

    # manual files since RAR has some mismatched hashes
    manual_map = {}
    manual_map["tetris"] = "https://s2roms.cc/s3roms/Atari%202600/P-T/Tetris%202600%20%28Colin%20Hughes%29.zip"
    manual_downloads(installation_dirs, manual_map, checksum_map)

    # copy into second_dir
    if len(installation_dirs) > 1:
        for secondary in installation_dirs[1:]:
            if os.path.exists(secondary):
                shutil.rmtree(secondary)
            shutil.copytree(installation_dirs[0], secondary)

    for ch in checksum_map:
        print("Missing: ", checksum_map[ch])
    print("Done!")

if __name__ == "__main__":
    import sys
    import argparse

    parser = argparse.ArgumentParser(description="Process arguments")
    parser.add_argument(
        "-v", "--accept", action="store_true", help="Accept license agreement"
    )
    parser.add_argument(
        "-d", "--dir", type=str, help="Installation directory"
    )
    parser.set_defaults(accept=False, dir=None)

    args = parser.parse_args()
    main(args.accept, specific_dir=args.dir)
