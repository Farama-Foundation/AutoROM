import subprocess
from subprocess import PIPE

"""
Commands to be run are:

transmission-daemon
transmission-remote -a "*.torrent"
transmission-remote -l until Done
transmission-remote -t all -r

"""

torrent_file = "https://webtorrent.io/torrents/tears-of-steel.torrent"

# start transmission daemon
process = subprocess.Popen(["transmission-daemon"], stdout=PIPE, stderr=PIPE)
stdout, stderr = process.communicate()
# begin torrent
process = subprocess.Popen(
    ["transmission-remote", "-a", torrent_file], stdout=PIPE, stderr=PIPE)
stdout, stderr = process.communicate()

# repeatedly list all torrent download statuses until torrent done
done = False
prev_download = ""
while not done:
    list_res = subprocess.check_output(["transmission-remote", "-l"])
    lines = list_res.splitlines()
    if len(lines) < 3:
        print("Error in starting torrent")
        break
    else:
        status_line = lines[1].decode("utf-8")
        status_line_arr = status_line.split()
        if prev_download != status_line_arr[1]:
            prev_download = status_line_arr[1]
            print(prev_download)
        if status_line_arr[1] == "100%":
            done = True

print("Successfully downloaded torrent")

# stop torrent seeding
subprocess.call(["transmission-remote", "-t", "all", "-r"])
