#! /usr/bin/python
# jerryrig: a script to restart Jellyfin when "too many open files" log error detected

import sys, os, time, subprocess
from datetime import datetime, date, timedelta

while True:
    try:
        # set timestamps
        timestamp = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
        today = (datetime.now().strftime('%Y%m%d'))

        # set log file path with date
        log_file = "/var/log/jellyfin/jellyfin" + today + ".log"

        # open the log
        f = open(log_file, 'r')

        # read last line in log
        f.seek(0, os.SEEK_END)
        line = f.readline()

        # if the error isn't there, continue to keep rechecking
        if "too many open files" not in line.lower():
            os.system('clear')
            print(f'{timestamp}: jerryrig: monitoring current Jellyfin log:\nfile: {log_file}')
            time.sleep(0.1)
            continue

        # if error is there, restart Jellyfin, then continue to keep rechecking after 30 seconds
        if "too many open files" in line.lower():
            subprocess.run(["systemctl", "restart", "jellyfin"])
            print(f"{timestamp}: jerryrig: 'too many open files' error detected, restarted Jellyfin")
            time.sleep(30)
            continue
    except:
        # rechecking before file exists will error out - wait then continue rechecking
        os.system('clear')
        print(f'{timestamp}: jerryrig: waiting for log file...')
        time.sleep(5)
        continue
