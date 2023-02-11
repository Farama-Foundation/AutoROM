#!/usr/bin/env python3
import os
import sys
import time

import libtorrent as lt


def torrent_tar():
    # specify the save path
    save_path = os.path.dirname(__file__)

    # magnet uri
    uri = "magnet:?xt=urn:btih:a606d1dabf28e794cbc0f88f10d0b8225dc854b4&dn=Roms.tar.gz&tr=udp%3A%2F%2Ftracker.opentrackr.org%3A1337%2Fannounce&tr=http%3A%2F%2Ftracker.opentrackr.org%3A1337%2Fannounce&tr=udp%3A%2F%2F9.rarbg.com%3A2810%2Fannounce&tr=udp%3A%2F%2Ftracker.openbittorrent.com%3A6969%2Fannounce&tr=http%3A%2F%2Ftracker.openbittorrent.com%3A80%2Fannounce&tr=udp%3A%2F%2Fopentracker.i2p.rocks%3A6969%2Fannounce&tr=https%3A%2F%2Fopentracker.i2p.rocks%3A443%2Fannounce&tr=udp%3A%2F%2Fopen.stealth.si%3A80%2Fannounce&tr=udp%3A%2F%2Ftracker.torrent.eu.org%3A451%2Fannounce&tr=udp%3A%2F%2Ftracker2.dler.org%3A80%2Fannounce&tr=udp%3A%2F%2Ftracker.tiny-vps.com%3A6969%2Fannounce&tr=udp%3A%2F%2Ftracker.moeking.me%3A6969%2Fannounce&tr=udp%3A%2F%2Ftracker.dler.org%3A6969%2Fannounce&tr=udp%3A%2F%2Fpublic.tracker.vraphim.com%3A6969%2Fannounce&tr=udp%3A%2F%2Fp4p.arenabg.com%3A1337%2Fannounce&tr=udp%3A%2F%2Fopen.demonii.com%3A1337%2Fannounce&tr=udp%3A%2F%2Fmovies.zsw.ca%3A6969%2Fannounce&tr=udp%3A%2F%2Fipv4.tracker.harry.lu%3A80%2Fannounce&tr=udp%3A%2F%2Ffe.dealclub.de%3A6969%2Fannounce&tr=udp%3A%2F%2Fexplodie.org%3A6969%2Fannounce&tr=udp%3A%2F%2Fexodus.desync.com%3A6969%2Fannounce&tr=udp%3A%2F%2Fbt2.archive.org%3A6969%2Fannounce&tr=udp%3A%2F%2Fbt1.archive.org%3A6969%2Fannounce&tr=udp%3A%2F%2F6ahddutb1ucc3cp.ru%3A6969%2Fannounce&tr=https%3A%2F%2Ftracker.nanoha.org%3A443%2Fannounce&tr=https%3A%2F%2Ftracker.lilithraws.org%3A443%2Fannounce&tr=https%3A%2F%2Ftr.burnabyhighstar.com%3A443%2Fannounce&tr=http%3A%2F%2Fvps02.net.orel.ru%3A80%2Fannounce&tr=http%3A%2F%2Ftracker2.dler.org%3A80%2Fannounce&tr=http%3A%2F%2Ftracker.mywaifu.best%3A6969%2Fannounce&tr=http%3A%2F%2Ftracker.files.fm%3A6969%2Fannounce&tr=http%3A%2F%2Ftracker.dler.org%3A6969%2Fannounce&tr=http%3A%2F%2Ft.overflow.biz%3A6969%2Fannounce&tr=udp%3A%2F%2Fzecircle.xyz%3A6969%2Fannounce&tr=udp%3A%2F%2Fyahor.ftp.sh%3A6969%2Fannounce&tr=udp%3A%2F%2Fvibe.sleepyinternetfun.xyz%3A1738%2Fannounce&tr=udp%3A%2F%2Fuploads.gamecoast.net%3A6969%2Fannounce&tr=udp%3A%2F%2Ftracker1.bt.moack.co.kr%3A80%2Fannounce&tr=udp%3A%2F%2Ftracker.theoks.net%3A6969%2Fannounce&tr=udp%3A%2F%2Ftracker.tcp.exchange%3A6969%2Fannounce&tr=udp%3A%2F%2Ftracker.swateam.org.uk%3A2710%2Fannounce&tr=udp%3A%2F%2Ftracker.srv00.com%3A6969%2Fannounce&tr=udp%3A%2F%2Ftracker.skyts.net%3A6969%2Fannounce&tr=udp%3A%2F%2Ftracker.publictracker.xyz%3A6969%2Fannounce&tr=udp%3A%2F%2Ftracker.pomf.se%3A80%2Fannounce&tr=udp%3A%2F%2Ftracker.openbtba.com%3A6969%2Fannounce&tr=udp%3A%2F%2Ftracker.monitorit4.me%3A6969%2Fannounce&tr=udp%3A%2F%2Ftracker.lelux.fi%3A6969%2Fannounce&tr=udp%3A%2F%2Ftracker.leech.ie%3A1337%2Fannounce&tr=udp%3A%2F%2Ftracker.joybomb.tw%3A6969%2Fannounce&tr=udp%3A%2F%2Ftracker.jonaslsa.com%3A6969%2Fannounce&tr=udp%3A%2F%2Ftracker.filemail.com%3A6969%2Fannounce&tr=udp%3A%2F%2Ftracker.ddunlimited.net%3A6969%2Fannounce&tr=udp%3A%2F%2Ftracker.bitsearch.to%3A1337%2Fannounce&tr=udp%3A%2F%2Ftracker.auctor.tv%3A6969%2Fannounce&tr=udp%3A%2F%2Ftracker.artixlinux.org%3A6969%2Fannounce&tr=udp%3A%2F%2Ftracker.army%3A6969%2Fannounce&tr=udp%3A%2F%2Ftracker.altrosky.nl%3A6969%2Fannounce&tr=udp%3A%2F%2Ftracker.4.babico.name.tr%3A3131%2Fannounce&tr=udp%3A%2F%2Ftracker-udp.gbitt.info%3A80%2Fannounce&tr=udp%3A%2F%2Ftorrents.artixlinux.org%3A6969%2Fannounce&tr=udp%3A%2F%2Ftorrentclub.space%3A6969%2Fannounce&tr=udp%3A%2F%2Fthouvenin.cloud%3A6969%2Fannounce&tr=udp%3A%2F%2Ftamas3.ynh.fr%3A6969%2Fannounce&tr=udp%3A%2F%2Fsmtp-relay.odysseylabel.com.au%3A6969%2Fannounce&tr=udp%3A%2F%2Fsanincode.com%3A6969%2Fannounce&tr=udp%3A%2F%2Frun.publictracker.xyz%3A6969%2Fannounce&tr=udp%3A%2F%2Frun-2.publictracker.xyz%3A6969%2Fannounce&tr=udp%3A%2F%2Frep-art.ynh.fr%3A6969%2Fannounce&tr=udp%3A%2F%2Frekcart.duckdns.org%3A15480%2Fannounce&tr=udp%3A%2F%2Fqtstm32fan.ru%3A6969%2Fannounce&tr=udp%3A%2F%2Fpublic.publictracker.xyz%3A6969%2Fannounce&tr=udp%3A%2F%2Fpsyco.fr%3A6969%2Fannounce&tr=udp%3A%2F%2Fopen.tracker.ink%3A6969%2Fannounce&tr=udp%3A%2F%2Fopen.free-tracker.ga%3A6969%2Fannounce&tr=udp%3A%2F%2Fopen.dstud.io%3A6969%2Fannounce&tr=udp%3A%2F%2Fnew-line.net%3A6969%2Fannounce&tr=udp%3A%2F%2Fmoonburrow.club%3A6969%2Fannounce&tr=udp%3A%2F%2Fmirror.aptus.co.tz%3A6969%2Fannounce&tr=udp%3A%2F%2Fmail.zasaonsk.ga%3A6969%2Fannounce&tr=udp%3A%2F%2Fmail.artixlinux.org%3A6969%2Fannounce&tr=udp%3A%2F%2Fmadiator.com%3A6969%2Fannounce&tr=udp%3A%2F%2Fleefafa.tk%3A6969%2Fannounce&tr=udp%3A%2F%2Flaze.cc%3A6969%2Fannounce&tr=udp%3A%2F%2Fkokodayo.site%3A6969%2Fannounce&tr=udp%3A%2F%2Fkeke.re%3A6969%2Fannounce&tr=udp%3A%2F%2Fhtz3.noho.st%3A6969%2Fannounce&tr=udp%3A%2F%2Ffh2.cmp-gaming.com%3A6969%2Fannounce&tr=udp%3A%2F%2Ff1sh.de%3A6969%2Fannounce&tr=udp%3A%2F%2Fepider.me%3A6969%2Fannounce&tr=udp%3A%2F%2Felementsbrowser.com%3A6969%2Fannounce&tr=udp%3A%2F%2Fdownload.nerocloud.me%3A6969%2Fannounce&tr=udp%3A%2F%2Fcutscloud.duckdns.org%3A6969%2Fannounce&tr=udp%3A%2F%2Fconcen.org%3A6969%2Fannounce&tr=udp%3A%2F%2Fchouchou.top%3A8080%2Fannounce&tr=udp%3A%2F%2Fcarr.codes%3A6969%2Fannounce&tr=udp%3A%2F%2Fcamera.lei001.com%3A6969%2Fannounce&tr=udp%3A%2F%2Fbuddyfly.top%3A6969%2Fannounce&tr=udp%3A%2F%2Fbubu.mapfactor.com%3A6969%2Fannounce&tr=udp%3A%2F%2Fbt.ktrackers.com%3A6666%2Fannounce&tr=udp%3A%2F%2Fblack-bird.ynh.fr%3A6969%2Fannounce&tr=udp%3A%2F%2Fben.kerbertools.xyz%3A6969%2Fannounce&tr=udp%3A%2F%2Fbananas.space%3A6969%2Fannounce&tr=udp%3A%2F%2Fastrr.ru%3A6969%2Fannounce&tr=udp%3A%2F%2Fapp.icon256.com%3A8000%2Fannounce&tr=udp%3A%2F%2Fadmin.videoenpoche.info%3A6969%2Fannounce&tr=udp%3A%2F%2Fadmin.52ywp.com%3A6969%2Fannounce&tr=udp%3A%2F%2Faarsen.me%3A6969%2Fannounce&tr=udp%3A%2F%2F960303.xyz%3A6969%2Fannounce&tr=https%3A%2F%2Fxtremex.herokuapp.com%3A443%2Fannounce&tr=https%3A%2F%2Ftracker2.ctix.cn%3A443%2Fannounce&tr=https%3A%2F%2Ftracker1.520.jp%3A443%2Fannounce&tr=https%3A%2F%2Ftracker.tamersunion.org%3A443%2Fannounce&tr=https%3A%2F%2Ftracker.kuroy.me%3A443%2Fannounce&tr=https%3A%2F%2Ftracker.gbitt.info%3A443%2Fannounce&tr=https%3A%2F%2Ftracker.foreverpirates.co%3A443%2Fannounce&tr=https%3A%2F%2Ftracker.expli.top%3A443%2Fannounce&tr=https%3A%2F%2Ftr.abir.ga%3A443%2Fannounce&tr=https%3A%2F%2Ftr.abiir.top%3A443%2Fannounce&tr=https%3A%2F%2F1337.abcvg.info%3A443%2Fannounce&tr=http%3A%2F%2Fwepzone.net%3A6969%2Fannounce&tr=http%3A%2F%2Ftracker4.itzmx.com%3A2710%2Fannounce&tr=http%3A%2F%2Ftracker3.itzmx.com%3A6961%2Fannounce&tr=http%3A%2F%2Ftracker3.ctix.cn%3A8080%2Fannounce&tr=http%3A%2F%2Ftracker1.itzmx.com%3A8080%2Fannounce&tr=http%3A%2F%2Ftracker1.bt.moack.co.kr%3A80%2Fannounce&tr=http%3A%2F%2Ftracker.skyts.net%3A6969%2Fannounce&tr=http%3A%2F%2Ftracker.lelux.fi%3A80%2Fannounce&tr=http%3A%2F%2Ftracker.gbitt.info%3A80%2Fannounce&tr=http%3A%2F%2Ftracker.edkj.club%3A6969%2Fannounce&tr=http%3A%2F%2Ftracker.bt4g.com%3A2095%2Fannounce&tr=http%3A%2F%2Ftorrenttracker.nwc.acsalaska.net%3A6969%2Fannounce&tr=http%3A%2F%2Ft.acg.rip%3A6699%2Fannounce&tr=http%3A%2F%2Fopen.tracker.ink%3A6969%2Fannounce&tr=http%3A%2F%2Fopen.acgnxtracker.com%3A80%2Fannounce&tr=http%3A%2F%2Fjp.moeweb.pw%3A6969%2Fannounce&tr=http%3A%2F%2Fincine.ru%3A6969%2Fannounce&tr=http%3A%2F%2Ffxtt.ru%3A80%2Fannounce&tr=http%3A%2F%2Fbt.okmp3.ru%3A2710%2Fannounce&tr=http%3A%2F%2F1337.abcvg.info%3A80%2Fannounce"

    # libtorrent params
    ses = lt.session()
    params = lt.parse_magnet_uri(uri)
    params.save_path = save_path
    handle: lt.torrent_handle = ses.add_torrent(params)

    # download roms as long as state is not seeding
    timeit = 0
    while handle.status().state not in {4, 5}:
        if timeit >= 180:
            raise RuntimeError(
                "Terminating attempt to download ROMs after 180 seconds, this has failed, please report it."
            )
        elif timeit % 5 == 0:
            status: lt.torrent_status = handle.status()
            print(
                f"time={timeit}/180 seconds - Trying to download atari roms\n"
                f"\ttotal downloaded bytes={status.total_download}\n"
                f"\ttotal payload download={status.total_payload_download}\n"
                f"\ttotal failed bytes={status.total_failed_bytes}",
                file=sys.stderr,
            )

        # some sleep helps
        time.sleep(1.0)
        timeit += 1

    return save_path


if __name__ == "__main__":
    print(torrent_tar())
    print("asdfasdfdsf")
