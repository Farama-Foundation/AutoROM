## AutoROM

[![Build Status](https://travis-ci.com/PettingZoo-Team/AutoROM.svg?branch=master)](https://travis-ci.com/PettingZoo-Team/AutoROM)

Due to a legal issue, Atari ROM files are no longer installed by default with the Gym library (or more specifically ALE-Py, which Gym depends on).

AutoROM automatically downloads the needed Atari ROMs from ROM hosting websites into the ALE-Py folder in a very simple manner:

```
pip3 install autorom
AutoROM
```

 The specific ROM websites AutoROM pulls from are gamulator.com, atarimania.com and s2roms.cc.
