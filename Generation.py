import Core,Menus,random,string,struct,time
from scapy.all import *

conf.verb = 0

def HTTPGen():
    Core.RemoveLine()
    Address = 'None'
    try:
        Address = input('Please Enter Target address [www.google.co.uk] > ')
    except:
        Address = "www.google.co.uk"
    if(Address.find('.') == -1):
        Address = "www.google.co.uk"
        Core.RemoveLine()
    try:
        if(os.name == 'nt'):
            PacketsToSend = int(input(str("How many packets to send [10] > ")))
        else:
            PacketsToSend = int(input(str("How many packets to send [Max 10] > ")))
            if(PacketsToSend < 10):
                PacketsToSend = 10
    except:
        PacketsToSend = 10
    print(" ")
    i = 0
    while(i < PacketsToSend):
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
            Core.RemoveLine()
            print("Sent " + str(i) + "/" + str(PacketsToSend) + " HTTP Packet")
            FakeAns = a.sr1(req)
            scapy.http

            
        except:
            print("An Error Occured")
        #answser = a.sr1(req)
        a.close()
        i = i + 1
    Core.RemoveLine()
    Core.RemoveLine()
    print(str(i) + " HTTP Packet(s) Sent")

    input('Press Enter to return to the main menu')
    print(" ")
    print(" ")
    print(" ")
    print(" ")
    i = 0
    while(i < 6):
        i = i + 1
        Core.RemoveLine()
    Core.ReturnToMenu(Menus.GenerationMenu)
    
    #print("Generate HTTP HERE")

def DHCPGen():
   
    Core.RemoveLine()
    Multi = input('Do you want to send multiple DHCP Requests [no] > ')
    if(Multi.find('y') != -1):
        Multi = True
    else:
        Multi = False
    Core.RemoveLine()

    MacRand = input("Do you want to randomise MAC Address' [yes] > ")
    if(MacRand.find("n") !=-1):
        MacRand = False
    else:
        MacRand = True

    CanRun = False
    while(CanRun == False):
        Core.RemoveLine()
        TargetIP = input("Enter Target DHCP Server IP > ")
        if(TargetIP.find(".") !=-1):
            CanRun = True
            
    #Single packet with random Mac
    if(Multi == False and MacRand == True):

        Core.RemoveLine()
        WantedIP = input("Enter Desired IP Address [Random] > ")
        if(WantedIP.find(".") !=-1):
            fakevar = None
        else:

            ParsedIP = TargetIP.split(".")
            WantedIP = ParsedIP[0] + "." + ParsedIP[1] + "." + ParsedIP[2] + "." + str(random.randint(2,253))

        try:
            DHCPReq = Ether(src=RandMAC(),dst="ff:ff:ff:ff:ff:ff")/IP(src="0.0.0.0", dst="255.255.255.255")/UDP(sport=68, dport=67)/BOOTP(chaddr=RandMAC())/DHCP(options=[("message-type", "request"),("requested_addr", str(WantedIP)),("server_id", TargetIP),"end"])
            sendp(DHCPReq)
            
            Core.RemoveLine()
            Core.RemoveLine()
            #Core.RemoveLine()
            print(" ")
            print("Requested IP: " + str(WantedIP))
            
            input("Press Enter to return to main menu")
            #print(" ")
            Core.RemoveLine()
            Core.ReturnToMenu(Menus.GenerationMenu)
        except:
            FakeVar = None
            #Single Packet Chosen MAC
    elif(Multi == False and MacRand == False):
        Core.RemoveLine()
        WantedIP = input("Enter Desired IP Address [Random] > ")
        if(WantedIP.find(".") !=-1):
            fakevar = None
        else:

            ParsedIP = TargetIP.split(".")
            WantedIP = ParsedIP[0] + "." + ParsedIP[1] + "." + ParsedIP[2] + "." + str(random.randint(2,253))
            
        Core.RemoveLine()
        
        WantedMac = input("Enter Desired Mac Address [Random] > ")
        if(WantedMac.find(":") !=-1):
            fakevar = None
            
        else:
            FakeWantedMac = RandMAC()
            FakeWantedMac = str(FakeWantedMac)
            WantedMac = FakeWantedMac
            
        Core.RemoveLine()
        try:
            DHCPReq = Ether(src=WantedMac,dst="ff:ff:ff:ff:ff:ff")/IP(src="0.0.0.0", dst="255.255.255.255")/UDP(sport=68, dport=67)/BOOTP(chaddr=WantedMac)/DHCP(options=[("message-type", "request"),("requested_addr", str(WantedIP)),("server_id", TargetIP),"end"])
            sendp(DHCPReq)
            
            Core.RemoveLine()
          #  Core.RemoveLine()
            print("")
            
            print("Requested IP: " + str(WantedIP) + "  |  Source Mac: " + str(WantedMac))
            
            input("Press Enter to return to main menu")
            Core.RemoveLine()
           # print(" ")
            Core.ReturnToMenu(Menus.GenerationMenu)
        except:
            FakeVar = None
    elif(Multi == True and MacRand == True):
        Core.RemoveLine()
        ParsedIP = TargetIP.split(".")
        FakeIP = (ParsedIP[0] + "." + ParsedIP[1] + "." + ParsedIP[2] + ".")
        LowerRange = input(str("Please enter the lowest | " + FakeIP))
        LowerRange = int(LowerRange)
        Core.RemoveLine()
        HigherRange = input(str("Please enter the Highest | " + FakeIP))
        HigherRange = int(HigherRange)
        Core.RemoveLine()
        
        i = LowerRange
        print(" ")
        while(i <= HigherRange):
            Core.RemoveLine()            
            FakeWantedMac = RandMAC()
            FakeWantedMac = str(FakeWantedMac)
            WantedMac = FakeWantedMac
            WantedIP = str(FakeIP+str(i))
            
            try:                               
                DHCPReq = Ether(src=WantedMac,dst="ff:ff:ff:ff:ff:ff")/IP(src="0.0.0.0", dst="255.255.255.255")/UDP(sport=68, dport=67)/BOOTP(chaddr=WantedMac)/DHCP(options=[("message-type", "request"),("requested_addr", str(WantedIP)),("server_id", TargetIP),"end"])
                sendp(DHCPReq)
                print("Sent IP Request " + FakeIP + str(i) + "/" + FakeIP + str(HigherRange))
                time.sleep(0.2)
                i = i + 1
            except:
                print("Error")
        
        input("Press Enter to return to main menu")
        Core.RemoveLine()
        Core.ReturnToMenu(Menus.GenerationMenu)
    elif(Multi==True and MacRand == False):
        Core.RemoveLine()
        ParsedIP = TargetIP.split(".")
        FakeIP = (ParsedIP[0] + "." + ParsedIP[1] + "." + ParsedIP[2] + ".")
        LowerRange = input(str("Please enter the lowest | " + FakeIP))
        LowerRange = int(LowerRange)
        Core.RemoveLine()
        HigherRange = input(str("Please enter the Highest | " + FakeIP))
        HigherRange = int(HigherRange)
        Core.RemoveLine()
        
        i = LowerRange
        print(" ")
        while(i <= HigherRange):
            Core.RemoveLine()    
            
            
                    
            WantedMac = input("Enter Desired Mac Address [Random] > ")
            if(WantedMac.find(":") !=-1):
                fakevar = None
            else:
                FakeWantedMac = RandMAC()
                FakeWantedMac = str(FakeWantedMac)
                WantedMac = FakeWantedMac
            Core.RemoveLine()
            
            
            
            WantedIP = str(FakeIP+str(i))
            
            try:                               
                DHCPReq = Ether(src=WantedMac,dst="ff:ff:ff:ff:ff:ff")/IP(src="0.0.0.0", dst="255.255.255.255")/UDP(sport=68, dport=67)/BOOTP(chaddr=WantedMac)/DHCP(options=[("message-type", "request"),("requested_addr", str(WantedIP)),("server_id", TargetIP),"end"])
                sendp(DHCPReq)
                print("Sent IP Request " + FakeIP + str(i) + "/" + FakeIP + str(HigherRange))
                time.sleep(0.2)
                i = i + 1
            except:
                print("Error")
        
        input("Press Enter to return to main menu")
        Core.RemoveLine()
        Core.ReturnToMenu(Menus.GenerationMenu)
def DNSGen():
    ValidName = False
    Address = input('Please Enter DNS Server Address [1.1.1.1] > ')
    if(Address == ''):
        Address = '1.1.1.1'
    try:
        Core.RemoveLine()
        while(ValidName == False):
            Resolve = input('Please Enter Hostname To Resolve > ')
            if(Resolve.find('.') != -1):
                Core.RemoveLine()
                Resolve = Resolve
                ValidName = True
            else:
                ValidName = False
                Core.RemoveLine()
                
    except:
        ValidName = False    
            
    RecievedData = sr1(IP(dst=Address)/UDP(sport=53,dport=53)/DNS(rd=1,qd=DNSQR(qname=Resolve)),verbose=0)
    Recieved = (RecievedData[DNS].summary())
    #print(Recieved)
    Resolved = (Recieved.split('"'))
    print('Resolved Address is ' + Resolved[1])
    
    input('Press Enter to return to the main menu')
    Core.RemoveLine()
    Core.RemoveLine()
   # Core.RemoveLine()
    Core.ReturnToMenu(Menus.GenerationMenu)
