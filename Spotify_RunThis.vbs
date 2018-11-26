'objArgs is all objects that are dropped on this file
Set objArgs = Wscript.Arguments

'used for other things
Set objShell = WScript.CreateObject("WScript.Shell")

''messagebox Arguments
' For i = 0 to objArgs.count - 1
'     msgbox(objArgs(i))
'     Next

' msgbox(objArgs.count)

on error resume next

dim spotifyPath, URI

' maxVolume = objArgs(0)
spotifyPath = objArgs(0)
URI = objArgs(1)

If Err.Number <> 0 Then
    spotifyPath = "C:\Users\JGarza\AppData\Roaming\Spotify\Spotify.exe"
    URI = "spotify:user:spotify:playlist:37i9dQZF1DX0UrRvztWcAU"
    ' URL = "spotify:user:1257524228:playlist:7rub0Bqf5Ko2G81l6stMyQ"
End If

Function getSpotifyPID()
    Set Processes = GetObject("winmgmts:").InstancesOf("Win32_Process")
    For Each Process In Processes
        If StrComp(Process.Name, "Spotify.exe", vbTextCompare) = 0 Then
            getSpotifyPID = Process.ProcessId
            ' Activate the window using its process ID...
            ' With CreateObject("WScript.Shell")
            '     ' .AppActivate Process.ProcessId
            '     ' .SendKeys "%{F4}"
            ' End With

            ' We found our process. No more iteration required...
            Exit For
        End If
    Next
end Function 

sub quitWithPID(PID)
    strComputer = "."
    Set objWMIService = GetObject _
        ("winmgmts:\\" & strComputer & "\root\cimv2")
    Set colProcessList = objWMIService.ExecQuery _
        ("Select * from Win32_Process Where ProcessID = " & Cstr(PID))
    For Each objProcess in colProcessList
        objProcess.Terminate()
    Next
end sub

' sub MuteSystem()

' end sub

' sub increaseSystemVolume()
'     set oShell = CreateObject("WScript.Shell") 
'     oShell.run"%SystemRoot%\System32\SndVol.exe" 'Runs The Master Volume App.
'     WScript.Sleep 1000 'Waits For The Program To Open
'     ' oShell.SendKeys("{PGDN}") 'Turns Up The Volume 20, If It Is Muted Then It Will Unmute It
'     ' oShell.SendKeys("{PGDN}") 'Turns Up The Volume 20
'     ' oShell.SendKeys("{PGDN}") 'Turns Up The Volume 20
'     ' oShell.SendKeys("{PGDN}") 'Turns Up The Volume 20
'     ' oShell.SendKeys("{PGDN}") 'Turns Up The Volume 20

'     oShell.SendKeys("{END}") 'Turns The Volume 0

'     For i = 0 to maxVolume
'         objShell.SendKeys "{UP}"
'         ' WScript.sleep 1500  
'         NEXT

'     oShell.SendKeys"%{F4}"  ' ALT F4 To Exit The App.
' end sub


' increaseSystemVolume()
quitWithPID(getSpotifyPID())
' msgbox("-spotify is killed-")
WScript.sleep 1000
objShell.Run(spotifyPath)
' msgbox("-spotify is Alive-")
WScript.sleep 1000
objShell.AppActivate getSpotifyPID()
' WScript.sleep 1500
' msgbox("-go to playlist-")
WScript.sleep 5000
objShell.Run(URI)
' WScript.sleep 3000
' msgbox("-play-")
' objShell.SendKeys "^+{UP}"

WScript.sleep 1000
For i = 0 to 20
    objShell.SendKeys "^{DOWN}"
    WScript.sleep 10  
    NEXT

' WScript.sleep 3000
' objShell.SendKeys "^f"

WScript.sleep 10000
objShell.SendKeys "+{TAB}"
WScript.sleep 100
objShell.SendKeys "+{TAB}"
WScript.sleep 100
objShell.SendKeys "+{TAB}"
WScript.sleep 100
objShell.SendKeys "+{TAB}"
WScript.sleep 100
objShell.SendKeys "{ENTER}"

' objShell.SendKeys "^{RIGHT}"

WScript.sleep 5000
For i = 0 to 20
    objShell.SendKeys "^{UP}"
    WScript.sleep 2000  
    NEXT

