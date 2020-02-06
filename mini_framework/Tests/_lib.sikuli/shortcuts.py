from sikuli import *

class Shortcuts(object):
    @classmethod
    def Copy(self):
        type('c', Key.CTRL)
        sleep(0.5)

    @classmethod
    def Paste(self):
        type('v', Key.CTRL)
        sleep(0.5)

    @classmethod
    def SelectAll(self):
        type('a', Key.CTRL)
        sleep(0.5)
