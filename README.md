Due to a recent legal issue, OpenAI is no longer able to include Atari ROM files in their Gym library (or ALE-Py, the package Gym uses for their Atari logic). This requires users to add the needed the ROMs themselves. One such source of these ROM files is torrents. AutoROM automates the process of downloading the Atari ROMs from torrents, and inserting them into ALE-Py so that they can be used in Gym.

To use:

`brew install transmission-cli` or `apt install transmission-cli` or similiar

```
pip3 install autorom
AutoROM
```

We currently don't support Windows because none of us use it, but we'd welcome a PR for Windows support.

Disclaimer:

AutoROM in no way helps distribute Atari ROMs. It simply allows people to install them from existing sources on the internet in a simplified manner. AutoROM makes no claims regarding it's suitability of use or about the legality or ethics of downloading Atari ROM files via the bit torrent. AutoROM does not create the included torrents, it simply uses ones that already exist.
