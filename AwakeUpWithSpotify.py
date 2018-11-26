import os, json,datetime, re,time
from pathlib import Path

from ctypes import cast, POINTER
from comtypes import CLSCTX_ALL
from pycaw.pycaw import AudioUtilities, IAudioEndpointVolume

"""
import colorama
"""
from colorama import init,Fore, Back, Style
init()
# print(Fore.RED + 'some red text')
# print(Back.GREEN + 'and with a green background')
# print(Style.BRIGHT + 'and in dim text')
# print(Style.RESET_ALL)
# print('back to normal now')
"""
"""


dir = os.path.dirname(__file__)
# print(dir)
settingsPath = os.path.join(dir,"alarmSettings.json").replace("\\","/")
settings = ""
alarmIndex = 0

# print(settingsPath)

def setSystemVolume(level):
    # from ctypes import cast, POINTER
    # from comtypes import CLSCTX_ALL
    # from pycaw.pycaw import AudioUtilities, IAudioEndpointVolume
    devices = AudioUtilities.GetSpeakers()
    interface = devices.Activate(
        IAudioEndpointVolume._iid_, CLSCTX_ALL, None)
    volume = cast(interface, POINTER(IAudioEndpointVolume))
    volume.SetMasterVolumeLevelScalar(level,None)


def getSystemVolume():
    # from ctypes import cast, POINTER
    # from comtypes import CLSCTX_ALL
    # from pycaw.pycaw import AudioUtilities, IAudioEndpointVolume
    devices = AudioUtilities.GetSpeakers()
    interface = devices.Activate(
        IAudioEndpointVolume._iid_, CLSCTX_ALL, None)
    volume = cast(interface, POINTER(IAudioEndpointVolume))
    # print(volume.GetMasterVolumeLevelScalar())
    return round(volume.GetMasterVolumeLevelScalar(),4)



def createSettings():
    data = {}
    data["maxSystemVolume"] = getSystemVolume()
    data["offTilNextDay"] = False
    data["offDay"] = ""
    data["PlayList"] = "Covers"
    data["alarms"] = []
    data["alarms"].append({
        "enable": True,
        "time": 900,
        "SMTWRFS": "0111110",
        "exeDay": 0
    })
    data["alarms"].append({
        "enable": True,
        "time": 915,
        "SMTWRFS": "0111110",
        "exeDay": 0
    })
    with open(settingsPath, 'w') as outfile:
        json.dump(data, outfile, indent=4)
        setSettings(data)



# def createSettings():
#     data = {}
#     data["spotifyPath"] = getSpotifyPath()
#     data["maxSystemVolume"] = 50
#     data["snoozeTime"] = 900000
#     data["offTilNextDay"] = False
#     data["offDay"] = ""
#     data["alarms"] = []
#     data["alarms"].append({
#         "name": "00",
#         "enable": True,
#         "time": "900",
#         "repeat": True,
#         "repeatDays": "MTWRF",
#         "allowSnooze": True,
#         "URI": "spotify:user:spotify:playlist:37i9dQZF1DX0UrRvztWcAU"
#     })
#     data["alarms"].append({
#         "name": "01",
#         "enable": True,
#         "time": "915",
#         "repeat": True,
#         "repeatDays": "MTWRF",
#         "allowSnooze": True,
#         "URI": "spotify:user:spotify:playlist:37i9dQZF1DX0UrRvztWcAU"
#     })
#     with open(settingsPath, 'w') as outfile:
#         json.dump(data, outfile, indent=4)


def getSettings():
        if os.path.isfile(settingsPath):
            with open(settingsPath) as json_file:  
                # print("allData:: \n" + str(settings) + "\n")
                return json.load(json_file)
        else:
            createSettings()
            with open(settingsPath) as f:
                return json.load(f)




def setSettings(data):
    # print("data: \n" + str(data))
    with open(settingsPath, 'w') as outfile:
        json.dump(data, outfile, indent=4)


# def getSpotifyPath():
#     thisString = str(Path.home()) + "\\AppData\\Roaming\\Spotify\\Spotify.exe"
#     # print(Path(thisString).is_file())
#     if Path(thisString).is_file():
#         return str(Path.home()) + "\\AppData\\Roaming\\Spotify\\Spotify.exe"
#     else:
#         for subdir, dirs, files in os.walk("C:\\"):
#             for file in files:
#                 if "Spotify.exe" in file:
#                     # print(os.path.join(subdir,file))
#                     return os.path.join(subdir,file)


# def ChangeValue():
#     settings = getSettings()
#     # print(str(settings["alarms"]))
#     # print("{this}".format(this = settings["maxSystemVolume"]))
#     settings["maxSystemVolume"] = 10
#     setSettings(settings)


def StartSpotify(_playList):
    os.system(os.path.join(dir,"Spotify_RunThis.vbs") + " " + _playList)

"""
def processInput(thisInput):
    # print(i)
    settings = getSettings()

    thisInput = thisInput.lower()

    if re.match("vol-*",thisInput) or re.match("vol",thisInput):
        vol = re.findall("\d+\.\d+",thisInput)
        # print(vol)
        if len(vol) > 0:
            # print(vol[0])
            settings["maxSystemVolume"] = vol[0]
            setSettings(settings)
        else:
            print( Back.RED + Fore.BLACK + Style.DIM + "***ERROR PLEASE USE THE CORRECT FORMAT***")
    if re.match("false",thisInput) or re.match("off",thisInput)  or re.match("of",thisInput):
        settings["offTilNextDay"] = "false"
        settings["offDay"] = str(datetime.datetime.now().date()).replace("-","")
        setSettings(settings)
    if re.match("[0-9]",thisInput[:1]):
        i = int(thisInput[:1])
        os.system('cls')
        # print("Alarm{alarmNum}\ntime: {time}\nrepeat: {repeat}\nrepeatDays: {repeatDays}\nenable: {enable}".format(alarmNum = i,time=settings["alarms"][i]["time"], repeat=settings["alarms"][i]["repeat"],repeatDays=settings["alarms"][i]["repeatDays"],enable = settings["alarms"][i]["enable"]))
        print("**ALARM # " + str(i) + "**")
        print("time: " + str(settings["alarms"][i]["time"]))
        print("repeat: " + str(settings["alarms"][i]["repeat"]))
        print("repeatDays: " + settings["alarms"][i]["repeatDays"])
        print("enable: " + str(settings["alarms"][i]["enable"]))




def EditMenu():
    settings = getSettings()
    os.system('cls')

    print(Back.BLACK + Fore.GREEN + Style.DIM  + "*****************")
    print("*** EDIT MENU ***")
    print("*****************")

    print(Style.RESET_ALL)

    print( Back.RED + Fore.BLACK + Style.DIM  + "***             WARNING            ***")
    print("*** ALARMS WON'T PLAY IN EDIT MENU ***")
    print("***             WARNING            ***")

    print(Style.RESET_ALL)

    template = Fore.GREEN + "{key}" + Fore.WHITE + " :: {desc}\n"

    print(template.format(key = "vol-#.#",desc = "Modify the Max Volume, between 0.0 and 1.0" ))
    print(template.format(key = "false or off",desc = "Turn off all alarms until the next day" ))
    print(template.format(key = "URI i.e.(spotify:user:spotify:playlist:37i9dQZF1DX0UrRvztWcAU)",desc = "Enter URI to change the spotify playlist" ))
    print(template.format(key = "n",desc = "Creates a new alarm" ))
    print(template.format(key = "d-#",desc = "Removes alarm, # is index number" ))
    print(template.format(key = "#-false",desc = "Disables alarm, # is index number" ))
    print(template.format(key = "#-true",desc = "Enables alarm, # is index number" ))
    print(template.format(key = "#-HHMM",desc = "Change alarm time, # is index number, HH is hours, MM is minutes" ))
    print(template.format(key = "#-SMTWRFS",desc = "Change alarm time, # is index number, SMTWRFS should be 0s and 1s" ))
    print(template.format(key = "x or nothing",desc = "Exit Edit Mode" ))

    print(Style.RESET_ALL)

    printTimes()

    thisInput = input("Enter Option:\n")
    processInput(thisInput)

    MainMenu()
"""

    # print("**************************************************")
    # print("{key}: {value} \n--Enter {edit} to Change it \n".format(key = "spotifyPath", value = settings["spotifyPath"], edit = "\"C:\\[Path to File]\Spotify.exe\"" ))
    # print("{key}: {value} \n--Enter {edit} to Change it \n".format(key = "maxSystemVolume", value = settings["maxSystemVolume"], edit = "vol #.##" ))
    # # print("{key}: {value} \n    Enter {edit} to Change it \n".format(key = "snoozeTime", value = settings["snoozeTime"], edit = "ST" ))
    # print("{key}: {value} \n--Enter {edit} to Change it \n".format(key = "offTilNextDay", value = settings["offTilNextDay"], edit = "'offTilNextDay' or 'OTND' or 'X' or ' '" ))
    # print("**************************************************")
    # print("here is a list of your alarms, enter number to change them")

    # i = 0
    # while i < len(settings["alarms"]):
    #     print("{index}: {time} | {repeatDays} | {enable}".format(
    #         index=i, time=settings["alarms"][i]["time"], repeatDays=settings["alarms"][i]["repeatDays"],enable = settings["alarms"][i]["enable"]
    #         ))
    #     # print(settings["alarms"][i])
    #     i+=1
    
    # print("\n")
    # processInput(input("Enter an option: \n"))





# def printSettings():
#     settings = getSettings()

#     print("**************************************************")
#     print("{key}: {value}".format(key = "maxSystemVolume", value = settings["maxSystemVolume"]))
#     print("{key}: {value}".format(key = "playListURI", value = settings["playListURI"]))
#     print("{key}: {value}".format(key = "offTilNextDay", value = settings["offTilNextDay"]))
#     print("**************************************************")

#     now = datetime.datetime.now()
#     i = 0
#     while i < len(settings["alarms"]):
#         print("{index}: {time} | {SMTWRFS} | {enable}".format(
#             index=i, time=settings["alarms"][i]["time"], SMTWRFS=settings["alarms"][i]["SMTWRFS"],enable = settings["alarms"][i]["enable"]
#             ))
#         i+=1
#     print("\n")


def printTimes():
    settings = getSettings()
    color = ""

    print("#, time, SMTWRFS, enable")
    print("*******************************")

    # now = datetime.datetime.now()
    i = 0
    while i < len(settings["alarms"]):

        if settings["alarms"][i]["enable"] == False :
            color = Fore.RED
        else:
            color = Fore.RESET

        print(color + "{index} | {time} | {SMTWRFS} | {enable}".format(
            index=i, time=settings["alarms"][i]["time"], SMTWRFS=settings["alarms"][i]["SMTWRFS"],enable = settings["alarms"][i]["enable"]
            ))
        i+=1
    print(Style.RESET_ALL)
    # print("\n")


def getTime(withColon = False):
    if withColon:
        return str(datetime.datetime.now().time())[:5]
    else:
        return int(str(datetime.datetime.now().time())[:5].replace(":",""))

def getDay():
    return int(str(datetime.datetime.now().date())[:10].replace("-",""))


def SMTWRFS(schedule):
    # print(schedule)
    dayOfTheWeek = datetime.date.isoweekday(datetime.datetime.now().date()) 
    # dayOfTheWeek += 1
    dayNumber = dayOfTheWeek % 7
    # print(dayNumber)
    char = schedule[dayNumber]
    # print(char)
    if char == "1":
        return True
    else:
        return False


def playAlarms():
    settings = getSettings()

    t = getTime()
    # print(t)

    d = getDay()
    # print(d)



    i = 0
    while i < len(settings["alarms"]):

        # print(SMTWRFS(settings["alarms"][i]["SMTWRFS"]) )

        #enabled and has not played today
        if settings["alarms"][i]["enable"] == True and SMTWRFS(settings["alarms"][i]["SMTWRFS"]) and settings["alarms"][i]["exeDay"] < d:
            if settings["alarms"][i]["time"] <= t :
                StartSpotify(settings["PlayList"])
                settings["alarms"][i]["exeDay"] = d
                setSettings(settings)
                setSystemVolume(settings["maxSystemVolume"])
                print("*** playing Alarm" + str(i) + " ***")
        i+=1

    # setSystemVolume(0.0)
    # i = 0 
    # currentVol = 0.0

    # # print(currentVol)
    # # print(settings["maxSystemVolume"])

    # setSystemVolume(0.0)
    # while i < 100:
    #     i += 1
    #     currentVol = (settings["maxSystemVolume"]/100) * i
    #     setSystemVolume(currentVol)
    #     time.sleep(0.5)



def MainMenu():
    try:
        while True:
            os.system('cls')
            print( Back.RED + Fore.BLACK + Style.DIM + "***Press Ctrl+C to edit***")
            print(Back.WHITE + Fore.BLACK + Style.DIM + "CurrentTime: " + str(getTime(True)) + " ")
            print(Style.RESET_ALL)
            printTimes()
            print(Style.RESET_ALL)
            playAlarms()
            time.sleep(5)
# print(datetime.datetime.now().time())
    except KeyboardInterrupt:
        i = 1
        os.startfile(settingsPath)
        MainMenu()

# createSettings()
MainMenu()


# print(datetime.date.isoweekday(datetime.datetime.now().date()))
# Dnum = datetime.date.isoweekday(datetime.datetime.now().date()) + 1 % 7
# print(Dnum)

# print("1234567"[0-1])
# print("1234567"[3-1])


# print("1time"[:1])
# print("1time"[:-1])
# print("1time"[1:-1])

# do_print()

# print("22:33"[3:])

# # print(datetime.datetime.now().date())
# print(datetime.datetime.now().time())

# if time("22:00") > datetime.datetime.now().time():
#     print("1")
# else:
#     print("2")

# createSettings()
# getSettings()
# print(getSpotifyPath().replace("\\\\","\\"))
# print(str(settings))

# Clear Screen
# os.system('cls')


# setSystemVolume(0.10)
# # createSettings()
# StartSpotify()

