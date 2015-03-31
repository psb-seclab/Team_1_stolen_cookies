#
# This script is used to download a user's cookies from their Firefox personal profile.
# Simply login into a few websites, then close the browser, then run the script
# Cookies that have been exported can be found in a directory where this script has been execute.
#

import os
import shutil
import BrowserConstants

appDataDir = BrowserConstants.appDataDir #Storing the %Appdata% directory

firefoxCookieFile = BrowserConstants.firefoxCookieFile  #Cook file to search for in the Firefox directory
chromeCookieFile = BrowserConstants.chromeCookieFile  #Cookie file to search for in the Chrome directory

#
# First is finding and ripping Mozilla Firefox cookies
#
if(os.path.isdir(appDataDir + "\Mozilla") and os.path.isdir(appDataDir + "\Mozilla\Firefox")): #Checking if Firefox is installed
	
	firefoxProfile = os.listdir(appDataDir + "\Mozilla\Firefox\Profiles")[0] #Storing the Firefox profile found in the Firefox directory
	firefoxPathToCookies = appDataDir + '\Mozilla\Firefox\Profiles\\' +firefoxProfile #Storing the whole directory path to the cookies

	if(os.path.isdir(firefoxPathToCookies)):  #Checking if building the path to the cookies exists
		if(os.path.exists(firefoxPathToCookies + "\\" + firefoxCookieFile)):  #Checking if the cookie files has been found
			shutil.copy2(firefoxPathToCookies + "\\" + firefoxCookieFile, 'exportedCookies/Firefox/' + firefoxCookieFile)  #Copy the Firefox cookies
		else:
			print "No cookies found for Firefox."
	else:
		print "Error computing Firefox user profile."
else: 
	print "User does not have Firefox installed."

#
# Secondd is finding and ripping Google Chrome cookies
#
if(os.path.isdir(appDataDir + "\..\Local\Google\Chrome")): #Checking if Chrome is installed
	
	chromePathToCookies = appDataDir + '\..\Local\Google\Chrome\User Data\Default' #Storing the whole directory path to the cookies

	if(os.path.isdir(chromePathToCookies)):  #Checking if building the path to the cookies exists
		if(os.path.exists(chromePathToCookies + "\\" + chromeCookieFile)):  #Checking if the cookie files has been found
			shutil.copy2(chromePathToCookies + "\\" + chromeCookieFile, 'exportedCookies/Chrome/' + chromeCookieFile)  #Copy the Firefox cookies
		else:
			print "No cookies found for Chrome."
	else:
		print "Error computing Chrome user profile."
else: 
	print "User does not have Chrome installed."