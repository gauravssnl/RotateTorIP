# RotateTorIP
Python scripts to test Tor IP  rotation


![ScreenShot]( https://github.com/gauravssnl/RotateTorIP/blob/master/Screenshot_20181207-125006.png )


## Requirements 
1. Termux Application for Android
2. python 3

## Steps
1. Install Tor. You can install Tor by using this command:
```code
apt install tor
``` 
You can test Tor installation by using `tor` command.

2. Install Privoxy. You can install Privoxy by using this command:
```code
apt install privoxy
```

3. You can test installation of Privoxy & its version by using this command:
```code
privoxy --version
```
4. Download the same version of Privoxy from the Privoxy homepage :  http://www.privoxy.org/sf-download-mirror/

Extract all those files to your /sdacrd/ directory (or your home directory).

5.Open Privoxy config file ( /sdcard/etc/privoxy/config) and add this new line to redirect all TCP requests to Tor (Tor listens for incoming request on localhost SOCKS5 proxy at Port 9050 ):
```code
forward-socks5 / 127.0.0.1:9050 .
```
Note that there is .(dot) symbol at last.

5.Start Privoxy server by running this command:
```code
sh privoxy.sh
```
6.Open new Terminal , and start Tor by using the `tor` command.

7.If everything is successful, you can check your Tor IP address by using this command:
```code
python torip.py
```
8.To check rotation of Tor IP & make sure that your IP address keeps on changing , use this command:
```code
python rotate.py
```
