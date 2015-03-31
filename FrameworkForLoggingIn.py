import cookielib
import os
import urllib
import urllib2

#Generic login credentials, will need special creds for special sites
generic_username = "lololol@hotmail.com"
generic_password = "GodBless9001"

cookie_filename = ""

class CaptureCookies(object):

    def __init__(self, login, password, host, loginURL):
        """ Start up... """
        #Store variables for local access
        self.login = login
        self.password = password
        self.host = host
        self.loginURL = loginURL

        #Name the cookie file based on host
        cookie_filename = host + ".cookies"
        #Create the cookie
        self.cj = cookielib.MozillaCookieJar(cookie_filename)

        #preparing library to open up a site
        self.opener = urllib2.build_opener(
            urllib2.HTTPRedirectHandler(),
            urllib2.HTTPHandler(debuglevel=0),
            urllib2.HTTPSHandler(debuglevel=0),
            urllib2.HTTPCookieProcessor(self.cj)
        )
        #Preparing headers that will be spoofed for the site
        self.opener.addheaders = [
            ('User-agent', ('Mozilla/5.0 (X11; U; FreeBSD i386; en-US; rv:1.8.1.14) Gecko/20080609 Firefox/2.0.0.14')),
            ('Accept', ('text/xml,application/xml,application/xhtml+xml,text/html;q=0.9,text/plain;q=0.8,text/png,*/*;q=0.5')),
            ('Accept-Language', ('en-us,en;q=0.5')),
            ('Accept-Charset', ('ISO-8859-1')),
            ('Content-type', ('application/x-www-form-urlencoded')),
            ('Host', (self.host))
        ]

        self.loginToFacebook()  #A unique function for logging into facebook

        self.cj.save() #Save the cookie

    def loginToFacebook(self):
        """
        Handle login. This should populate our cookie jar.
        """
        login_data = urllib.urlencode({
            'email' : self.login,
            'pass' : self.password,
            'login':'Log+In'
        })
        response = self.opener.open(self.loginURL, login_data)
        return ''.join(response.readlines())

class AccessWebsite(object):

    def __init__(self, host, loginURL):
        """ Start up... """
        cookie_filename = host + ".cookies" #Make sure we are accessing the proper cookie
        #Store variables for local access
        self.host = host
        self.loginURL = loginURL

        #loading cookies into memory
        self.cj = cookielib.MozillaCookieJar(cookie_filename)
        if os.access(cookie_filename, os.F_OK):
            self.cj.load()
        else:
            print "Error loading cookies."
            return ''

        #preparing library to open up a site
        self.opener = urllib2.build_opener(
            urllib2.HTTPRedirectHandler(),
            urllib2.HTTPHandler(debuglevel=0),
            urllib2.HTTPSHandler(debuglevel=0),
            urllib2.HTTPCookieProcessor(self.cj)
        )
        #Preparing headers that will be spoofed for the site
        self.opener.addheaders = [
            ('User-agent', ('Mozilla/5.0 (X11; U; FreeBSD i386; en-US; rv:1.8.1.14) Gecko/20080609 Firefox/2.0.0.14')),
            ('Accept', ('text/xml,application/xml,application/xhtml+xml,text/html;q=0.9,text/plain;q=0.8,text/png,*/*;q=0.5')),
            ('Accept-Language', ('en-us,en;q=0.5')),
            ('Accept-Charset', ('ISO-8859-1')),
            ('Content-type', ('application/x-www-form-urlencoded')),
            ('Host', (self.host))
        ]

        self.accessSite()

        #Function that will access the website and output the results
    def accessSite(self):
        response = self.opener.open(self.loginURL)
        print response.getcode()
        #print response.info()
        print response.read()
        return response.read()

capturing = CaptureCookies(generic_username, generic_password, 'm.facebook.com', "http://m.facebook.com/login.php?m=m&refsrc=m.facebook.com%2F")
accessing = AccessWebsite('m.facebook.com', "http://m.facebook.com/")