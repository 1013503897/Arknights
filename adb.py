from os import system

class adbKit(object):

    def screenshots(self, serialNumber=None):
        self.command('shell screencap -p /sdcard/screencap.png', serialNumber)
        self.command('pull /sdcard/screencap.png', serialNumber)

    def command(self, cmd, serialNumber=None):
        cmdstr = 'adb '
        if serialNumber:
            cmdstr = cmdstr+'-s '+serialNumber
        system(cmdstr+cmd)

    def click(self, point, serialNumber=None):
        return self.command('shell input tap ' + str(point[0]) + ' ' + str(point[1]), serialNumber)

