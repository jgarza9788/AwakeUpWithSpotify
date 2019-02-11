"""
this is a subprocess 
"""

#import libraries
import os, json,datetime, re,time
from pathlib import Path

# this library is used to control data
import alarmDataManager as ADM

#audio settings stuff
from ctypes import cast, POINTER
from comtypes import CLSCTX_ALL
from pycaw.pycaw import AudioUtilities, IAudioEndpointVolume

# sets the volume level
def setSystemVolume(level):
    devices = AudioUtilities.GetSpeakers()
    interface = devices.Activate(
        IAudioEndpointVolume._iid_, CLSCTX_ALL, None)
    volume = cast(interface, POINTER(IAudioEndpointVolume))
    volume.SetMasterVolumeLevelScalar(level,None)

#gets the current volume level
def getSystemVolume():
    devices = AudioUtilities.GetSpeakers()
    interface = devices.Activate(
        IAudioEndpointVolume._iid_, CLSCTX_ALL, None)
    volume = cast(interface, POINTER(IAudioEndpointVolume))
    return round(volume.GetMasterVolumeLevelScalar(),4)

# gets the current time (int or string)
def getTime(withColon = False):
    if withColon:
        return str(datetime.datetime.now().time())[:5]
    else:
        return int(str(datetime.datetime.now().time())[:5].replace(":",""))

# gets the current day in YYYYMMDD format
def getDay():
    return int(str(datetime.datetime.now().date())[:10].replace("-",""))

# gets day of the week (Su,M,T,W,R,F,Sa)
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
    else:
        return "Su"
    
# gets the number of seconds until the next minute
def diffSeconds():
    return(60 - datetime.datetime.now().second + 1)

# play Alarms
def playAlarms():
    #get all the settings
    settings = ADM.getSettings()

    t = getTime()
    # print(t)

    d = getDay()
    # print(d)

    # do nothing/print if disabledUntilAfter is 0
    if settings["disabledUntilAfter"] == 0:
        print("*")
    # don't play any alarm if disabledUntilAfter is greater than today
    elif settings["disabledUntilAfter"] >= d:
        return ""
    # else reset disabledUntilAfter to 0
    else:
        settings["disabledUntilAfter"] = 0
        ADM.setSettings(settings)

    #loop through each alarm 
    i = 0
    while i < len(settings["alarms"]):

        # make sure it's enabled and should play today
        if settings["alarms"][i]["enable"] == True and settings["alarms"][i][getDayOfWeek()] == True:

            #get time as an int
            alarmTime = (int)(settings["alarms"][i]["time"].replace(":",""))

            # if alarmTime is this time ...play
            if alarmTime == t:

                if re.match("[A-Z]:.*",settings["alarms"][i]["file"]):
                    os.startfile(settings["alarms"][i]["file"])
                else:
                    os.startfile(os.path.join(dir,settings["alarms"][i]["file"]))

                setSystemVolume(settings["alarms"][i]["volume"])
                print("*** playing Alarm" + str(i) + " ***")
        i+=1

#used for texting
if __name__ == "__main__":    
    while True:
        playAlarms()
        time.sleep(diffSeconds())
        # time.sleep(1)