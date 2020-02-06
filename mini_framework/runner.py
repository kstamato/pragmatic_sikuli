import os

# Precondition
#os.system("taskkill /IM chrome.exe /F")


##### RUN TESTS #####
#qos.system("fake cmd") # Workaround to enable colored logs
os.system(r"mini_framework/Sikuli/runsikulix -r mini_framework/Tests/smoke_tests_2.sikuli")


# Postcondition
#os.system("taskkill /IM chrome.exe /F")
