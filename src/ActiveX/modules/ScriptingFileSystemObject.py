
import logging
log = logging.getLogger("Thug")

def OpenTextFile(self, sFilePathAndName, ForWriting = True, flag = True):
    log.MAEC.add_behavior_warn('[Script.FileSystemObject ActiveX] OpenTextFile("%s", "%s", "%s")' % (sFilePathAndName, ForWriting, flag))

def Write(self, sFileContents):
    log.MAEC.add_behavior_warn('[Script.FileSystemObject ActiveX] Write("%s")' % (sFileContents, ))

def Close(self):
    log.MAEC.add_behavior_warn('[Script.FileSystemObject ActiveX] Close()')

def BuildPath(self, arg0, arg1):
    log.MAEC.add_behavior_warn('[Script.FileSystemObject ActiveX] BuildPath("%s", "%s")' % (arg0, arg1, ))

def GetSpecialFolder(self, arg):
    log.MAEC.add_behavior_warn('[Script.FileSystemObject ActiveX] GetSpecialFolder(%s)' % (arg, ))
    return '%TEMP%'
