import threading
import random
import sys
import irc.bot
import requests
import time

class TwitchBot(irc.bot.SingleServerIRCBot):
    def __init__(self, username, client_id, token, channel):
        
        self.client_id = client_id
        self.token = token
        self.channel = '#' + channel
        self.last_call = time.time()-30
        self.auto_msg_count = 0
        # Get the channel id, we will need this for v5 API calls
        url = 'https://api.twitch.tv/kraken/users?login=' + channel
        headers = {'Client-ID': client_id, 'Accept': 'application/vnd.twitchtv.v5+json'}
        r = requests.get(url, headers=headers).json()
        self.channel_id = r['users'][0]['_id']

        # Create IRC bot connection
        server = 'irc.chat.twitch.tv'
        port = 6667
        print ('Connecting to ' + server + ' on port ' + str(port) + '...')
        irc.bot.SingleServerIRCBot.__init__(self, [(server, port, 'oauth:'+token)], username, username)
        

    def on_welcome(self, c, e):
        print ('Joining ' + self.channel)

        # You must request specific capabilities before you can use them
        c.cap('REQ', ':twitch.tv/membership')
        c.cap('REQ', ':twitch.tv/tags')
        c.cap('REQ', ':twitch.tv/commands')
        c.join(self.channel)
        self.send_jebait()
        
    def send_jebait(self,e=None):#random.randint(10,100)
        self.t2 = threading.Timer(random.randint(60,600), self.send_jebait)
        self.t2.start()
        self.do_command(e, "!jebait", "bot inner script")
        self.auto_msg_count += 1
        print ("running automated message number ", self.auto_msg_count)
        
    def on_pubmsg(self, c, e):
        #check whether last call was more than 30 seconds ago
        #if time.time()-self.last_call <= 30:
            #if random.randint(1,10)<9:
                #self.timed_jebait(e)
        if time.time()-self.last_call != 30:
		
		# If a chat message starts with an exclamation point, try to run it as a command
		#print (e.tags['display-name'])
		
            if e.arguments[0][:1] == '?':
                print ("???")
                #self.timed_jebait(e)
            elif e.arguments[0][:1] == '!':
                self.last_call = time.time()
                cmd = e.arguments[0]
                print ('Received command: ' + cmd)
                for dic in e.tags:
                    if dic['key'] == 'display-name':
                        command_issuer = (dic['value'])
                self.do_command(e, cmd, command_issuer)
            pass
        else:
            #print("last message was"+ str(time.time()-self.last_call) +" time ago")
            pass

    def do_command(self, e, cmd, command_issuer):
        c = self.connection
        cmd = cmd.split(' ')
		
        # Poll the API to get current game.
        if cmd[0] == "!game":
            url = 'https://api.twitch.tv/kraken/channels/' + self.channel_id
            headers = {'Client-ID': self.client_id, 'Accept': 'application/vnd.twitchtv.v5+json'}
            r = requests.get(url, headers=headers).json()
            if not r['game']:
                c.privmsg(self.channel, r['display_name'] + ' Currently plays no game')
            else:
                c.privmsg(self.channel, r['display_name'] + ' currently testing ' + r['game'])

        # Poll the API the get the current status of the stream
        elif cmd[0] == "!title":
            url = 'https://api.twitch.tv/kraken/channels/' + self.channel_id
            headers = {'Client-ID': self.client_id, 'Accept': 'application/vnd.twitchtv.v5+json'}
            r = requests.get(url, headers=headers).json()
            if not r['status']:
                c.privmsg(self.channel, r['display_name'] + ' currently has no title')
            else:
                c.privmsg(self.channel, r['display_name'] + ' channel title is currently ' + r['status'])

        # Provide basic information to viewers for specific commands

        elif cmd[0] == "!testerooni":
            message = "Testing this piece of spaghettio code."            
            c.privmsg(self.channel, message)
			
        elif cmd[0] == "!rtd":
            c.privmsg(self.channel, str(random.randint(1,6)))
        elif cmd[0] == "!tooost":
            self.t2.cancel()
        elif cmd[0] == "!taaast":
            self.send_jebait(e)
        elif cmd[0] == "!hello":
            c.privmsg(self.channel, "hello, "+ command_issuer)
        elif cmd[0] == "!jebait":
            answers = [ "Forsen is streaming hearthstone again!",
                        "Have you checked outside? It's raining again",
                        "By now you must have consumed at least 1 liter of water",
                        "༼ ºل͟º༼ ºل͟º༼ ºل͟º༼ ºل͟º ༽ºل͟º ༽ºل͟º ༽YOU CAME TO THE WRONG DONGERHOOD༼ ºل͟º༼ ºل͟º༼ ºل͟º༼ ºل͟º ༽ºل͟º ༽ºل͟º ༽"
                       ]
            answer =answers[random.randint(0,len(answers)-1)]
            c.privmsg(self.channel, answer)
        elif cmd[0] == "!mod":
            if len(cmd) > 1:
                if cmd[1] == "/mod":
                    c.privmsg(self.channel, command_issuer + " what you trying there Kappa ")    
                else:
                    c.privmsg(self.channel, cmd[1] + " has just become a mod PogChamp")
            else:
                c.privmsg(self.channel, command_issuer + " has just become a mod PogChamp")
        # The command was not recognized
        #else:
            #c.privmsg(self.channel, "Did not understand command: " + cmd)
    def timed_jebait(self, e, cmd=None, command_issuer=None):
        self.do_command(e, "!jebait", "bot inner script")
    
    def endit(self):
        self.t2.cancel()
        
def main():
    if len(sys.argv) != 5:
        print("Usage: twitchbot <username> <client id> <token> <channel>")
        sys.exit(1)

    username  = sys.argv[1]
    client_id = sys.argv[2]
    token     = sys.argv[3]
    channel   = sys.argv[4]

    bot = TwitchBot(username, client_id, token, channel)
    while True:
        try:
            bot.start()
        except KeyboardInterrupt:
            bot.endit()
            print("ending thread")
            sys.exit()

if __name__ == "__main__":
    main()
