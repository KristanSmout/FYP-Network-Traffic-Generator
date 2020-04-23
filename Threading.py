import threading,time
import InternalInformation as Internal

exitFlag = 0


class GlobalHostName(threading.Thread):
    def __init__(self, threadID,name):
      threading.Thread.__init__(self)
      self.threadID = threadID
      self.name = name
    def run(self):
     # print ("Starting " + self.name)
      GrabHostname()
     # print ("Exiting " + self.name)
def GrabHostname():
    #while(True):
    Internal.GetHostName()
       # print("Grabbed Hostname")
        #time.sleep(5)
        
class GlobalLocalIP(threading.Thread):
    def __init__(self, threadID,name):
      threading.Thread.__init__(self)
      self.threadID = threadID
      self.name = name
    def run(self):
     # print ("Starting " + self.name)
      GrabLocalIP()
     # print ("Exiting " + self.name)
def GrabLocalIP():
    #while(True):
    Internal.GetLocalIP()
      #  print("Grabbed LocalIP")
        #time.sleep(5)


class GlobalIPV4Grabber (threading.Thread):
    def __init__(self, threadID,name):
      threading.Thread.__init__(self)
      self.threadID = threadID
      self.name = name
    def run(self):
     # print ("Starting " + self.name)
      GrabGlobalIPV4()
     # print ("Exiting " + self.name)
def GrabGlobalIPV4():
    #while(True):
    Internal.GetGlobalIPV4()
      #  print("Grabbed GIPV4")
    #time.sleep(5)

        
class GlobalIPV6Grabber (threading.Thread):
    def __init__(self, threadID,name):
      threading.Thread.__init__(self)
      self.threadID = threadID
      self.name = name
    def run(self):
   #   print ("Starting " + self.name)
      GrabGlobalIPV4()
   #   print ("Exiting " + self.name)
def GrabGlobalIPV6():
    #while(True):
    Internal.GetGlobalIPV6()
      #  print("Grabbed GIPV6")
    #time.sleep(5)
