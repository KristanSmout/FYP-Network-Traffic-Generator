import sys,scapy,Core,Menus,time,Core,os,sys,time,socket
from scapy.all import *
from colorama import init,Fore
init()



def SimplePingGen():

    Core.RemoveLine()
    ValidIP = False
    try:
        while(ValidIP == False):
            TargetIP = input(str("Select Target IP > "))
            if(TargetIP.find(".") == -1):
                Core.RemoveLine()
                TargetIP = input(str("Select Target IP > "))
            else:
                ValidIP = True
                Core.RemoveLine()
                TargetIP = TargetIP
            
    except:
        ValidIP = False
    
    i = 0
    #request = send(IP(dst=TargetIP) /ICMP() /b"Hello World")
    #answer = sr1(request, verbose = 0, timeout = 2)

    while(i < 5):
        i = i + 1
        msg = Ether() / IP(dst = TargetIP, ttl = 10) / ICMP()
        TempPacketTime = msg.time
        ans = srp1(msg, verbose = 0, timeout = 2)
        if ans is not None:
            FakeVar = ("%d: %s" % (i, ans[IP].src))
            if(os.name == 'nt'):
                print(str('%0.3fms'%((ans.time - TempPacketTime)*1000)))
            else:
                print(str('%0.3fms'%((ans.time - TempPacketTime)*1000)))
            time.sleep(1)
            #print("%d: %s" % (i, ans[IP].src))
        else:
            print(Fore.RED + "Error" + Fore.RESET)
        #send(IP(dst=TargetIP)/ICMP()/"HelloWorld",verbose=0)
    input('Press Enter to return to the main menu')
    i = 0
    while(i<6):
        i = i + 1
        Core.RemoveLine()
    print(".")
    Core.ReturnToMenu(Menus.ConnectivityMenu)

        


def AdvancedPingGen():
    Core.RemoveLine()
    ValidIP = False
    try:
        while(ValidIP == False):
            TargetIP = input(str("Select Target IP > "))
            if(TargetIP.find(".") == -1):
                Core.RemoveLine()
                TargetIP = input(str("Select Target IP > "))
            else:
                ValidIP = True
                Core.RemoveLine()
                TargetIP = TargetIP
            
    except:
        ValidIP = False
    ShouldSpoof = input(str("Would you like to spoof IP (You will not get a response) [No] > "))
    try:
        if(ShouldSpoof.lower().find("y") != -1):
            ShouldSpoof = 'True'
            Core.RemoveLine()
            SpoofedIP = input(str("Input Spoofed IP > "))
        else:
            ShouldSpoof = False
    except:
        ShouldSpoof = False
        

        
    if(ShouldSpoof == False):
        s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        s.connect(("8.8.8.8", 80))
        SpoofedIP = s.getsockname()[0]
    Core.RemoveLine()
    try:
        TimeToLive = int(input('Enter TTL [10] > '))
        if(TimeToLive < 1):
            TimeToLive = 10
    except:
        TimeToLive = 10
    Core.RemoveLine()
    try:
        PingCounter = int(input('Enter times to ping [5] > '))
        if(PingCounter < 1):
            PingCounter = 5
    except:
        PingCounter = 5
    Core.RemoveLine()
       
    i = 0
    TotalTime = 0
    while(i < PingCounter):
        i = i + 1
        msg = Ether() / IP(src = SpoofedIP,dst = TargetIP, ttl = int(TimeToLive)) / ICMP()
        TempPacketTime = msg.time
        ans = srp1(msg, verbose = 0, timeout = 2)
        if ans is not None:
            FakeVar = ("%d: %s" % (i, ans[IP].src))
            if(os.name == 'nt'):
                print(str('%0.3fms'%((ans.time - TempPacketTime)*1000)))
            else:
                print(str('%0.3fms'%((ans.time - TempPacketTime)*1000)))
            TotalTime = TotalTime + (ans.time - TempPacketTime)
            time.sleep(1)
            #print("%d: %s" % (i, ans[IP].src))
        else:
            print(Fore.RED + "No Response" + Fore.RESET)
    if(os.name == 'nt'):
        print('Average trip time is %0.3fms'%((TotalTime * 1000) / int(PingCounter)))
    else:
        print('Average trip time is %0.3fms'%((TotalTime * 1000) / int(PingCounter)))
        
    input('Press Enter to return to the main menu')
    print('')
    
    y = 0
    while(y < i + 3):
        y = y + 1
        Core.RemoveLine()
    print(".")
    Core.ReturnToMenu(Menus.ConnectivityMenu)
    



def TracertGen():
    Core.RemoveLine()
    TargetIP = input(str("Select Target IP > "))
    for i in range(1,300):
        pkt = IP(dst=TargetIP, ttl=i) / UDP (dport=33434)
        reply = sr1(pkt, verbose=0, timeout = 2)
        if reply is None:
            
            print("%d Hops Away: " % i,Fore.RED + "Request Timed Out")
            #i = 1
            #break
        elif reply.type == 3:
            print("Reached " + str(reply.src))
            break
        else:
            print("%d Hops Away: " % i,reply.src)
            #print(str(i))
            
            
    input('Press Enter to return to the main menu')

    y = 0
    while(y < (i + 2)):
        Core.RemoveLine()
        y = y + 1
    #ReturnToMenu()

    print(".")
    Core.ReturnToMenu(Menus.ConnectivityMenu)
    #print("Generate Tracert HERE")






