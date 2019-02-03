
import os, json,datetime, re,time
from pathlib import Path

#audio settings stuff
from ctypes import cast, POINTER
from comtypes import CLSCTX_ALL
from pycaw.pycaw import AudioUtilities, IAudioEndpointVolume

dir = os.path.dirname(__file__)
#[:1].upper() + os.path.dirname(__file__)[1:]
# dir = dir.replace("\\","/")
# print("C:\somethign"[1:])
# print(dir)
# exit()

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

def OpenFile(playButton):
    print(playButton)
    print(playButton.file)
    print(playButton.volume)
    openFile2(playButton.file,playButton.volume)

def openFile2(filePath, volume):
    if re.match("[A-Za-z]:.*",filePath):
        os.startfile(filePath)
    else:
        os.startfile(os.path.join(dir,filePath))
    setSystemVolume(volume)


if __name__ == "__main__":
    # openFile2(r"C:\Users\JGarza\GitHub\pyAlarm\alarms\Bounce.mp3", 0.5)
    # openFile2(r"[dir]alarms\Awake.mp3", 0.5)
    # print(dir)
    # this = os.path.join(dir,"alarms\\Awaken.mp3")
    # print(this)
    # print(os.path.isfile(this))
    openFile2("alarms\\Awaken.mp3",0.1)