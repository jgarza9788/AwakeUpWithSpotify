
import os, json,datetime, re,time
from pathlib import Path
import portalocker

#audio settings stuff
from ctypes import cast, POINTER
from comtypes import CLSCTX_ALL
from pycaw.pycaw import AudioUtilities, IAudioEndpointVolume

dir = os.path.dirname(__file__)
# print(dir)
settingsPath = os.path.join(dir,"alarmSettings.json").replace("\\","/")
settings = ""

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
            if settings["alarms"][i]["time"] <= t and settings["alarms"][i]["time"] + 10 >= t:
                # StartSpotify("\"" + settings["PlayList"] + "\"")
                
                if re.match("[A-Z]:.*",settings["alarms"][i]["file"]):
                    os.startfile(settings["alarms"][i]["file"])
                else:
                    os.startfile(os.path.join(dir,settings["alarms"][i]["file"]))

                # os.startfile(os.path.join(dir,settings["alarms"][i]["file"]))
                settings["alarms"][i]["exeDay"] = d
                setSettings(settings)
                setSystemVolume(settings["alarms"][i]["volume"])
                print("*** playing Alarm" + str(i) + " ***")
        i+=1

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
            time.sleep(30)


MainMenu()