#vimming under the influence - You can't afford it.

#usage -- python cookieMonster.py http://someUrl.com
#for more info -- http://stackoverflow.com/questions/5606083/how-to-set-and-retrieve-cookie-in-http-header-in-python

import sys
import cookielib
import urllib2

cookies = cookielib.LWPCookieJar()
handlers = [	urllib2.HTTPHandler(),
		urllib2.HTTPSHandler(),
		urllib2.HTTPCookieProcessor(cookies)]

def main():
	uri = sys.argv[1]
	fetch(uri)
	for cookie in cookies:
		print cookie.name, cookie.value
	#cookies.save('cookies.txt')

def fetch(uri):
	opener = urllib2.build_opener(*handlers)
	response = urllib2.Request(uri)
	return opener.open(response)
	


if __name__ == '__main__':
	main()
