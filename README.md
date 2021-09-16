# AutoROM

[![Build Status](https://travis-ci.com/PettingZoo-Team/AutoROM.svg?branch=master)](https://travis-ci.com/PettingZoo-Team/AutoROM)

This package automaticaly installs Atari ROM files for Atari-Py (which Gym Depends on), multi-agent-ALE (which PettingZoo depends on), and ALE-Py (which will replaced multi-agent-ALE and Atari-Py in the future).

AutoROM automatically downloads the needed Atari ROMs from ROM hosting websites into the ALE-Py folder and Multi-Agent-ALE-py folder in a very simple manner:

```
pip install autorom
AutoROM
```

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

AutoROM requires that you package it as a source distribution. We have a special script to build the source distribution, i.e., `./scripts/build-sdist.sh`. The resulting source distribution will be located in `dist/`. You can directly install this with `pip` even including the extra `accept-rom-license`. For example,

```
pip install AutoROM-0.4.0.tar.gz[accept-rom-license]
```

## Citing

If you want to cite this repo for some reason, the bibtex is:

```
@misc{autorom2020,
  author = {Terry, Justin K and Jayakumar, Mario and Black, Benjamin},
  title = {AutoROM},
  year = {2020},
  publisher = {GitHub},
  note = {GitHub repository},
  howpublished = {\url{https://github.com/PettingZoo-Team/AutoROM}}
}
```
