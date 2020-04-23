import Core,Menus,random,string,struct
from scapy.all import *

def HTTPGen():


    x = 0
    while(x <= 100):
        x = x + 1
        print("Line " + str(x))


    Address = 'None'
    try:
        Address = input('Please Enter Target address [www.google.co.uk] > ')
    except:
        Address = "www.google.co.uk"
    if(Address.find('.') == -1):
        Address = "www.google.co.uk"
        Core.RemoveLine()
    try:
        PacketsToSend = int(input(str("How many packets to send [1000] > ")))
    except:
        PacketsToSend = 10
        
    i = 0
    while(i <= 10):
        Core.RemoveLine()
        load_layer("http")
        req = HTTP()/HTTPRequest(
            Accept_Encoding=b'gzip, deflate',
            Cache_Control=b'no-cache',
            Connection=b'keep-alive',
            Host=str(Address),
            Pragma=b'no-cache'
        )
        try:
            a = TCP_client.tcplink(HTTP, Address, 80,)
           # Core.RemoveLine()
            print("Sending " + str(i) + " HTTP Packet")
            
            FakeAns = a.sr1(req)

            
        except:
            print("An Error Occured")
        #answser = a.sr1(req)
        a.close()
        i = i + 1
    Core.RemoveLine()
    print(str(i) + " HTTP Packet(s) Sent")
    print("Done")
   
  
HTTPGen()