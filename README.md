# pyAlarm.py 
An alarm clock (written in Python, Json) that plays mp3 files.

## Donate
[Buy me a Beer 🍺](https://www.paypal.me/JGarza9788/)

## Requires
* Python  
* pycaw (install python module with pip)  
    * pycaw is a module for adjusting the volume in windows
        * this is why it will need adjusting before working on macOS or Linux
* PySide2 (install python module with pip)  

## Settings
settings are in a json file.  
Obviously, you'll want to adjust the file to your liking. 

**disabledUntilAfter**
alarms will not play if before or on this date.

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


## UI

### Task Bar Icon
![Imgur](https://i.imgur.com/n6IbL2S.png)

### Main Window
![Imgur](https://i.imgur.com/SMeA5VU.png)

#### Tool Bar

**Add New Alarm**  
![Imgur](https://i.imgur.com/TA8lXOR.png)  

**Show Json Code/Settings**  
![Imgur](https://i.imgur.com/r31fpS6.png)

**disable alarms for the rest of the day**  
![Imgur](https://i.imgur.com/nKjXCj4.png)

**disable alarms for the rest of the day and tomorrow**  
![Imgur](https://i.imgur.com/0rPkzQ5.png)

**undo disable**
![Imgur](https://i.imgur.com/EOd9zOH.png)



