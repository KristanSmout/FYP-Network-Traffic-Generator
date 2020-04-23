import sys,os,socket,Generation,Connectivity,Stress
import InternalInformation as Internal
import Core as Core
from colorama import init,Fore
from os import execle
init(autoreset=True)


#Menu Lists
MainMenu = ["   1) Packet Generation   | Generate Network Traffic","   2) Connectivity Menu   | Ensure Connectivity", "   3) Stress Testing Menu | Test Network Limit's"]

GenerationMenu = ["   1) HTTP   | Generate HHTP Traffic","   2) DHCP   | Generate DHCP Traffic","   3) DNS    | Generate DNS Traffic"]
ConnectivityMenu = ["   1) Ping Simple   | Check basic connectivity", "   2) Ping Advanced | check basic connectivity with custom parameters","   3) Tracert       | Show each """""hop" towards the target"""]
StressMenu = ["   1) UDP Flooder   | Test Port Flooding"]

ConfirmedLocalIP = ''

def DisplayLocalInformationPanel():
    Internal.CollectInformationPanelInformation()
    print("===============================")
    
    #Formatting Hostname
    if Internal.HostName == "Error Obtaining HostName":
        print("Hostname: " + Fore.RED + "{Internal.HostName}")
    else:
        print("Hostname: " + str(Internal.HostName))
    
    #Formatting LocalIP
    if Internal.LocalIP == "Error Obtaining LocalIP":
        print("Local IP:" + Fore.RED + "{Internal.LocalIP}")
    else:
            ConfirmedLocalIP = str(Internal.LocalIP)
            print("Local IP: " + str(Internal.LocalIP))
            
        
    #Formatting IPV4
    if Internal.GlobalIPV4 == "Error Obtaining IPV4":
        print("Global IPV4: " + Fore.RED + "{Internal.GlobalIPV4}")
    else:
        print("Global IPV4: " + str(Internal.GlobalIPV4))
        
    #Formatting IPV6
    if Internal.GlobalIPV6 == "Error Obtaining IPV6":
        print("Global IPV6: " + Fore.RED + str(Internal.GlobalIPV6))
    else:
        print("Global IPV6: " + str(Internal.GlobalIPV6))
    print("===============================")


def PrintMainMenu():
    print(*MainMenu, sep="\n")
    Selection = (input("\nSynapse> "))
    try:
        if Selection == "exit":
            quit()
        elif Selection == "reload":
            Core.ClearScreen()
            os.execl(sys.executable, sys.executable, *sys.argv)
        else:
            Selection = (int(Selection))
            if Selection == 1:
                SelectedMenu = (GenerationMenu)
                SelectedInput = "Synapse Connectivity> "
                SelectMenu(MainMenu,GenerationMenu)
            # conselection()
            elif Selection == 2:
                SelectedMenu = (ConnectivityMenu)
                SelectedInput = "Synapse Connectivity> "
                SelectMenu(MainMenu,ConnectivityMenu)
            # stressselection()
            elif Selection == 3:
                SelectedMenu = (StressMenu)
                SelectedInput = "Synapse Stress> "
                SelectMenu(MainMenu,StressMenu)
            else:
                print("Error Selection Not Valid")
    except:
        SelectMenu(MainMenu,MainMenu)

def PrintGenerationMenu():
    Selection = input("\nGeneration Menu > ")
    try:
        if Selection == "exit":
            #print("Spacer")
            SelectMenu(GenerationMenu,MainMenu)
        elif Selection == "reload":
            Core.ClearScreen()
            os.execl(sys.executable, sys.executable, *sys.argv)
        else:
            Selection = (int(Selection))
            if Selection == 1:
                Generation.HTTPGen()
            elif Selection == 2:
                Generation.DHCPGen()
            elif Selection == 3:
                Generation.DNSGen()
    except:
        SelectMenu(GenerationMenu,GenerationMenu)
    
def PrintConnectivityMenu():
    Selection = input("\nConnectivity Menu > ")
    try:
        if Selection == "exit":
            #print("Spacer")
            SelectMenu(ConnectivityMenu,MainMenu)
        elif Selection == "reload":
            Core.ClearScreen()
            os.execl(sys.executable, sys.executable, *sys.argv)
        else:
            Selection = (int(Selection))
            if Selection == 1:
                Connectivity.SimplePingGen()
            elif Selection == 2:
                Connectivity.AdvancedPingGen()
            elif Selection == 3:
                Connectivity.TracertGen()
    except:
        SelectMenu(ConnectivityMenu,ConnectivityMenu)
        print("Exception")
    
def PrintStressMenu():
    Selection = input("\nStress Menu > ")
    try:
        if Selection == "exit":
            #print("Spacer")
            SelectMenu(StressMenu,MainMenu)
        elif Selection == "reload":
            Core.ClearScreen()
            os.execl(sys.executable, sys.executable, *sys.argv)
        else:
            Selection = (int(Selection))
            if Selection == 1:
                Stress.UDPFlooderGen()
    except:
        SelectMenu(StressMenu,StressMenu)


def SelectMenu(CurrentMenu,SelectedMenu):
    for i in CurrentMenu:
        Core.RemoveLine()
    Core.RemoveLine()
    Core.RemoveLine()
   # print(SelectedMenu, sep="\n")
    
    SelectMenu = str(SelectedMenu)

    if str(SelectMenu) == str(MainMenu):
        PrintMainMenu()
    elif str(SelectMenu) == str(GenerationMenu):
        print(*GenerationMenu, sep="\n")
        PrintGenerationMenu()
    elif str(SelectMenu) == str(ConnectivityMenu):
        print(*ConnectivityMenu, sep="\n")
        PrintConnectivityMenu()
    elif str(SelectMenu) == str(StressMenu):
        print(*StressMenu, sep="\n")
        PrintStressMenu()
        
        

    