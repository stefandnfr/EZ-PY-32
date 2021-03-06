import network
import ubinascii
import utime
import time
import urequests as requests
import ujson


wlan_initalized = False
wlannetworks =[]
wlan = None
data = ""

def http_get(url):
	import socket
	_, _, host, path = url.split('/', 3)
	addr = socket.getaddrinfo(host, 3000)[0][-1]

	s = socket.socket()
	s.connect(addr)
	s.send(bytes('GET /%s HTTP/1.0\r\nHost: %s\r\n\r\n' % (path, host), 'utf8'))
	while True:
		data = s.recv(100)
		if data:
			print(str(data, 'utf8'), end='')
		else:
			break
	s.close()


def initWlan():
	print("init wlan")
	#get wlan networks
	global wlan
	wlan = network.WLAN(network.STA_IF) # create station interface
	wlan.active(True)	   # activate the interface

	nets = wlan.scan()
	wlannetworks = []
	for net in nets:
		wlannetworks.append(net[0].decode("utf-8")) 
	global networks
	networks = wlannetworks


def fetchNetwork():
	global wlan_initalized
	if not wlan_initalized:
		initWlan()
		wlan_initalized = True
	global networks 
	return networks

def fetchServer():
	global wlan
	global data
	try :
		import password 
		wlan.connect(password.essid, password.pw)
	except:
		print("could not connect wlan")
		data = "could not join wlan network"
	utime.sleep_ms(5000)
	if wlan.isconnected():
		try:
			res = requests.get(url='http://192.168.2.102:3000/data')
			data = res.text
		except:
			data = "server was not accessible"
	else:
		print("could not connect wlan")
		data = "could not join wlan network"		
	return data


def fetchNew():
	global data
	global wlan
	if wlan.isconnected():
		try:
			res = requests.get(url='http://192.168.2.102:3000/data')
			data = res.text
		except:
			data = "server was not accessible"
	else:
		data = "could not join wlan network"
	return data
