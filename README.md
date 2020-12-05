# AutoROM

[![Build Status](https://travis-ci.com/PettingZoo-Team/AutoROM.svg?branch=master)](https://travis-ci.com/PettingZoo-Team/AutoROM)

This package automaticaly installs Atari ROM files for Atari-Py (which Gym Depends on), multi-agent-ALE (which PettingZoo depends on), and ALE-Py (which will replaced multi-agent-ALE and Atari-Py in the future).

AutoROM automatically downloads the needed Atari ROMs from ROM hosting websites into the ALE-Py folder and Multi-Agent-ALE-py folder in a very simple manner:

```
pip3 install autorom
AutoROM
```

The specific ROM websites AutoROM pulls from are atarimania.com and s2roms.cc.

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
