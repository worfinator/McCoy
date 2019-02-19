#!/usr/bin/python

import ConfigParser, sys, subprocess, glob, notifier, ntpath, os.path, pycurl, json
from StringIO import StringIO

# Config file
config_file = '/etc/mccoy.conf'

# Defaults
remoteStatus = False;
notification_sent = False;

def getConfig(config_file):
    # lets get the config
    config = ConfigParser.ConfigParser()

    # loadconfig file if it exists
    if os.path.exists(config_file):
        config.read(config_file)
        return config
    else:
        print "Error: "+ config_file + " file not found"
        sys.exit()

def checkRemoteStatus(url):
    try:
        # use StringIO to capture the response from our push API call
        reponse = StringIO()

        # use Curl to post to the Instapush API
        request = pycurl.Curl()

        # set Instapush API URL
        request.setopt(request.URL, url)

        #our reponse
        request.setopt(request.WRITEFUNCTION, reponse.write)

        # log the post
        #logging.info(request.setopt(request.VERBOSE, True))

        # send the request
        request.perform()

        # capture the response from the server
        body = reponse.getvalue()

        # log the response
        #logging.info(body)

        # reset the reponse
        reponse.truncate(0)
        reponse.seek(0)

        # cleanup
        request.close()

        print("Remote is Alive")

        return True

    except:
        print("He's dead Jim!")

        return False

def sendNotification(notification_sent):
    message = config.get('mccoy','host_name') + " is no longer online \n"
    
    # add dropbox link
    if config.get('dropbox','share_link'):
        message += "\n " + config.get('dropbox','share_link')

    # Build the notification
    notifier.setConfig(config)
    notifier.setMessage(message) 
    notifier.sendMessage()

    return notification_sent

# Lets get the config
config = getConfig(config_file)

# Chech target is up
remoteStatus = checkRemoteStatus(config.get('mccoy','host_url'))

# Raise alert if not online
if not (remoteStatus):
    print("OMG ... freakout")
    notification_sent = sendNotification(notification_sent)

