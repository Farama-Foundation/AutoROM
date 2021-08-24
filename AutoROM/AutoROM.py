#!/usr/bin/env python3
import sys
import requests
import warnings
import hashlib
import tarfile
import pathlib
import click
import io

from collections import namedtuple

from tqdm import tqdm

if sys.version_info < (3, 9):
    import importlib_resources as resources
else:
    import importlib.resources as resources

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
def extract_roms_from_tar(buffer, packages, checksum_map):
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
            file_name = checksum_map[hash]

            # Write ROM to all output folders
            for package in packages:
                rom_path = package.path / file_name
                with rom_path.open("wb") as romfp:
                    romfp.write(bytes)
                if not package.filter(str(rom_path)):
                    rom_path.unlink()
                    continue

                print(f"Installed {rom_path}")

            # Cross off this ROM
            del checksum_map[hash]


SupportedPackage = namedtuple("SupportedPackage", ["path", "filter"])


def find_supported_packages():
    installation_dirs = []

    # Try and find ale-py
    try:

        # isSupportedROM filter. There's some multi-agent games that aren't supported in ale-py.
        def _ale_py_filter(path):
            from ale_py import ALEInterface

            return ALEInterface.isSupportedROM(path) is not None

        installation_dirs.append(
            SupportedPackage(resources.files("ale_py") / "roms", _ale_py_filter)
        )
    except ModuleNotFoundError:
        pass

    # Try and find multi-agent-ale-py
    try:
        # Assume all ROMs are supported
        installation_dirs.append(
            SupportedPackage(
                resources.files("multi_agent_ale_py") / "roms", lambda _: True
            )
        )
    except ModuleNotFoundError:
        pass

    return installation_dirs


@click.command()
@click.option(
    "--accept-license",
    is_flag=True,
    default=False,
    type=bool,
    help="Accept license agreement",
)
@click.option(
    "--install-dir",
    default=None,
    type=click.Path(exists=True),
    help="User specified install directory",
)
def main(accept_license, install_dir):
    if install_dir is not None:
        packages = [SupportedPackage(pathlib.Path(install_dir), lambda _: True)]
    else:
        packages = find_supported_packages()

        if len(packages) == 0:
            print("Unable to find ale-py or multi-ale-py, quitting.")
            quit()

    # Get checksums
    with resources.path("AutoROM", "checksums.txt") as checksum_file:
        with checksum_file.open(encoding="utf-8") as fp:
            # Filter out comments
            lines = filter(lambda line: not line.startswith("#"), fp.readlines())
            # Generate checksum map
            checksum_map = dict(map(lambda line: line.split(), lines))

    print("AutoROM will download the Atari 2600 ROMs from.\nThey will be installed to:")
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

    try:
        buffer = download_tar_to_buffer()
        extract_roms_from_tar(buffer, packages, checksum_map)
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


if __name__ == '__main__':
    main()
