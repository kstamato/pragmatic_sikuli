from sikuli import *
from _uimap import *
from shortcuts import *


class Browser(object):
    @classmethod
    def Start(self, url):
        print("Staring Chrome...")
        openApp("Google Chrome")
        sleep(2)
        type("t", Key.CMD)
        sleep(1)
        type("l", Key.CMD)
        sleep(1)
        type(url)
        type(Key.ENTER)
        sleep(2)
        print("Test PAge Opened in Chrome ....")

    @classmethod
    def Maximize(self):
        type("f", Key.CTRL, Key.CMD)

    @classmethod
    def OpenNewTab(self):
        type('t', Key.CMD)
        print("New Tap Opened")

    @classmethod
    def OpenURL(self, url):
        type('l', Key.CMD)
        sleep(0.5)
        paste(url)
        type(Key.ENTER)

    @classmethod
    def Copy_Image_URL(self):
        sleep(0.5)
        rightClick(Python_Org_UI.logo_link)
        sleep(0.5)
        type("co")
        sleep(0.5)
        type(Key.ENTER)
        sleep(2)
        
    @classmethod
    def Save_Image_As(self):
        rightClick(logo_link)
        sleep(1)
        click(save_as_img)
        wait(2)
        click()
        type(Key.ENTER)
    
    @classmethod
    def Page_Down(self):
        click()
        type(Key.DOWN, Key.CMD)
        print("Page is Down")
        sleep(2)


class UIActions(object):
    @classmethod
    def CopyAllClipboard(self):
        Shortcuts.SelectAll()
        Shortcuts.Copy()
        return Env.getClipboard()
        


