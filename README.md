I'm a big fan of the free & open source Plex alternative, [Jellyfin](https://github.com/jellyfin/jellyfin). It's great, but one bug a few people have encountered is the server sometimes randomly stops working, with the error "Too many open files" showing up. There are a few threads on this issue, but nothing definitive seems to have been found just yet. Fortunately, restarting Jellyfin with `systemctl restart jellyfin` clears it up.

I wrote this Python script to monitor the Jellyfin log file and look for "Too many open files". When the error appears, it will automatically restart Jellyfin. The script assumes that you have Jellyfin running as a systemd service, so it won't work for you otherwise without some tweaking.

## Requirements

**Python**

This is a Python script, so of course you need to have Python installed to run it. The command may vary depending on your system configuration. You can skip this step if you already know Python is installed.

Debian-based distributions: `sudo apt-get install python`

Arch-based distributions: `sudo pacman -S install python`

This script doesn't require any special packages!

## Installation & Usage

Give the script executable permissions if you'd like to run it simply with: `./jellyrig.py`:

`chmod +x jellyrig.py`

I recommend daemonizing the script, so that it stays running and runs automatically. There are numerous ways to achieve this depending on your system. For most Linux users, this can be done with systemd.

Create the systemd file using your editor of choice. With Nano, which comes with many Linux distributions:

`sudo nano /etc/systemd/system/jellyrig.service`

You'll have an empty file. Enter the following in the file, substituting the paths for your own as needed:

```[Unit]
Description=jellyrig
After=multi-user.target

[Service]
Type=simple
WorkingDirectory=/path/to/jellyrigfolder/
ExecStart=/usr/bin/python /path/to/jellyrigfolder/jellyrig.py
StandardInput=tty-force
Restart=always
RestartSec=5

[Install]
WantedBy=multi-user.target
```

Save and exit - in Nano, you can do this by pressing `CTRL-X`, then `Y`, then `Enter` to save & write the file.

Enable the jellyrig systemd and reload systemctl daemon:

`sudo systemctl enable jellyrig.service`

`sudo systemctl daemon-reload`

You can now start, stop, restart and check the status of Jellyrig:

`sudo systemctl start jellyrig`

`sudo systemctl stop jellyrig`

`sudo systemctl restart jellyrig`

`sudo systemctl status jellyrig`
