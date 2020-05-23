# AutoROM

[![Build Status](https://travis-ci.com/PettingZoo-Team/AutoROM.svg?branch=master)](https://travis-ci.com/PettingZoo-Team/AutoROM)

Atari ROM files are no longer automatically installed with Gym (or more specifically ALE-Py, which Gym depends on).

AutoROM automatically downloads the needed Atari ROMs from ROM hosting websites into the ALE-Py folder and Multi-Agent-ALE-py folder in a very simple manner:

```
pip3 install autorom
AutoROM
```

 The specific ROM websites AutoROM pulls from are atarimania.com and s2roms.cc.
