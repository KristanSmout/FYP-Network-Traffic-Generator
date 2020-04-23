import sys,os,socket,threading,colorama
import Core as Core
import Menus as Menus
import InternalInformation as Internal
import Threading as thread
from colorama import init
init(autoreset=True)


def InitialRun():
    print(colorama.Fore.BLUE + "Kristan's Networking Tool" + "          " + colorama.Fore.RED)
    print("This is a prototype piece of software, the program is to be used as is with no support")
    print("Created by Kristan Smout     |    S018997h@student.staffs.ac.uk")
    Menus.DisplayLocalInformationPanel()

Core.ClearScreen()
InitialRun()
thread1 = thread.GlobalIPV4Grabber(1,"Global IPV4 Grabber Thread")
thread2 = thread.GlobalIPV6Grabber(1,"Global IPV6 Grabber Thread")
thread3 = thread.GlobalHostName(1,"Local Host4ame Grabber Thread")
thread4 = thread.GlobalLocalIP(1, "LocalIP address Grabber Thread")

thread1.start()
thread2.start()
thread3.start()
thread4.start()
Menus.PrintMainMenu()
