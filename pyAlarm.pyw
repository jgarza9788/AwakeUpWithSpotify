# stuff for System Tray Icon
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *

app = QApplication([])
app.setQuitOnLastWindowClosed(False)

# Create the icon
icon = QIcon("icon.png")

import os, json,datetime, re,time,subprocess
from pathlib import Path

#audio settings stuff
from ctypes import cast, POINTER
from comtypes import CLSCTX_ALL
from pycaw.pycaw import AudioUtilities, IAudioEndpointVolume

import portalocker


dir = os.path.dirname(__file__)
# print(dir)
settingsPath = os.path.join(dir,"alarmSettings.json").replace("\\","/")
settings = ""



# def setSystemVolume(level):
#     # from ctypes import cast, POINTER
#     # from comtypes import CLSCTX_ALL
#     # from pycaw.pycaw import AudioUtilities, IAudioEndpointVolume
#     devices = AudioUtilities.GetSpeakers()
#     interface = devices.Activate(
#         IAudioEndpointVolume._iid_, CLSCTX_ALL, None)
#     volume = cast(interface, POINTER(IAudioEndpointVolume))
#     volume.SetMasterVolumeLevelScalar(level,None)


# def getSystemVolume():
#     # from ctypes import cast, POINTER
#     # from comtypes import CLSCTX_ALL
#     # from pycaw.pycaw import AudioUtilities, IAudioEndpointVolume
#     devices = AudioUtilities.GetSpeakers()
#     interface = devices.Activate(
#         IAudioEndpointVolume._iid_, CLSCTX_ALL, None)
#     volume = cast(interface, POINTER(IAudioEndpointVolume))
#     # print(volume.GetMasterVolumeLevelScalar())
#     return round(volume.GetMasterVolumeLevelScalar(),4)



def createSettings():
    data = {}
    data["alarms"] = []
    data["alarms"].append({
        "enable": True,
        "file": "alarms\\Awake.mp3",
        "volume": 0.05,
        "time": 900,
        "SMTWRFS": "0111110",
        "exeDay": 0
    })
    data["alarms"].append({
        "enable": True,
        "file": "Hey_hey.mp3",
        "volume": 0.05,
        "time": 915,
        "SMTWRFS": "0111110",
        "exeDay": 0
    })
    # with open(settingsPath, 'w') as outfile:
    #     json.dump(data, outfile, indent=4)
    #     setSettings(data)
    with portalocker.Lock(settingsPath,'w', timeout=60) as outfile:
        json.dump(data, outfile, indent=4)
        # flush and sync to filesystem
        outfile.flush()
        os.fsync(outfile.fileno())


def getSettings():
    if os.path.isfile(settingsPath):
        with open(settingsPath,'r') as json_file:  
            # print("allData:: \n" + str(settings) + "\n")
            return json.load(json_file)
        # with portalocker.Lock(settingsPath,'w', timeout=60) as json_file:
        #     return json.load(json_file)
        #     # flush and sync to filesystem
        #     outfile.flush()
        #     os.fsync(outfile.fileno())
    else:
        createSettings()
        with open(settingsPath,'r') as f:
            return json.load(f)
        # with portalocker.Lock(settingsPath,'w', timeout=60) as f:
        #     return json.load(json_file)
        #     # flush and sync to filesystem
        #     outfile.flush()
        #     os.fsync(outfile.fileno())

def setSettings(data):
    # print("data: \n" + str(data))
    # with open(settingsPath, 'w') as outfile:
    #     json.dump(data, outfile, indent=4)
    with portalocker.Lock(settingsPath,'w', timeout=60) as outfile:
        json.dump(data, outfile, indent=4)
        # flush and sync to filesystem
        outfile.flush()
        os.fsync(outfile.fileno())

# settings = getSettings()
# setSettings(settings)
# exit()

#this is no longer being used...but keep here for reference
"""
def StartSpotify(_playList):
    os.system(os.path.join(dir,"Spotify_RunThis.vbs") + " " + _playList)
"""


#this is no longer being used...but keep here for reference
"""
def printTimes():
    settings = getSettings()
    color = ""

    # print(Fore.LIGHTGREEN_EX + "PlayList: {item}".format(item=settings["PlayList"]))
    # print(Fore.LIGHTGREEN_EX + "File: {item}".format(item=settings["File"]))
    print(Style.RESET_ALL)

    print("#, time, SMTWRFS, enable")
    print("*******************************")

    # now = datetime.datetime.now()
    i = 0
    while i < len(settings["alarms"]):

        if settings["alarms"][i]["enable"] == False :
            color = Fore.RED
        elif settings["alarms"][i]["exeDay"] == getDay():
            color = Fore.LIGHTBLUE_EX
        else:
            color = Fore.RESET

        print(color +  "{index} | {time} | {SMTWRFS} | {enable}".format(
            index=i, time=settings["alarms"][i]["time"], SMTWRFS=settings["alarms"][i]["SMTWRFS"],enable = settings["alarms"][i]["enable"]
            ))
        i+=1
    print(Style.RESET_ALL)
    # print("\n")
"""

# def getTime(withColon = False):
#     if withColon:
#         return str(datetime.datetime.now().time())[:5]
#     else:
#         return int(str(datetime.datetime.now().time())[:5].replace(":",""))

def getDay():
    return int(str(datetime.datetime.now().date())[:10].replace("-",""))


# def SMTWRFS(schedule):
#     # print(schedule)
#     dayOfTheWeek = datetime.date.isoweekday(datetime.datetime.now().date()) 
#     # dayOfTheWeek += 1
#     dayNumber = dayOfTheWeek % 7
#     # print(dayNumber)
#     char = schedule[dayNumber]
#     # print(char)
#     if char == "1":
#         return True
#     else:
#         return False


# def playAlarms():
#     settings = getSettings()

#     t = getTime()
#     # print(t)

#     d = getDay()
#     # print(d)



#     i = 0
#     while i < len(settings["alarms"]):

#         # print(SMTWRFS(settings["alarms"][i]["SMTWRFS"]) )

#         #enabled and has not played today
#         if settings["alarms"][i]["enable"] == True and SMTWRFS(settings["alarms"][i]["SMTWRFS"]) and settings["alarms"][i]["exeDay"] < d:
#             if settings["alarms"][i]["time"] <= t and settings["alarms"][i]["time"] + 10 >= t:
#                 # StartSpotify("\"" + settings["PlayList"] + "\"")
                
#                 if re.match("[A-Z]:.*",settings["alarms"][i]["file"]):
#                     os.startfile(settings["alarms"][i]["file"])
#                 else:
#                     os.startfile(os.path.join(dir,settings["alarms"][i]["file"]))

#                 icon = QIcon("alarm.png")
#                 tray.setIcon(icon)
#                 tray.setVisible(True)

#                 # os.startfile(os.path.join(dir,settings["alarms"][i]["file"]))
#                 settings["alarms"][i]["exeDay"] = d
#                 setSettings(settings)
#                 setSystemVolume(settings["alarms"][i]["volume"])
#                 print("*** playing Alarm" + str(i) + " ***")
#         i+=1

def disableUntilTomorrow():
    settings = getSettings()
    d = getDay()
    i = 0
    while i < len(settings["alarms"]):
        settings["alarms"][i]["exeDay"] = d
        i+=1
    setSettings(settings)

# disableUntilTomorrow()

def openSettings():
    os.startfile(settingsPath)


def QuitProgram():
    proc.terminate()
    sys.exit()

def MainMenu():
    # try:
        while True:
            # os.system('cls')
            # print( Back.LIGHTRED_EX + Fore.BLACK + Style.NORMAL + "***Press Ctrl+C to edit settings***")
            # print(Back.WHITE + Fore.BLACK + Style.DIM + "CurrentTime: " + str(getTime(True)) + " ")
            # print(Style.RESET_ALL)
            # printTimes()
            # print(Style.RESET_ALL)
            playAlarms()
            # print("string"[:2])

            time.sleep(1)

            icon = QIcon("icon.png")
            tray.setIcon(icon)
            tray.setVisible(True)
            
# # print(datetime.datetime.now().time())
#     except KeyboardInterrupt:
#         i = 1
#         os.startfile(settingsPath)
#         MainMenu()

# createSettings()

#MainMenu()

############################################################################
############################################################################
############################################################################



# Create the tray
tray = QSystemTrayIcon()
tray.setIcon(icon)
tray.setVisible(True)


# Create the menu
menu = QMenu()
action1 = QAction("Open Settings")
action1.triggered.connect(openSettings)
menu.addAction(action1)

action2 = QAction("Disable Until Tomorrow")
action2.triggered.connect(disableUntilTomorrow)
menu.addAction(action2)

action3 = QAction("Quit")
action3.triggered.connect(QuitProgram)
menu.addAction(action3)


# Add the menu to the tray
tray.setContextMenu(menu)

# os.startfile("timer.pyw")

timer = os.path.join(dir,"timer.pyw")
proc = subprocess.Popen(['py', timer], shell=True)

app.exec_()



# MainMenu()

