#Ben Reichert, 1/25/13, 1:51am, 
#irc handle: benji
#simple bot with little to no functionality
#but demonstrates a simple python bot

import socket
 
network = 'iss.cat.pdx.edu'
port = 6667
irc = socket.socket ( socket.AF_INET, socket.SOCK_STREAM )
irc.connect ( ( network, port ) )
print irc.recv ( 4096 )
irc.send ( 'NICK benjibot\r\n' )
irc.send ( 'USER benjibot benjibot benjibot :Benji\'s Simple IRC Bot\r\n' )
irc.send ( 'JOIN #benjibot\r\n' )
irc.send ( 'PRIVMSG #benjibot :benjibot has joined the channel\r\n' )
while True:
   data = irc.recv ( 4096 )
   if data.find ( 'PING' ) != -1:
      irc.send ( 'PONG ' + data.split() [ 1 ] + '\r\n' )
   if data.find ( '!benjibot quit' ) != -1:
      irc.send ( 'PRIVMSG #benjibot :Fine, if you don\'t want me\r\n' )
      irc.send ( 'QUIT\r\n' )
   if data.find ( 'hello benjibot' ) != -1:
      irc.send ( 'PRIVMSG #benjibot : Hello!\r\n' )
   if data.find ( 'KICK' ) != -1:
      irc.send ( 'JOIN #benjibot\r\n' )
   if data.find ( 'benjibot benji' ) != -1:
      irc.send ( 'PRIVMSG #benjibot : benji is the almighty creator of myself \n for I am forever thankful.\r\n' )
   print data
