import os,json,time,subprocess
from PySide2 import QtCore, QtGui, QtWidgets

from functools import partial

import alarmDataManager as ADM

dir = os.path.dirname(__file__)
settingsPath = os.path.join(dir,"settings.json").replace("\\","/")
settings = ""

# print(datetime.datetime.now().time())
# print(time.strptime("09:00", "%H:%M")  )
# thisTime = time.strptime("09:00", "%H:%M") 
# print(thisTime.tm_hour)
# print(thisTime.tm_min)
# exit()

enableStyle = ".QWidget {background-color: #F0F0F0;border-color:#6b6b6b;border-style:solid;border-width: 1px}"
disableStyle = ".QWidget {background-color: #a0a0a0;border-color:#6b6b6b;border-style:solid;border-width: 1px}"


class MainWindow(QtWidgets.QMainWindow):
    def __init__(self):
        super(MainWindow, self).__init__()

        settings = ADM.getSettings()
        print(settings)
        print(settings["alarms"])
        print(len(settings["alarms"]))
        print(settings["alarms"][0])

        self.createTrayIcon()
        
        self.setWindowTitle('pyAlarm')
        icon = QtGui.QIcon(os.path.join(dir,"images",'iconDark.png'))
        self.setWindowIcon(icon)
        
        appSettings = QtCore.QSettings("JGarza9788", "pyAlarm")
        size = appSettings.value("size", QtCore.QSize(800, 1200))
        self.resize(size)
        self.setMaximumWidth(800)
        self.setMinimumWidth(700)
        self.setMinimumHeight(600)
    
        self.AlarmWidget = QtWidgets.QListWidget(self)

        # item = QtWidgets.QListWidgetItem(self.AlarmWidget)
        # self.displayMessage = QtWidgets.QLabel(ADM.getTempDisable())
        # self.displayMessage.setStyleSheet(ADM.getStyle())
        # item.setSizeHint(self.displayMessage.sizeHint())
        # self.AlarmWidget.addItem(item)
        # self.AlarmWidget.setItemWidget(item,self.displayMessage)


        i = 0 
        # while i < 50:
        while i < len(settings["alarms"]):
            print(settings["alarms"][i])

            item = QtWidgets.QListWidgetItem(self.AlarmWidget)

            thisItem = self.createNewItem(i,settings["alarms"][i])

            item.setSizeHint(thisItem.sizeHint())
            self.AlarmWidget.addItem(item)
            self.AlarmWidget.setItemWidget(item,thisItem)
            i+=1

        self.setCentralWidget(self.AlarmWidget)

        self.createToolBars()

        # timer = os.path.join(dir,"timer.py")
        # proc = subprocess.Popen(['py', timer], shell=True)

    def createToolBars(self):
        self.thisToolbar = QtWidgets.QToolBar()
        # self.addToolBar(QtCore.Qt.BottomToolBarArea,self.thisToolbar)
        self.addToolBar(self.thisToolbar)
        self.thisToolbar.setFloatable(False) 
        # self.thisToolbar.setMovable (False)

        # toolBarFunc = partial(self.thisToolbar)
        self.thisToolbar.visibilityChanged.connect(self.unhideToolBar)

        newAlarmIcon = os.path.join(dir,"images","alarm-plus.png")
        self.newAct = QtWidgets.QAction(QtGui.QIcon(newAlarmIcon), "&New Alarm - Ctrl+N",
                self, shortcut=QtGui.QKeySequence.New,
                statusTip="Create a new Alarm", triggered=self.newAlarm)
        self.thisToolbar.addAction(self.newAct)
        
        self.thisToolbar.addSeparator()

        showCodeIcon = os.path.join(dir,"images","json.png")
        self.actOpenCode = QtWidgets.QAction(QtGui.QIcon(showCodeIcon), "&Show Settings Code",
                self, statusTip="Show Settings Code", triggered=self.openSettingsCode)
        self.thisToolbar.addAction(self.actOpenCode)

        self.thisToolbar.addSeparator()
        self.thisToolbar.addSeparator()
        self.thisToolbar.addSeparator()

        disableTodayIcon = os.path.join(dir,"images","calendar-today.png")
        self.actDisableToday = QtWidgets.QAction(QtGui.QIcon(disableTodayIcon), "&Disable Today",
                self, statusTip="disable alarms for the rest of the day", triggered=self.disableToday)
        self.thisToolbar.addAction(self.actDisableToday)

        disableTomorrowIcon = os.path.join(dir,"images","calendar.png")
        self.actDisableTomorrow = QtWidgets.QAction(QtGui.QIcon(disableTomorrowIcon), "&Disable Tomorrow",
                self, statusTip="disable alarms until after tomorrow", triggered=self.disableTomorrow)
        self.thisToolbar.addAction(self.actDisableTomorrow)

        undisableIcon = os.path.join(dir,"images","calendar-check.png")
        self.actUndisable = QtWidgets.QAction(QtGui.QIcon(undisableIcon), "&Undisable Today/Tomorrow",
                self, statusTip="undo Disable Today/Tormorrow", triggered=self.undisableAlarms)
        self.thisToolbar.addAction(self.actUndisable)

        self.thisToolbar.addSeparator()
        self.thisToolbar.addSeparator()
        self.thisToolbar.addSeparator()

        self.message = QtWidgets.QLabel(ADM.getTempDisable())
        self.message.setStyleSheet(ADM.getStyle())
        self.thisToolbar.addWidget(self.message)

    def unhideToolBar(self):
        self.thisToolbar.show()
        # self.createToolBars()

    def newAlarm(self):
        print("+Alarm")
        settings = ADM.getSettings()
        ADM.newAlarm(settings)
        self.refresh()

    # def createAddNewAlarm(self):
    #     self.NewAlarm = QtWidgets.QPushButton("+Alarm",self)
    #     return self.NewAlarm
    
    def createNewItem(self, i,alarmData):
        self.nItem = QtWidgets.QWidget()
        self.nItem.index = i

        

        layout = QtWidgets.QGridLayout()
        layout.setColumnStretch(0,0)
        layout.setColumnStretch(1,1)
        layout.setColumnStretch(2,1)
        layout.setColumnStretch(3,1)
        layout.setColumnStretch(4,1)
        layout.setColumnStretch(5,1)
        layout.setColumnStretch(6,1)
        layout.setColumnStretch(7,1)
        layout.setColumnStretch(8,1)
        layout.setColumnStretch(9,1)


        # self.nItem.setStyleSheet("QWidget {color:#333333;background-color: #a0a0a0}")
        # self.nItem.setStyleSheet("QPushButton {}")

        self.enable =  QtWidgets.QCheckBox("Enable",self)
        
        # if ADM.getDisabledUntilAfter() != 0:
        #     self.enable.setCheckState(QtCore.Qt.Unchecked)
        #     self.nItem.setStyleSheet(disableStyle)
        #     self.statusBar().showMessage(ADM.getTempDisable())
        #     self.statusBar().setStyleSheet(ADM.getStatusStyle())
        if alarmData["enable"] == True:
            self.enable.setCheckState(QtCore.Qt.Checked)
            self.nItem.setStyleSheet(enableStyle)
        else:
            self.enable.setCheckState(QtCore.Qt.Unchecked)
            self.nItem.setStyleSheet(disableStyle)
        self.enable.index = i
        enableFunc = partial(self.enableAlarm,self.enable,self.nItem)
        self.enable.stateChanged.connect(enableFunc)
        layout.addWidget(self.enable,0,0)

        

        self.delete = QtWidgets.QPushButton("X",self)
        # self.delete.setStyleSheet("QPushButton {background-color: #ffffff}")
        self.delete.index = i
        self.delete.cnt = 0
        self.delete.setMaximumSize (48,48)
        # self.delete.resize(QtCore.QSize(22,22))
        deleteFunc = partial(self.deleteAlarm,self.delete)
        self.delete.clicked.connect(deleteFunc)
        layout.addWidget(self.delete,0,9,1,1)

        frameStyle = QtWidgets.QFrame.Sunken | QtWidgets.QFrame.Panel
        self.openFileNameLabel = QtWidgets.QLabel(alarmData["file"])
        self.openFileNameLabel.index = i
        self.openFileNameLabel.setFrameStyle(frameStyle)
        self.openFileNameButton = QtWidgets.QPushButton('File:') #"QFileDialog.get&OpenFileName()")
        openFileNameFunct = partial(self.setOpenFileName,self.openFileNameLabel)
        self.openFileNameButton.clicked.connect(openFileNameFunct)
        layout.addWidget(self.openFileNameButton,1,0)
        layout.addWidget(self.openFileNameLabel,1,1,1,9)

        self.volumneLabel = QtWidgets.QLabel("Volume (" + str((int)(alarmData["volume"] * 100)) + ")")
        self.volumne = QtWidgets.QSlider(QtCore.Qt.Horizontal,self)
        self.volumne.setMaximum(20)
        self.volumne.setMinimum(1)
        self.volumne.setValue(alarmData["volume"] * 100)
        self.volumne.index = i
        valumeFunc =  partial(self.volumeChange,self.volumneLabel,self.volumne)
        self.volumne.valueChanged.connect(valumeFunc)
        layout.addWidget(self.volumneLabel, 2, 0)
        layout.addWidget(self.volumne, 2, 1,1,9)

        self.TimeLable = QtWidgets.QLabel("Time")
        self.Time = QtWidgets.QTimeEdit()
        self.Time.index = i
        self.Time.setDisplayFormat("HH:mm")
        # print(str(alarmData["time"])[2:])
        # print(str(alarmData["time"])[:2])
        aTime = time.strptime(alarmData["time"],"%H:%M")
        bTime = QtCore.QTime(aTime.tm_hour,aTime.tm_min)
        self.Time.setTime(bTime)
        timeFunc = partial(self.timeChange,self.Time)
        self.Time.timeChanged.connect(timeFunc)
        layout.addWidget(self.TimeLable, 3, 0)
        layout.addWidget(self.Time, 3, 1,1,2)



        # self.DaysLabel = QtWidgets.QLabel("Repeat Days")

        self.Su = QtWidgets.QPushButton("S",self)
        self.Su.index = i
        self.Su.day = "Su"
        self.Su.value = alarmData["Su"] 
        self.Su.setMaximumSize (48,48)
        if alarmData["Su"] == True:
            self.Su.setStyleSheet("QPushButton {background:#E5F1FB;border-color:#007AD9;border-style:solid;border-width: 1px}")
        else:
            self.Su.setStyleSheet("QPushButton {background:#7f7f7f;border-color:#000000;border-style:solid;border-width: 1px}")
        dayFunc = partial(self.checkDay,self.Su)
        self.Su.clicked.connect(dayFunc)

        # self.Su = QtWidgets.QCheckBox("S",self)
        # if alarmData["Su"] == True:
        #     self.Su.setCheckState(QtCore.Qt.Checked)
        # self.Su.index = i
        # self.Su.day = "Su"
        # dayFunc = partial(self.checkDay,self.Su)
        # self.Su.stateChanged.connect(dayFunc)

        self.M = QtWidgets.QPushButton("M",self)
        self.M.index = i
        self.M.day = "M"
        self.M.value = alarmData["M"] 
        self.M.setMaximumSize (48,48)
        if alarmData["M"] == True:
            self.M.setStyleSheet("QPushButton {background:#E5F1FB;border-color:#007AD9;border-style:solid;border-width: 1px}")
        else:
            self.M.setStyleSheet("QPushButton {background:#7f7f7f;border-color:#000000;border-style:solid;border-width: 1px}")
        dayFunc = partial(self.checkDay,self.M)
        self.M.clicked.connect(dayFunc)

        self.T = QtWidgets.QPushButton("T",self)
        self.T.index = i
        self.T.day = "T"
        self.T.value = alarmData["T"] 
        self.T.setMaximumSize (48,48)
        if alarmData["T"] == True:
            self.T.setStyleSheet("QPushButton {background:#E5F1FB;border-color:#007AD9;border-style:solid;border-width: 1px}")
        else:
            self.T.setStyleSheet("QPushButton {background:#7f7f7f;border-color:#000000;border-style:solid;border-width: 1px}")
        dayFunc = partial(self.checkDay,self.T)
        self.T.clicked.connect(dayFunc)

        self.W = QtWidgets.QPushButton("W",self)
        self.W.index = i
        self.W.day = "W"
        self.W.value = alarmData["W"] 
        self.W.setMaximumSize (48,48)
        if alarmData["W"] == True:
            self.W.setStyleSheet("QPushButton {background:#E5F1FB;border-color:#007AD9;border-style:solid;border-width: 1px}")
        else:
            self.W.setStyleSheet("QPushButton {background:#7f7f7f;border-color:#000000;border-style:solid;border-width: 1px}")
        dayFunc = partial(self.checkDay,self.W)
        self.W.clicked.connect(dayFunc)

        self.R = QtWidgets.QPushButton("R",self)
        self.R.index = i
        self.R.day = "R"
        self.R.value = alarmData["R"] 
        self.R.setMaximumSize (48,48)
        if alarmData["R"] == True:
            self.R.setStyleSheet("QPushButton {background:#E5F1FB;border-color:#007AD9;border-style:solid;border-width: 1px}")
        else:
            self.R.setStyleSheet("QPushButton {background:#7f7f7f;border-color:#000000;border-style:solid;border-width: 1px}")
        dayFunc = partial(self.checkDay,self.R)
        self.R.clicked.connect(dayFunc)

        self.F = QtWidgets.QPushButton("F",self)
        self.F.index = i
        self.F.day = "F"
        self.F.value = alarmData["F"] 
        self.F.setMaximumSize (48,48)
        if alarmData["F"] == True:
            self.F.setStyleSheet("QPushButton {background:#E5F1FB;border-color:#007AD9;border-style:solid;border-width: 1px}")
        else:
            self.F.setStyleSheet("QPushButton {background:#7f7f7f;border-color:#000000;border-style:solid;border-width: 1px}")
        dayFunc = partial(self.checkDay,self.F)
        self.F.clicked.connect(dayFunc)

        self.Sa = QtWidgets.QPushButton("S",self)
        self.Sa.index = i
        self.Sa.day = "Sa"
        self.Sa.value = alarmData["Sa"] 
        self.Sa.setMaximumSize (48,48)
        if alarmData["Sa"] == True:
            self.Sa.setStyleSheet("QPushButton {background:#E5F1FB;border-color:#007AD9;border-style:solid;border-width: 1px}")
        else:
            self.Sa.setStyleSheet("QPushButton {background:#7f7f7f;border-color:#000000;border-style:solid;border-width: 1px}")
        dayFunc = partial(self.checkDay,self.Sa)
        self.Sa.clicked.connect(dayFunc)

        # layout.addWidget(self.DaysLabel,4,0)
        layout.addWidget(self.Su,3,3)
        layout.addWidget(self.M,3,4)
        layout.addWidget(self.T,3,5)
        layout.addWidget(self.W,3,6)
        layout.addWidget(self.R,3,7)
        layout.addWidget(self.F,3,8)
        layout.addWidget(self.Sa,3,9)

        # self.button = QtWidgets.QPushButton(str(i))
        # self.button.clicked.connect(self.refresh)
        # layout.addWidget(self.button,i,0)       

        self.nItem.setLayout(layout)
        return self.nItem


    # def findDeleteButton(self,i):
    #     index = 0
    #     for child in self.AlarmWidget.findChildren(QtWidgets.QWidget):
    #         print(child)
    #         print(child.index)
    #         index+=1

    def checkDay(self,dayBox):

        if dayBox.value == True:
            dayBox.value = False
            dayBox.setStyleSheet("QPushButton {background:#7f7f7f;border-color:#000000;border-style:solid;border-width: 1px}")
        else:
            dayBox.value = True
            dayBox.setStyleSheet("QPushButton {background:#E5F1FB;border-color:#007AD9;border-style:solid;border-width: 1px}")

        settings = ADM.getSettings()
        settings["alarms"][dayBox.index][dayBox.day] = dayBox.value
        ADM.setSettings(settings)

    def timeChange(self,time,value):
        print(self)
        print(time)
        print(value)
        print(value.hour())
        print(value.minute())
        h = ("00" + str(value.hour()))[-2:]
        m = ("00" + str(value.minute()))[-2:]
        t = h + ":" + m
        print(t)
        settings = ADM.getSettings()
        settings["alarms"][time.index]["time"] = t
        ADM.setSettings(settings)
        # self.refresh()
        
        # settings["alarms"][time.index][time] = 


    def volumeChange(self,label,volume,value):
        print(volume)
        print(volume.index)
        print(value)
        settings = ADM.getSettings()
        settings["alarms"][volume.index]["volume"] = value/100
        label.setText("Volume (" + str(value) + ")")
        print(settings["alarms"][volume.index]["volume"])
        ADM.setSettings(settings)
        # self.refresh()

    def enableAlarm(self,thisCheckBox,nItem,state):
        print(state) # 2 == yes, 0 == no
        print(thisCheckBox.index)
        print("*")

        E = False
        # nItem.setStyleSheet("QWidget {color:#333333;background-color: #a0a0a0}")
        # nItem.setStyleSheet("QWidget {background-color: #a0a0a0}")
        nItem.setStyleSheet(disableStyle)
        if state == 2:
            E = True
            # nItem.setStyleSheet("")
            nItem.setStyleSheet(enableStyle)
            # nItem.setStyleSheet("QWidget {background-color: #ffffff}")
        
        print(E)
        settings = ADM.getSettings()
        settings["alarms"][thisCheckBox.index]["enable"] = E
        print(settings["alarms"][thisCheckBox.index]["enable"])

        ADM.setSettings(settings)
        # self.refresh()

    def deleteAlarm(self,thisButton):
        if thisButton.cnt == 0:
            thisButton.setText("?")
            thisButton.setStyleSheet("background-color:#ff0000;")
            thisButton.cnt += 1
        else:
            print(str(thisButton.index))
            print(str(thisButton.cnt))
            print("this was deleted")

            settings = ADM.getSettings()
            settings["alarms"].pop(thisButton.index)
            print(settings["alarms"])
            ADM.setSettings(settings)
            self.refresh()


        # print(this)
        # findDeleteButton(self.de)
        # if self.delete.cnt == 0:
        #     self.delete.setText("Sure?")
        #     self.delete.setStyleSheet("background-color:#ff0000;")
        #     self.delete.cnt += 1
        # else:
        #     self.refresh()

    def refresh(self):
        self.AlarmWidget.deleteLater()
        self.AlarmWidget = QtWidgets.QListWidget(self)

        settings = ADM.getSettings()

        i = 0 
        # while i < 50:
        while i < len(settings["alarms"]):
            print(settings["alarms"][i])

            item = QtWidgets.QListWidgetItem(self.AlarmWidget)

            thisItem = self.createNewItem(i,settings["alarms"][i])

            item.setSizeHint(thisItem.sizeHint())
            self.AlarmWidget.addItem(item)
            self.AlarmWidget.setItemWidget(item,thisItem)
            i+=1

        self.setCentralWidget(self.AlarmWidget)

    def setOpenFileName(self, thisLabel):
        options = QtWidgets.QFileDialog.Options()
        settings = ADM.getSettings()

        # if not self.native.isChecked():
        #     options |= QtWidgets.QFileDialog.DontUseNativeDialog
        fileName, filtr = QtWidgets.QFileDialog.getOpenFileName(self,
                "QFileDialog.getOpenFileName()",os.path.join(dir,"alarms"),
                # self.openFileNameLabel.text(),
                "All Files (*);;Text Files (*.txt)", "", options)
        if fileName:
            thisLabel.setText(fileName)
            settings["alarms"][thisLabel.index]["file"] = fileName
            ADM.setSettings(settings)
            # self.openFileNameLabel.setText(fileName)
            # print(self.openFileNameLabel.index)
            # print(self.openFileNameLabel.name)

            # items = self.openFileNameButton.get
            # for item in items:
            #     print "row number of found item =",self.listWidgetName.row(item)
            #     print "text of found item =",item.text() 

    def updateMessage(self):
        self.displayMessage.setText(ADM.getTempDisable())
        self.displayMessage.setStyleSheet(ADM.getStyle())


    def createTrayIcon(self):
        self.trayIconMenu = QtWidgets.QMenu(self)
        

        self.actOpen = QtWidgets.QAction("Open")
        self.actOpen.triggered.connect(self.OpenMainWindow)
        self.trayIconMenu.addAction(self.actOpen)

        self.trayIconMenu.addSeparator()

        self.actToday = QtWidgets.QAction("Disable Today")
        self.actToday.triggered.connect(self.disableToday)
        self.trayIconMenu.addAction(self.actToday)

        self.actTorrrmow = QtWidgets.QAction("Disable Tomorrow")
        self.actTorrrmow.triggered.connect(self.disableTomorrow)
        self.trayIconMenu.addAction(self.actTorrrmow)

        self.actUndisableAlarms = QtWidgets.QAction("Undo Disable")
        self.actUndisableAlarms.triggered.connect(self.undisableAlarms)
        self.trayIconMenu.addAction(self.actUndisableAlarms)

        self.trayIconMenu.addSeparator()

        self.actQuit = QtWidgets.QAction("Quit")
        self.actQuit.triggered.connect(self.QuitProgram)
        self.trayIconMenu.addAction(self.actQuit)

        # self.trayIconMenu.addAction(self.QuitProgram)
        # self.trayIconMenu.addAction(self.maximizeAction)
        # self.trayIconMenu.addAction(self.restoreAction)
        # self.trayIconMenu.addSeparator()
        # self.trayIconMenu.addAction(self.quitAction)

        self.trayIcon = QtWidgets.QSystemTrayIcon(self)
        icon =  QtGui.QIcon(os.path.join(dir,"images",'iconWhite.png'))
        self.trayIcon.setIcon(icon)
        self.trayIcon.setVisible(True)
        self.trayIcon.setContextMenu(self.trayIconMenu)

        self.trayIcon.activated.connect(self.OpenMainWindow)
        # self.trayIcon.show()

    def QuitProgram(self):
        proc.terminate()
        sys.exit()

    def OpenMainWindow(self):
        mainWin.show()

    def openSettingsCode(self):
        os.startfile(settingsPath)

    def disableToday(self):
        ADM.disableToday()
        self.message.setText(ADM.getTempDisable())
        self.message.setStyleSheet(ADM.getStyle())
        # self.statusBar().showMessage(ADM.getTempDisable())
        # self.statusBar().setStyleSheet(ADM.getStatusStyle())

    def disableTomorrow(self):
        ADM.disableTomorrow()
        self.message.setText(ADM.getTempDisable())
        self.message.setStyleSheet(ADM.getStyle())
        # self.statusBar().showMessage(ADM.getTempDisable())
        # self.statusBar().setStyleSheet(ADM.getStatusStyle())

    def undisableAlarms(self):
        ADM.undisableAlarms()
        self.message.setText(ADM.getTempDisable())
        self.message.setStyleSheet(ADM.getStyle())
        # self.statusBar().showMessage(ADM.getTempDisable())
        # self.statusBar().setStyleSheet(ADM.getStatusStyle())

if __name__ == '__main__':

    import sys

    app = QtWidgets.QApplication(sys.argv)
    app.setQuitOnLastWindowClosed(False)

    mainWin = MainWindow()
    mainWin.show()

    timer = os.path.join(dir,"timer.pyw")
    proc = subprocess.Popen(['py', timer], shell=True)

    sys.exit(app.exec_())
