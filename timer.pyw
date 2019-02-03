
import os, json,datetime, re,time
from pathlib import Path

import alarmDataManager as ADM

#audio settings stuff
from ctypes import cast, POINTER
from comtypes import CLSCTX_ALL
from pycaw.pycaw import AudioUtilities, IAudioEndpointVolume


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



def getTime(withColon = False):
    if withColon:
        return str(datetime.datetime.now().time())[:5]
    else:
        return int(str(datetime.datetime.now().time())[:5].replace(":",""))

def getDay():
    return int(str(datetime.datetime.now().date())[:10].replace("-",""))


def getDayOfWeek():
    dayNum = datetime.date.isoweekday(datetime.datetime.now().date())

    if dayNum == 0:
        return "M"
    elif dayNum == 1:
        return "T"
    elif dayNum == 2:
        return "W"
    elif dayNum == 3:
        return "R"
    elif dayNum == 4:
        return "F"
    elif dayNum == 5:
        return "Sa"
    # elif dayNum == 6:
    else:
        return "Su"
    
    
def diffSeconds():
    return(60 - datetime.datetime.now().second + 1)

# diffSeconds()
# exit()

# print(datetime.date.weekday(datetime.datetime.now().date()))
# exit()

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


def playAlarms():
    settings = ADM.getSettings()
    # print(settings)

    t = getTime()
    # print(t)

    d = getDay()
    # print(d)

    if settings["disabledUntilAfter"] == 0:
        print("*")
    elif settings["disabledUntilAfter"] < d:
        return ""
    else:
        settings["disabledUntilAfter"] = 0
        ADM.setSettings(settings)

    i = 0
    while i < len(settings["alarms"]):

        if settings["alarms"][i]["enable"] == True and settings["alarms"][i][getDayOfWeek()] == True:

            alarmTime = (int)(settings["alarms"][i]["time"].replace(":",""))
            # print(alarmTime)

            if alarmTime == t:

                if re.match("[A-Z]:.*",settings["alarms"][i]["file"]):
                    os.startfile(settings["alarms"][i]["file"])
                else:
                    os.startfile(os.path.join(dir,settings["alarms"][i]["file"]))

                settings["alarms"][i]["exeDay"] = d
                ADM.setSettings(settings)
                setSystemVolume(settings["alarms"][i]["volume"])
                print("*** playing Alarm" + str(i) + " ***")
        i+=1


while True:
    # print(datetime.datetime.now().time())
    # print(diffSeconds())
    playAlarms()
    time.sleep(diffSeconds())
    # time.sleep(1)