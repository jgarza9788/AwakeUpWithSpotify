import os, json,datetime, re,time,subprocess
from pathlib import Path

import portalocker


dir = os.path.dirname(__file__)

settingsPath = os.path.join(dir,"settings.json").replace("\\","/")
settings = ""


# print(str(datetime.datetime.now().time())[:5])
# exit()

def createSettings():
    data = {}
    data["disabledUntilAfter"] = 0
    data["alarms"] = []
    data["alarms"].append({
        "enable": True,
        "file": "alarms\\Awake.mp3",
        "volume": 0.05,
        "time": "09:00",
        "Su": False,
        "M": True,
        "T": True,
        "W": True,
        "R": True,
        "F": True,
        "Sa": False,
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
    print("data: \n" + str(data))
    # with open(settingsPath, 'w') as outfile:
    #     json.dump(data, outfile, indent=4)
    with portalocker.Lock(settingsPath,'w', timeout=60) as outfile:
        json.dump(data, outfile, indent=4)
        # flush and sync to filesystem
        outfile.flush()
        os.fsync(outfile.fileno())

def newAlarm(data):
    if len(data["alarms"]) > 0:
        data["alarms"].append({
            "enable": data["alarms"][len(data["alarms"])-1]["enable"],
            "file": data["alarms"][len(data["alarms"])-1]["file"],
            "volume": data["alarms"][len(data["alarms"])-1]["volume"],
            "time": data["alarms"][len(data["alarms"])-1]["time"],
            "Su": data["alarms"][len(data["alarms"])-1]["Su"],
            "M": data["alarms"][len(data["alarms"])-1]["M"],
            "T": data["alarms"][len(data["alarms"])-1]["T"],
            "W": data["alarms"][len(data["alarms"])-1]["W"],
            "R": data["alarms"][len(data["alarms"])-1]["R"],
            "F": data["alarms"][len(data["alarms"])-1]["F"],
            "Sa": data["alarms"][len(data["alarms"])-1]["Sa"],
            "exeDay": 0
        })
    else:
        data["alarms"].append({
            "enable": True,
            "file": "alarms\\Awake.mp3",
            "volume": 0.05,
            "time": "09:00",
            "Su": False,
            "M": True,
            "T": True,
            "W": True,
            "R": True,
            "F": True,
            "Sa": False,
            "exeDay": 0
        })
    setSettings(data)

def getDay():
    return int(str(datetime.datetime.now().date())[:10].replace("-",""))

def getTomorrow():
    tomorrow = datetime.datetime.now().date() + datetime.timedelta(days=1)
    return int(str(tomorrow)[:10].replace("-",""))

def intDayToString(intDay):
    return str(intDay)[:4] +"-" + str(intDay)[-4:-2] +"-"+str(intDay)[-2:]

# print(intDayToString(20190203))
# exit()

def disableToday():
    settings = getSettings()
    settings["disabledUntilAfter"] = getDay()
    setSettings(settings)

def disableTomorrow():
    settings = getSettings()
    settings["disabledUntilAfter"] = getTomorrow() 
    setSettings(settings)

def undisableAlarms():
    settings = getSettings()
    settings["disabledUntilAfter"] = 0
    setSettings(settings)

def getDisabledUntilAfter():
    settings = getSettings()
    return settings["disabledUntilAfter"] 

def getTempDisable():
    settings = getSettings()
    if settings["disabledUntilAfter"] == 0:
        return ""
    else:
        return "alarms are disabled until after " + intDayToString(settings["disabledUntilAfter"])


def getStyle():
    settings = getSettings()
    if settings["disabledUntilAfter"] == 0:
        return ""
    else:
        return "QLabel {padding-left:8px;padding:8px;background:rgba(255,0,0,255);color:black;font-weight:bold;}"
