#!/usr/bin/env python
import re
import os
import time
import json
import urllib
import pynotify
from pygame import mixer
import mechanize
import cookielib
from bs4 import BeautifulSoup
from twilio.rest import TwilioRestClient
import information


pynotify.init("upwork")


# Browser
br = mechanize.Browser()

# Cookie Jar
cj = cookielib.LWPCookieJar()
br.set_cookiejar(cj)

# Browser options
br.set_handle_equiv(True)
br.set_handle_gzip(True)
br.set_handle_redirect(True)
br.set_handle_referer(True)
br.set_handle_robots(False)

# Follows refresh 0 but not hangs on refresh > 0
br.set_handle_refresh(mechanize._http.HTTPRefreshProcessor(), max_time=1)


# User-Agent
br.addheaders = [('User-agent', 'Mozilla/5.0 (X11; U; Linux i686; en-US; rv:1.9.0.1) Gecko/2008071615 Fedora/3.0.1-1.fc9 Firefox/3.0.1')]

# Open upwork site
r = br.open('https://www.upwork.com/login.php')
form = br.forms().next()  # the login form is unnamed...

form["username"] = information.username
form["password"] = information.password
br.form = form
br.submit()


url = "https://www.upwork.com/jobs/?nbs=1&g=&q=%s" % information.search_word
page_url = br.open(url)
soup = BeautifulSoup(br.response().read())

titles = soup.find_all('h1', 'oRowTitle oH3')
hrefs = soup.find_all('a', 'oVisitedLink')
job_href = 'https://www.upwork.com' + hrefs[0]['href']

l = []

for i in titles:
    l.append(i.text)


fname = "%s/list_of_jobs.json" % os.getcwd()


with open(fname, 'rb') as f:
    s = json.load(f)

    if s == l:
        pass

    else:
        result = re.sub("<.*?>", "", l[0])
        mixer.init()
        mixer.music.load("/home/asd/Python/odesk_check/sound.mp3")
        mixer.music.play()
        time.sleep(0.4)
        notifier = pynotify.Notification(result,
        "<i>keyword = " + information.search_word + "</i>" + "\n<a href=" + "'" + job_href + "'" + ">Open in browser</a>",
        "/path/to/Upwrork-job-checker/logo.png")
        notifier.show()

        sms_message = result + " kwd = " + information.search_word
        account_sid = ""
        auth_token = ""
        client = TwilioRestClient(account_sid, auth_token)
        message = (client.sms.messages.create(body=sms_message, to="",
        from_=""))
        time.sleep(10)

with open(fname, 'wb') as f:
    json.dump(l, f)
