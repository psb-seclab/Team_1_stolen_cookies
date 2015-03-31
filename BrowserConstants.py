#
# This script is used to hold shared values between the import/export scripts
#

import os

appDataDir = os.getenv('APPDATA') #Storing the %Appdata% directory

firefoxCookieFile = "cookies.sqlite"  #Cook file to search for in the Firefox directory
firefoxCookieFileBackup = "cookies.sqlite.bak"  #Cookie file has a backup that must be accounted for
firefoxCookieFileBackupRe = "cookies.sqlite.bak-rebuild"  #Cookie file has a backup that must be accounted for
firefoxSessionCookies = "sessionstore.js"  #These are session cookies thatmust be accounted for

chromeCookieFile = "Cookies"
chromeCookieJournal = "Cookies-journal"
chromeSessionCookies = "Current Session"

if not os.path.exists('exportedCookies/'):
	os.makedirs('exportedCookies/') #Create a directory for the script to export the cookies to
if not os.path.exists('exportedCookies/Firefox'):
	os.makedirs('exportedCookies/Firefox') #Create a directory for the script to export the firefox cookies to
if not os.path.exists('exportedCookies/Chrome'):
	os.makedirs('exportedCookies/Chrome') #Create a directory for the script to export the chrome cookies to
if not os.path.exists('exportedCookies/IE'):
	os.makedirs('exportedCookies/IE') #Create a directory for the script to export the IE cookies to