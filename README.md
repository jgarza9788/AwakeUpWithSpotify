# pyAlarm.py 
An alarm clock (written in Python, Json) that plays mp3 files.

## Donate
[Buy me a Beer 🍺](https://www.paypal.me/JGarza9788/)

## Requires
* Python  
* pycaw (python Module)  
~~* colorama (python Module)~~

## Settings
settings are in a json file.  
Obviously, you'll want to adjust the file to your liking. 

**enable**  
true or false

**file**  
the mp3 file to play

**volume**  
the volume the computer should be at

**time**  
time to play the alarm (military - no colon)

**SMTWRFS**  
days the alarm should ring.   
0 = no, 1 = yes.  
i.e. 0111110 = weekdays  
1000001 = weekends  
0101010 = monday, wednesday, friday  

**exeDay**  
the last day this alarm was executed  

```json
{
    "alarms": [
        {
            "enable": true,
            "file": "D:\\Music\\8Bit Universe\\Unknown Album\\Safety Dance (8Bit Cover).mp3",
            "volume": 0.01,
            "time": 400,
            "SMTWRFS": "0111110",
            "exeDay": 20181220
        },
        {
            "enable": true,
            "file": "D:\\Music\\8Bit Universe\\Unknown Album\\Safety Dance (8Bit Cover).mp3",
            "volume": 0.02,
            "time": 415,
            "SMTWRFS": "0111110",
            "exeDay": 20181220
        },
        {
            "enable": true,
            "file": "D:\\Music\\8Bit Universe\\Unknown Album\\Safety Dance (8Bit Cover).mp3",
            "volume": 0.05,
            "time": 430,
            "SMTWRFS": "0111110",
            "exeDay": 20181220
        }
    ]
}
```



## New Feature(s)
* In System Tray
* Disable Until Tomorrow

![Gif](https://i.imgur.com/mFBODIy.gif)
