title: Simple Telnet Interface
date: 2014-12-27 19:37:38
tags:
---

## Emphasis on 'Simple'

This post will demonstrate how to quickly write a Telnet interface to your Hexo or other Markup-based blog. You can access the finished product using `telnet blog.danpopp.net` (on the default port 23).

### Why telnet?

Working with embedded systems, often times you may be tasked with creating console-based interfaces for device management. In an isolated environment, or other place where security is *not* a consideration, one of the quickest and dirtiest ways to accomplish this is with Telnet. 

Almost every OS has a Telnet client available, so it's convenient. But please bear in mind, data will be sent in plain-text, totally unencrypted and ripe for the eavesdropping. Do NOT expose your nuclear power plant's SCADA system over Telnet. You can optionally enable authentication, and encryption (via Telnet over SSH) but those topics are not covered here.

### Step 1: Gather your shit

You will need Python, pip, and the pip modules telnetsrv & gevent. You will need the build-essentials and python development libraries if you want to compile from source. Otherwise Debian based systems provide the python-gevent package via apt-get. Knowledge of Python will help, but it is not required. You should be able to aquire everything you need with your distributions built-in package management system. 

```` bash
# On Debian-based systems:
$ sudo apt-get install python python-pip python-gevent libpython-dev
$ pip install gevent telnetsrv
````

### Step 2: Write your interface
```` python
#!/bin/env python
import gevent, gevent.server, os, glob
from telnetsrv.green import TelnetHandler, command

class MyTelnetHandler(TelnetHandler):
    WELCOME = "Ahoy! Welcome Aboard!"
    PROMPT = "DANPOPP.NET/BLOG/>"
    POST = ""

    @command(['echo', 'copy', 'repeat'], hidden=True)
    def command_echo(self, params):
        '''<text to echo>
        Echo text back to the console.

        '''
        self.writeresponse( ' '.join(params) )
    
    @command('latest')
    def command_latest(self, params):
        '''
        Shows the latest post.

        '''
        newest = max(glob.iglob('*.[Mm][Dd]'), key=os.path.getctime)
        latest = open(newest, 'r')
        self.writeline(latest.read())
    
    @command('next')
    def command_next(self, params):
        '''
        Shows the next post (Chronologically).

        '''
        self.writeline(latest.read())
    
    @command('list')
    def command_list(self, params):
        '''
        Shows a list of available posts.

        '''
        for dirname, dirnames, filenames in os.walk('.'):
          for subdirname in dirnames:
            paths = os.path.join(dirname, subdirname)
          for filename in filenames:
            files = os.path.join(dirname, filename)
            self.writeline(files)
          if '.git' in dirnames:
            dirnames.remove('.git')

    @command('timer', hidden=True)
    def command_timer(self, params):
        '''<time> <message>
        In <time> seconds, display <message>.
        Send a message after a delay.
        <time> is in seconds.
        If <message> is more than one word, quotes are required.
        example:
        > TIMER 5 "hello world!"
        '''
        try:
            timestr, message = params[:2]
            time = int(timestr)
        except ValueError:
            self.writeerror( "Need both a time and a message" )
            return
        self.writeresponse("Waiting %d seconds...", time)
        gevent.spawn_later(time, self.writemessage, message)


server = gevent.server.StreamServer(("", 8023), MyTelnetHandler.streamserver_handle)
server.serve_forever()
````

## Step 3: Setup NAT & detonate

Place the script above in the same directory where you store your blog markup files (in Hexo, this is the `/source/_posts/` folder). Then, that's it, just run it and boom goes the dynamite.

```` bash
$ sudo iptables -A PREROUTING -t nat -i eth0 -p tcp --dport 23 -j DNAT --to 192.168.1.2:8023
$ sudo iptables -A FORWARD -p tcp -d 192.168.1.2 --dport 8023 -j ACCEPT
$ python telnet.py &
````
