# Upwork-job-checker
Get notified when new job posting is available at [upwork.com](https://www.upwork.com/)


###Screenshot

![Screenshot](http://i.imgur.com/GoE8gp4.jpg)

###About

Upwork-job-checker is automation software that goes on freelance site [upwork.com](https://www.upwork.com/) and fetches latest jobs defined by keyword specified, so you don't have to manually check every five minutes if there's new offerings on the site. Option to send [sms message](https://www.twilio.com/) to your phone when there's update and option to open job url in a browser(as shown in screenshot).

###Usage

For proper use you will need to enter valid username, password, search word(python, ruby...), and path to the exact location where Upwork-job-checker folder is.

This is intended to  be integrated with cron job so you will need to open terminal emulator and type:
```
crontab -e
```

Once inside scheduler type:
```
*/5 * * * * DISPLAY=:0 /usr/bin/python /path/to/the/Upwork-job-checker/main.py


@reboot sleep 30 && python /path/to/the/Upwork-job-checker/update_json.py > /path/to/the/Upwork-job-checker/file.log 2>&1
```

The first command will be executed every 5 minutes to see if there's new job postings. Second command is intended for updating json file where job listings are located, and store information on log file.

To stop running simply type:
```
crontab -e
```
And put comment sign(#) in front of previously mentioned commands.

### Requirements

Upwork-job-checker is using [pynotify](http://home.gna.org/py-notify/) to display notifications, [pygame](http://pygame.org/news.html) to play notification sound, [Beautiful Soup](http://www.crummy.com/software/BeautifulSoup/) for scraping, [mechanize](https://pypi.python.org/pypi/mechanize/) for emulating browser, [twilio](https://www.twilio.com/) for sending sms message.


### Installation and Running
```
git clone https://github.com/Lazar-T/Upwork-job-checker

```
Proper running is explained in Usage part.

