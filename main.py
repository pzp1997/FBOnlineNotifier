#!/usr/bin/env python2.7

"""
Get notified when your friend goes online on Facebook!
"""

from datetime import datetime
import json
import os
import time

from bs4 import BeautifulSoup
from selenium import webdriver

__author__ = 'Palmer Paul'
__version__ = '1.0.0'
__email__ = 'pzpaul2002@yahoo.com'

FACEBOOK_URL = 'https://www.facebook.com/'
DELAY = 60

# HTML classes used for parsing page
FRIEND_SIDEBAR_CLASS = '_55lp'
ONLINE_STATUS_CLASS = '_568-'
FRIEND_NAME_CLASS = '_55lr'

# Retrieve username and password
SETTINGS_FILE = 'settings.txt'
with open(SETTINGS_FILE, 'r') as f:
    settings = json.load(f)

# Initialize selenium
driver = webdriver.Firefox()
driver.get(FACEBOOK_URL)

# Sign in to Facebook
username_field = driver.find_element_by_name('email')
password_field = driver.find_element_by_name('pass')
username_field.send_keys(settings['username'])
password_field.send_keys(settings['password'])
password_field.submit()

online_now = set()

while True:
    # Retrieve HTML and parse it
    html = driver.page_source
    soup = BeautifulSoup(html, 'html5lib')

    # Get list of friends from chat sidebar
    friends_from_sidebar = soup.find_all('div', class_=FRIEND_SIDEBAR_CLASS)

    # Keep track of friends who were online `DELAY` seconds ago.
    online_before, online_now = online_now, set()

    # Populate `online_now` by checking which friends are online.
    for friend in friends_from_sidebar:
        online = friend.find(class_=ONLINE_STATUS_CLASS)
        if online is not None and online.get_text() == '':
            name = friend.find(class_=FRIEND_NAME_CLASS).get_text()
            online_now.add(name)

    # Find who has come online since `DELAY`
    came_online = online_now - online_before

    if came_online:
        # If a person in `special_people` comes online, say their name.
        for person in settings['special_people']:
            if person in came_online:
                os.system("say '{}'".format(person))

        # Log everyone who has come online
        print datetime.strftime(datetime.now(), '%a %b %d %I:%M %p')
        print '\n'.join(sorted(came_online))
        print

    # Wait `DELAY` seconds before reloading the page.
    time.sleep(DELAY)
    driver.refresh()

driver.quit()
