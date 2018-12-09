import time
from stem import Signal
from stem.control import Controller

import  torip
from colors import *

__author__ = "gauravssnl"
__credits__ = "abhishekmenon_"

def main():
	print(LYELLOW+ "_" * 50)
	print(WHITE + "Rotate Tor IP  Script" + RESTORE)
	print(LYELLOW + "_" * 50)
	print(LCYAN + "Author : " + LGREEN + __author__)
	print(LBLUE + "Credits : " + LRED + __credits__)
	print(GREEN + "_" * 50)
	print(YELLOW + "Please Wait")
	while True:
		torip.showIP()
		print(MAGENTA + "*" * 50)
		print (LBLUE + "Rotating IP")
		time.sleep(9)
		
		with Controller.from_port(port = 9051) as controller:
			passkey = "gauravssnl"
			controller.authenticate(passkey)
			controller.signal(Signal.NEWNYM)
        	

if __name__ == '__main__':
    main()
    print(RESTORE)