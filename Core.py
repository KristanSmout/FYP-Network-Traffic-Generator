import os,sys,colorama,Menus
from colorama import init
init()

def ClearScreen():
    os.system('cls' if os.name == 'nt' else 'clear') # Check OS and run relevant command

def RemoveLine():
    if(os.name == 'nt'): #Check if current OS is windows
        CursorUp = '\x1b[1A' #ANSI escape for moving the cursor up
        EraseLine = '\x1b[2K' # ANSI escape to erase the current line
        print(CursorUp + EraseLine + CursorUp) # Move cursor up / Erase Line / Move cursor up
    else: # If system is not windows
        sys.stdout.write("\033[F") #ANSI escape for moving the cursor up
        sys.stdout.write("\033[K") #ANSI escape to erase the current line
        
def ReturnToMenu(CurrentMenu):
    Menus.SelectMenu(CurrentMenu,Menus.MainMenu)
