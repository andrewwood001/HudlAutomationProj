# HudlAutomationProj
Automation Project for Hudl 

# About this project
This is a collection of tests written by Andrew Wood in the Python language using Selenium.  These tests automate the basic functionality of logging into the Hudl website (https://hudl.com).

# Built With
This script was built with PyCharm Community Edition 2022.1.4: [Pycharm](https://www.jetbrains.com/pycharm/download/#section=windows)

# Installation & Operation
1. Clone the GitHub Repository (git clone https://github.com/andrewwood001/HudlAutomationProj.git), or download directly from the link [HTTPS Download Link](https://github.com/andrewwood001/HudlAutomationProj.git)
2. Open the file "test_login.py" with PyCharm Community Edition
3. Install the required packages to run the automation scripts. Click on File > Settings > Project: Downloads (left-hand column) > Python Interpreter > + (Plus Sign):
* Selenium (V.4.3.0)
* PyTest (V. 7.1.2)
* Unitest (V. 1.4.9)
* Configparser (V 0.5.1)
4. Click Ok on the Settings Menu once all Packages have been installed/applied
5. Open the file "test_base.py" and update the Webdriver to the correct path for the desired browser driver on the local machine (i.e "self.driver = webdriver.Chrome(executable_path="C:\Selenium\chromedriver.exe""). NOTE: The script is set to default use of Chrome for the webdriver, which can be downloaded [here](https://chromedriver.chromium.org/downloads)
6. Update the "config.ini" file with correct user login information
7. In the 'test_login.py" file, click the green "Play" icon in the top right corner of PyCharm to run the script

# Contact
Andrew Wood - andrew.wood.001@gmail.com
https://github.com/andrewwood001/HudlAutomationPro
