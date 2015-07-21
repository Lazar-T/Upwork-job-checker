#!/usr/bin/python
import os
import json
import mechanize
import cookielib
from bs4 import BeautifulSoup
import information


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
br.addheaders = [("User-agent", "Mozilla/5.0 (X11; U; Linux i686; en-US; rv:1.9.0.1) Gecko/2008071615 Fedora/3.0.1-1.fc9 Firefox/3.0.1")]

# Open upwork site
r = br.open("https://www.upwork.com/login.php")
form = br.forms().next()  # the login form is unnamed...

form["username"] = information.username
form["password"] = information.password
br.form = form
br.submit()


url = "https://www.upwork.com/jobs/?nbs=1&g=&q=%s" % information.search_word
page_url = br.open(url)
soup = BeautifulSoup(br.response().read())

titles = soup.find_all("h1", "oRowTitle oH3")

l = []

for i in titles:
    l.append(i.text)


fname = "%s/list_of_jobs.json" % os.getcwd()

with open(fname, "wb") as f:
    json.dump(l, f)
