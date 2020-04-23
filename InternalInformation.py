import sys,os,socket,requests
from requests import get

#Global Variables
HostName = None
LocalIP = None
GlobalIPV4 = None
GlobalIPV6 = None


def CollectInformationPanelInformation():
    GetHostName() #Run GetHostName Function
    GetLocalIP() #Run GetLocalIP Function
    GetGlobalIPV4() #Run GetGlobalIPV4 Function
    GetGlobalIPV6() #Run GetGlobalIPV6 Function

def GetHostName():
    global HostName #Global Variable for the hostname
    try: #Attempt to run the code within the statement
        TempHostname = socket.gethostname() #Get the current hostname of the machine
        if TempHostname != HostName: #if currenthostname doesnt match then run code below
            HostName = TempHostname #Set hostname to the new hostname
        else: #If hostname is the same // Currently None
            HostName = "Error Obtaining LocalIP" #Change hostname to display the error
    except: #If there is an error running the code run the code below instead
        print("Error Obtaining HostName") #Print to the console there is an error
        
def GetLocalIP():
    global LocalIP
    try:
        #TempLocalIP = socket.gethostbyname(socket.gethostname())
        s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        s.connect(("8.8.8.8", 80))
        TempLocalIP = s.getsockname()[0]
        if TempLocalIP != LocalIP:
            LocalIP = TempLocalIP
        else:
             LocalIP = "Error Obtaining LocalIP"   
    except:
        print("Error Obtaining LocalIP")

def GetGlobalIPV4():
    global GlobalIPV4
    try:
        TempGlobalIPV4 = requests.get("https://api.ipify.org/").text
        if TempGlobalIPV4 != GlobalIPV4:
            if "." in TempGlobalIPV4:
                GlobalIPV4 = TempGlobalIPV4
            else:
                GlobalIPV4 = "Error Obtaining IPV4"
    except:
        print("Error Obtaining IPV4")
        
def GetGlobalIPV6():
    global GlobalIPV6
    try:
        TempGlobalIPV6 = requests.get("https://api6.ipify.org/").text
        if TempGlobalIPV6 != GlobalIPV6:
            if ":" in TempGlobalIPV6:
                GlobalIPV6 = TempGlobalIPV6
            else:
                GlobalIPV6 = "Error Obtaining IPV6"
    except:
        print("Error Obtaining IPV6")