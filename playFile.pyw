"""
This files is used to play/open files and set the correct volume
"""

#import libraries
import os, json,datetime, re,time
from pathlib import Path

#audio settings stuff
from ctypes import cast, POINTER
from comtypes import CLSCTX_ALL
from pycaw.pycaw import AudioUtilities, IAudioEndpointVolume

#this directory
dir = os.path.dirname(__file__)

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

# opens a file
def OpenFile(playButton):
    print(playButton)
    print(playButton.file)
    print(playButton.volume)
    openFile2(playButton.file,playButton.volume)

#opens a file
def openFile2(filePath, volume):
    if re.match("[A-Za-z]:.*",filePath):
        os.startfile(filePath)
    else:
        os.startfile(os.path.join(dir,filePath))
    setSystemVolume(volume)

#used for testing
if __name__ == "__main__":
    openFile2("alarms\\Awaken.mp3",0.1)