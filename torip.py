import requests
from stem import Signal
from stem.control import Controller

from colors import  *


with Controller.from_port(port = 9051) as controller:
  passkey = "gauravssnl"
  controller.authenticate(passkey)
  controller.signal(Signal.NEWNYM)
proxies = {
  "http": "http://127.0.0.1:8118"
}
headers = {
  'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_9_1) AppleWebKit/537.73.11 (KHTML, like Gecko) Version/7.0.1 Safari/537.73.11'
}

def showIP():
	r = requests.get("http://icanhazip.com", proxies=proxies, headers=headers)
	print ( CYAN+ "Your current IP : " + GREEN +  r.text.strip() + RESTORE)
	
if __name__ == "__main__":
	showIP()
