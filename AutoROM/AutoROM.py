#!/usr/bin/env python3
import sys
import requests
import warnings
import hashlib
import tarfile
import pathlib
import click
import io

from typing import Dict
from collections import namedtuple

from tqdm import tqdm

if sys.version_info < (3, 9):
    import importlib_resources as resources
else:
    import importlib.resources as resources

CHECKSUM_MAP: Dict[str, str] = {
    "4b27f5397c442d25f0c418ccdacf1926": "adventure",
    "35be55426c1fec32dfb503b4f0651572": "air_raid",
    "f1a0a23e6464d954e3a9579c4ccd01c8": "alien",
    "acb7750b4d0c4bd34969802a7deb2990": "amidar",
    "de78b3a064d374390ac0710f95edde92": "assault",
    "89a68746eff7f266bbf08de2483abe55": "asterix",
    "ccbd36746ed4525821a8083b0d6d2c2c": "asteroids",
    "826481f6fc53ea47c9f272f7050eedf7": "atlantis2",
    "9ad36e699ef6f45d9eb6c4cf90475c9f": "atlantis",
    "8556b42aa05f94bc29ff39c39b11bff4": "backgammon",
    "00ce0bdd43aed84a983bef38fe7f5ee3": "bank_heist",
    "819aeeb9a2e11deb54e6de334f843894": "basic_math",
    "41f252a66c6301f1e8ab3612c19bc5d4": "battle_zone",
    "79ab4123a83dc11d468fb2108ea09e2e": "beam_rider",
    "136f75c4dd02c29283752b7e5799f978": "berzerk",
    "0a981c03204ac2b278ba392674682560": "blackjack",
    "c9b7afad3bfd922e006a6bfc1d4f3fe7": "bowling",
    "c3ef5c4653212088eda54dc91d787870": "boxing",
    "f34f08e5eb96e500e851a80be3277a56": "breakout",
    "028024fb8e5e5f18ea586652f9799c96": "carnival",
    "b816296311019ab69a21cb9e9e235d12": "casino",
    "91c2098e88a6b13f977af8c003e0bca5": "centipede",
    "c1cb228470a87beb5f36e90ac745da26": "chopper_command",
    "0ef64cdbecccb7049752a3de0b7ade14": "combat",
    "55ef7b65066428367844342ed59f956c": "crazy_climber",
    "8cd26dcf249456fe4aeb8db42d49df74": "crossbow",
    "106855474c69d08c8ffa308d47337269": "darkchambers",
    "0f643c34e40e3f1daafd9c524d3ffe64": "defender",
    "f0e0addc07971561ab80d9abe1b8d333": "demon_attack",
    "36b20c427975760cb9cf4a47e41369e4": "donkey_kong",
    "368d88a6c071caba60b4f778615aae94": "double_dunk",
    "5aea9974b975a6a844e6df10d2b861c4": "earthworld",
    "71f8bacfbdca019113f3f0801849057e": "elevator_action",
    "94b92a882f6dbaa6993a46e2dcc58402": "enduro",
    "6b683be69f92958abe0e2a9945157ad5": "entombed",
    "615a3bf251a38eb6638cdc7ffbde5480": "et",
    "b8865f05676e64f3bec72b9defdacfa7": "fishing_derby",
    "30512e0e83903fc05541d2f6a6a62654": "flag_capture",
    "8e0ab801b1705a740b476b7f588c6d16": "freeway",
    "081e2c114c9c20b61acf25fc95c71bf4": "frogger",
    "4ca73eb959299471788f0b685c3ba0b5": "frostbite",
    "211774f4c5739042618be8ff67351177": "galaxian",
    "c16c79aad6272baffb8aae9a7fff0864": "gopher",
    "8ac18076d01a6b63acf6e2cab4968940": "gravitar",
    "f16c709df0a6c52f47ff52b9d95b7d8d": "hangman",
    "f0a6e99f5875891246c3dbecbf2d2cea": "haunted_house",
    "fca4a5be1251927027f2c24774a02160": "hero",
    "7972e5101fa548b952d852db24ad6060": "human_cannonball",
    "a4c08c4994eb9d24fb78be1793e82e26": "ice_hockey",
    "e51030251e440cffaab1ac63438b44ae": "jamesbond",
    "718ae62c70af4e5fd8e932fee216948a": "journey_escape",
    "3276c777cbe97cdd2b4a63ffc16b7151": "joust",
    "5428cdfada281c569c74c7308c7f2c26": "kaboom",
    "4326edb70ff20d0ee5ba58fa5cb09d60": "kangaroo",
    "6c1f3f2e359dbf55df462ccbcdd2f6bf": "keystone_kapers",
    "0dd4c69b5f9a7ae96a7a08329496779a": "king_kong",
    "eed9eaf1a0b6a2b9bc4c8032cb43e3fb": "klax",
    "534e23210dd1993c828d944c6ac4d9fb": "koolaid",
    "4baada22435320d185c95b7dd2bcdb24": "krull",
    "5b92a93b23523ff16e2789b820e2a4c5": "kung_fu_master",
    "8e4cd60d93fcde8065c1a2b972a26377": "laser_gates",
    "2d76c5d1aad506442b9e9fb67765e051": "lost_luggage",
    "e908611d99890733be31733a979c62d8": "mario_bros",
    "ed2218b3075d15eaa34e3356025ccca3": "maze_craze",
    "df62a658496ac98a3aa4a6ee5719c251": "miniature_golf",
    "3347a6dd59049b15a38394aa2dafa585": "montezuma_revenge",
    "aa7bb54d2c189a31bb1fa20099e42859": "mr_do",
    "87e79cd41ce136fd4f72cc6e2c161bee": "ms_pacman",
    "36306070f0c90a72461551a7a4f3a209": "name_this_game",
    "113cd09c9771ac278544b7e90efe7df2": "othello",
    "fc2233fc116faef0d3c31541717ca2db": "pacman",
    "7e52a95074a66640fcfde124fffd491a": "phoenix",
    "6d842c96d5a01967be9680080dd5be54": "pitfall2",
    "3e90cf23106f2e08b2781e41299de556": "pitfall",
    "60e0ea3cbe0913d39803477945e9e5ec": "pong",
    "4799a40b6e889370b7ee55c17ba65141": "pooyan",
    "ef3a4f64b6494ba770862768caf04b86": "private_eye",
    "484b0076816a104875e00467d431c2d2": "qbert",
    "393948436d1f4cc3192410bb918f9724": "riverraid",
    "ce5cc62608be2cd3ed8abd844efb8919": "road_runner",
    "4f618c2429138e0280969193ed6c107e": "robotank",
    "240bfbac5163af4df5ae713985386f92": "seaquest",
    "dd0cbe5351551a538414fb9e37fc56e8": "sir_lancelot",
    "b76fbadc8ffb1f83e2ca08b6fb4d6c9f": "skiing",
    "e72eb8d4410152bdcb69e7fba327b420": "solaris",
    "72ffbef6504b75e69ee1045af9075f66": "space_invaders",
    "b702641d698c60bcdc922dbd8c9dd49c": "space_war",
    "a3c1c70024d7aabb41381adbfb6d3b25": "star_gunner",
    "a9531c763077464307086ec9a1fd057d": "superman",
    "4d7517ae69f95cfbc053be01312b7dba": "surround",
    "42cdd6a9e42a3639e190722b8ea3fc51": "tennis",
    "b0e1ee07fbc73493eac5651a52f90f00": "tetris",
    "0db4f4150fecf77e4ce72ca4d04c052f": "tic_tac_toe_3d",
    "fc2104dd2dadf9a6176c1c1c8f87ced9": "time_pilot",
    "fb27afe896e7c928089307b32e5642ee": "trondead",
    "7a5463545dfb2dcfdafa6074b2f2c15e": "turmoil",
    "085322bae40d904f53bdcc56df0593fc": "tutankham",
    "a499d720e7ee35c62424de882a3351b6": "up_n_down",
    "3e899eba0ca8cd2972da1ae5479b4f0d": "venture",
    "539d26b6e9df0da8e7465f0f5ad863b7": "video_checkers",
    "f0b7db930ca0e548c41a97160b9f6275": "video_chess",
    "3f540a30fdee0b20aed7288e4a5ea528": "video_cube",
    "107cc025334211e6d29da0b6be46aec7": "video_pinball",
    "cbe5a166550a8129a5e6d374901dffad": "warlords",
    "7e8aa18bc9502eb57daaf5e7c1e94da7": "wizard_of_wor",
    "ec3beb6d8b5689e867bafb5d5f507491": "word_zapper",
    "c5930d0e8cdae3e037349bfa08e871be": "yars_revenge",
    "eea0da9b987d661264cce69a7c13c3bd": "zaxxon",
}

# simply download tar file to specified dir
def download_tar_to_buffer(url="https://roms8.s3.us-east-2.amazonaws.com/Roms.tar.gz"):
    with requests.get(url, stream=True) as response:
        assert response.status_code == 200
        assert response.headers["Content-Type"] == "application/x-gzip"

        archive_size = int(response.headers["Content-Length"])
        assert archive_size > 0

        chunk_size = 2 ** 10
        with tqdm(
            unit="B",
            unit_scale=True,
            unit_divisor=chunk_size,
            desc="Downloading ROMs",
            leave=False,
            total=archive_size,
        ) as pbar:
            buffer = io.BytesIO()
            for chunk in response.iter_content(chunk_size=chunk_size):
                buffer.write(chunk)
                pbar.update(len(chunk))

            buffer.flush()
            buffer.seek(0)
            return buffer


# Extract each valid ROM into each dir in installation_dirs
def extract_roms_from_tar(buffer, packages, checksum_map, quiet):
    with tarfile.open(fileobj=buffer) as tarfp:
        for member in tarfp.getmembers():
            if not (member.isfile() and member.name.endswith(".bin")):
                continue

            # Read file from archive
            fp = tarfp.extractfile(member)
            bytes = fp.read()

            # Get hash
            md5 = hashlib.md5()
            md5.update(bytes)
            hash = md5.hexdigest()

            if hash not in checksum_map:
                warnings.warn(f"File {member.name} not supported.")
                continue

            # Get filename from checksum map
            # Filenames are ROM.bin, get ROM
            rom = checksum_map[hash]

            # Write ROM to all output folders
            for package in packages:
                file_name = pathlib.Path(package.format.format(rom=rom))
                rom_path = package.path / file_name

                if not rom_path.parent.exists():
                    rom_path.parent.mkdir(parents=True)

                with rom_path.open("wb") as romfp:
                    romfp.write(bytes)
                if not package.filter(str(rom_path)):
                    rom_path.unlink()
                    continue

                if not quiet:
                    print(f"Installed {rom_path}")

            # Cross off this ROM
            del checksum_map[hash]


SupportedPackage = namedtuple("SupportedPackage", ["path", "format", "filter"])


def find_supported_packages():
    installation_dirs = []

    # Try and find AutoROM.roms
    try:
        installation_dirs.append(
            SupportedPackage(
                resources.files("AutoROM") / "roms", "{rom}.bin", lambda _: True
            )
        )
    except ModuleNotFoundError:
        pass
    except TypeError:
        warnings.warn(
            "ale-py package seems to be empty. Perhaps try reinstalling ale-py."
        )

    # Try and find multi-agent-ale-py
    try:
        # Assume all ROMs are supported
        installation_dirs.append(
            SupportedPackage(
                resources.files("multi_agent_ale_py") / "roms",
                "{rom}.bin",
                lambda _: True,
            )
        )
    except ModuleNotFoundError:
        pass
    except TypeError:
        warnings.warn(
            "multi-agent-ale-py package seems to be empty. Perhaps try reinstalling multi-agent-ale-py."
        )

    return installation_dirs


def main(accept_license, install_dir, quiet):
    if install_dir is not None:
        packages = [
            SupportedPackage(pathlib.Path(install_dir), "{rom}.bin", lambda _: True)
        ]
    else:
        packages = find_supported_packages()

        if len(packages) == 0:
            print("Unable to find ale-py or multi-ale-py, quitting.")
            quit()

    print("AutoROM will download the Atari 2600 ROMs.\nThey will be installed to:")
    for package in packages:
        print(f"\t{package.path.resolve()}")
    print("\nExisting ROMs will be overwritten.")

    if not accept_license:
        license_msg = (
            "\nI own a license to these Atari 2600 ROMs.\n"
            "I agree to not distribute these ROMs and wish to proceed:"
        )
        if not click.confirm(license_msg, default=True):
            quit()

    # Make sure directories exist
    for package in packages:
        if not package.path.exists():
            package.path.mkdir()

    # Create copy of checksum map which will be mutated
    checksum_map = dict(CHECKSUM_MAP)
    try:
        buffer = download_tar_to_buffer()
        extract_roms_from_tar(buffer, packages, checksum_map, quiet)
    except tarfile.ReadError:
        print("Failed to read tar archive. Check your network connection?")
        quit()
    except requests.ConnectionError:
        print("Network connection error. Check your network settings?")
        quit()

    # Print missing ROMs
    for rom in checksum_map.values():
        print(f"Missing: {rom}")
    print("Done!")


@click.command()
@click.option(
    "-v",
    "-y",
    "--accept-license",
    is_flag=True,
    default=False,
    type=bool,
    help="Accept license agreement",
)
@click.option(
    "-d",
    "--install-dir",
    default=None,
    type=click.Path(exists=True),
    help="User specified install directory",
)
@click.option(
    "--quiet", is_flag=True, default=False, help="Suppress installation output."
)
def cli(accept_license, install_dir, quiet):
    main(accept_license, install_dir, quiet)


if __name__ == "__main__":
    cli()
