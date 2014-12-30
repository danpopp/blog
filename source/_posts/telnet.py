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
    	# print path to all subdirectories first.
    	  for subdirname in dirnames:
            paths = os.path.join(dirname, subdirname)
   	# print path to all filenames.
  	  for filename in filenames:
            files = os.path.join(dirname, filename)
            self.writeline(files)
    	# Advanced usage:
    	# editing the 'dirnames' list will stop os.walk() from recursing into there.
   	  if '.git' in dirnames:
        # don't go into any .git directories.
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
