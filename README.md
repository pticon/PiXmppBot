## What is it?

This script will allow you to communicate directly with your Raspberry Pi using Gtalk / Google Hangouts.

You can run it in any device that supports google hangouts

[Check the video](http://youtu.be/vd6RlkAXWRs)

## How can I install it?

**1.** Install Python 2.7
```bh
sudo apt-get install python-pip git-core python2.7-dev
```
**2.** Update easy_install
```bh
sudo easy_install -U distribute
```
**3.** Install GPIO, xmpppy and pydns modules.
```bh
sudo pip install RPi.GPIO pydns
sudo pip install --pre xmpppy
```
**3bis.** A bug could be present in the xmpppy modules
```
--- xmpp/transports.py.orig	2010-04-06 21:05:04.000000000 +0800
+++ xmpp/transports.py	2010-04-06 21:05:20.000000000 +0800
@@ -27,7 +27,7 @@ Transports are stackable so you - f.e. T
 Also exception 'error' is defined to allow capture of this module specific exceptions.
  """

-import socket,select,base64,dispatcher,sys
+import socket,ssl,select,base64,dispatcher,sys
 from simplexml import ustr
 from client import PlugIn
 from protocol import *
@@ -312,9 +312,9 @@ class TLS(PlugIn):
         """ Immidiatedly switch socket to TLS mode. Used internally."""
         """ Here we should switch pending_data to hint mode."""
         tcpsock=self._owner.Connection
-        tcpsock._sslObj    = socket.ssl(tcpsock._sock, None, None)
-        tcpsock._sslIssuer = tcpsock._sslObj.issuer()
-        tcpsock._sslServer = tcpsock._sslObj.server()
+        tcpsock._sslObj    = ssl.wrap_socket(tcpsock._sock, None, None)
+        tcpsock._sslIssuer = tcpsock._sslObj.getpeercert().get('issuer')
+        tcpsock._sslServer = tcpsock._sslObj.getpeercert().get('server')
         tcpsock._recv = tcpsock._sslObj.read
         tcpsock._send = tcpsock._sslObj.write
```
**4.** Clone this repository.
```bh
git clone https://github.com/pticon/PiXmppBot.git
```
**5** Enter in the folder.
```bh
cd PiXmppBot
```
**6.** Edit raspiBot.py.
```bh
sudo nano raspiBot.py
```
**7.** Search for (BOT_GTALK_USER, BOT_GTALK_PASS, and BOT_ADMIN) in lines 31-33. Edit them and save all the changes.
```bh
raspi_bot_setup
```
**8.** Run the script.
```bh
sudo python ./raspiBot.py
```

## Main commands:

As [mitchtech](https://github.com/mitchtech) said in [this blog entry](http://mitchtech.net/raspberry-pi-google-talk-robot/):
> 
```
[pinon|pon|on|high] [pin] : turns on the specified GPIO pin
[pinoff|poff|off|low] [pin] : turns off the specified GPIO pin
[write|w] [pin] [state] : writes specified state to the specified GPIO pin
[read|r] [pin]: reads the value of the specified GPIO pin
[available|online|busy|dnd|away|idle|out|xa] [arg1] : set gtalk state and status message to specified argument
[shell|bash] [arg1] : executes the specified shell command argument after ‘shell’ or ‘bash’
```
>

## Additional resources

- [Raspberry Pi y Google Hangouts (Spanish)](http://www.blog.ulisesgascon.com/raspberry-pi-y-google-hangouts) by [Ulises Gascon](https://github.com/UlisesGascon)
- [Raspberry Pi Google Talk Robot (English)](http://mitchtech.net/raspberry-pi-google-talk-robot/) by [Michael Mitchell](https://github.com/mitchtech)
