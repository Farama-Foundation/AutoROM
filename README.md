<p align="center">
    <img src="https://raw.githubusercontent.com/Farama-Foundation/AutoROM/master/autorom-text.png" width="500px"/>
</p>


AutoROM automatically installs Atari ROM files for ALE-Py (which Gymnasium Depends on) and multi-agent-ALE (which PettingZoo depends on, but will replaced by ALE-Py in the future).

AutoROM automatically downloads the needed Atari ROMs from ROM hosting websites into the ALE-Py folder and Multi-Agent-ALE-py folder in a very simple manner:

```
pip install autorom
AutoROM
```
> IMPORTANT: We do not have official support for Windows. However, if you are on Windows and encounter a DLL import error, you may need to install [OpenSSL v1.1.1S](https://slproweb.com/products/Win32OpenSSL.html).
> IMPORTANT: Libtorrent, which AutoROM uses, requires pip version >20.0 to be installed. On M1 macs, this may require updating your pip installation.

To specify a specific installation directory for your ROMs, use the `--install-dir` command line flag.
```
AutoROM --install-dir /path/to/install
```
This will install ROMs at "/path/to/install/ROM/".

Furthermore, you can accept the license agreement from the command-line with:
```
AutoROM --accept-license
```
OR when you are installing the Python package by specifying the extra `accept-rom-license`:
```
pip install autorom[accept-rom-license]
```
This command would download the ROMs during installation and make them immediately discoverable to `ale-py`.

## Packaging

AutoROM requires that you package it as a source distribution. We have a special script to build all our source distributions, i.e., `./scripts/build-dist.sh`. The resulting source distributions will be located in `dist/`. You can directly install this with `pip` even including the extra `accept-rom-license`. For example,

```
pip install --find-links dist/ --no-cache-dir AutoROM[accept-rom-license]
```
