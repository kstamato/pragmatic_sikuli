import unittest
from _lib import *
import HTMLTestRunner

class SmokeTests(unittest.TestCase):
    def Test_Login(self):
        Browser.Start("file:///Users/kstamato/Desktop/Demos_Pragmatic/HTMLs/1_SampleWebpage.html")
        Browser.Page_Down()
        sleep(1)
        click(SamplePage_UI.user_name)
        sleep(1)
        type("usrename1")
        sleep(1)
        click(SamplePage_UI.password_f)
        type("somepass")
        type(Key.ENTER)
        find(SamplePage_UI.logged_in).highlight(2)
        
        


if __name__ == '__main__':
    #suite = unittest.TestLoader().loadTestsFromTestCase(SmokeTests)

    #Use it to add manually test cases - handy when debugging a specific part of the set
    suite = unittest.TestSuite()
    suite.addTest(SmokeTests("Test_Login"))
    # suite.addTest(SmokeTests('test_200_Get_Logo_Link'))
    # outfile = open("Report.html", "w")
    runner = HTMLTestRunner.HTMLTestRunner(file(r"Report.html", "w"))
    runner.run(suite)
    # outfile.close()