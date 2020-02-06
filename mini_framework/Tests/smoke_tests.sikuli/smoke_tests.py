import unittest
from _lib import Browser
import HTMLTestRunner

class SmokeTests(unittest.TestCase):
    def test_100_Start_Browser(self):
        print("XXXXXXXXX Test 1111 started XXXXXXXXX")
        Browser.Start("www.python.org")
        # Browser.Maximize()

    def test_200_Get_Logo_Link(self):
        print("XXXXXXXXX Test 222 started XXXXXXXXX")
        Browser.Copy_Image_URL()
        p_link = Env.getClipboard()
        print(p_link)
        assert "python.org/" in p_link

# suite = unittest.TestLoader().loadTestsFromTestCase(SmokeTests)
# HtmlXmlTestRunner.HTMLTestRunner(file(r"Report.html", "w")).run(suite)

# ↓↓↓↓↓ In the end of the file is another logic to run test ↓↓↓↓↓↓↓
if __name__ == '__main__':
    #suite = unittest.TestLoader().loadTestsFromTestCase(SmokeTests)

    #Use it to add manually test cases - handy when debugging a specific part of the set
    suite = unittest.TestSuite()
    suite.addTest(SmokeTests("test_100_Start_Browser"))
    suite.addTest(SmokeTests('test_200_Get_Logo_Link'))
    # outfile = open("Report.html", "w")
    runner = HTMLTestRunner.HTMLTestRunner(file(r"Report.html", "w"))
    runner.run(suite)
    # outfile.close()






## It's not the shortest version, but for sure it works stable for years :)
## Recommended to use it
# if __name__ == '__main__':
#     suite = unittest.TestLoader().loadTestsFromTestCase(SmokeTests)

#     # #Use it to add manually test cases - handy when debugging a specific part of the set
# 	  # suite = unittest.TestSuite()
#     # suite.addTest(SmokeTests('test_100_Start_Browser'))
#     # suite.addTest(SmokeTests('FREE_SLOT_FOR_THE_NEXT_TEST'))

#     outfile = open("Report.html", "w")
#     runner = HtmlXmlTestRunner.HTMLTestRunner(stream=outfile, title='SmokeTests Report', description="Description")
#     runner.run(suite)
#     outfile.close()
