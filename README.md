# McCoy

Python script to monitor remote server and send alert notification when offline.

## Requirements

WatchDog uses the Python [Notifier](https://github.com/worfinator/Notifier) module to be already installed in the `/usr/local/bin/` directory in order to send emails and push notifications.

## Installation

Download and unpack [mccoy.py](mccoy.py) to the `/usr/local/bin` folder.

```bash
cp mccoy.py /usr/local/bin
chmod 755 /usr/local/bin/mccoy.py
```

Copy [etc/mccoy.conf](etc/mccoy.conf) to the `/etc/` directory

```bash
cp mccoy.conf /etc
```

## Configuration

Edit the [/etc/mccoy.conf](etc/mccoy.conf) file and add your settings.

`host_name` - name of host you wish to monitor
`host_url` - url of health check webpage on target host

## Execution

Add the mccoy.py script as a CRON job that runs every 1 minute using the following format

`1 * * * * /usr/local/bin/mccoy.py`
