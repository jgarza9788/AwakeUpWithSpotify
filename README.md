# pyAlarm.py 
An alarm clock (written in Python, Json) that plays mp3 files.

## Donate
[Buy me a Beer 🍺](https://www.paypal.me/JGarza9788/)

## Requires
* Python  
* pycaw (python Module)  
    * pycaw is a module for adjusting the volume in windows
        * this is why it will need adjusting before working on macOS or Linux
* portalocker (python Module)  
* PySide2 (python Module)  


## Settings
settings are in a json file.  
Obviously, you'll want to adjust the file to your liking. 

**enable**  
true or false

**file**  
the mp3 file to play  
but it can be any file you system can open

**volume**  
the volume the computer should be at

**time**  
time to play the alarm (military - no colon)

**Sa,M,T,W,R,F,Su**   
these are bools on whether or not the alarm should execute on those days.

**exeDay**  
the last day this alarm was executed  

```json
{
    "disabledUntilAfter": 0,
    "alarms": [
        {
            "enable": true,
            "file": "alarms\\Awaken.mp3",
            "volume": 0.12,
            "time": "09:00",
            "Su": false,
            "M": true,
            "T": true,
            "W": true,
            "R": true,
            "F": true,
            "Sa": false,
            "exeDay": 0
        }
    ]
}
```



## New Feature(s)
* In System Tray
* Disable Until Tomorrow


