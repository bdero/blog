Title: "Unlikr": Unlike everything on Tumblr
Date: 2013-12-04 23:28
Category: Scripts
Tags: firefox, python, robot, script, selenium, tool, tumblr, unlikr
Slug: unlikr
Authors: Brandon DeRosier
Summary: So, if you're not so much like me, you use Tumblr - and you probably have thousands of likes and reblogs. Of course, your taste for material might change over time.

# **Warning: This probably doesn't work anymore!**
**This script is brittle because it relies on non-versioned endpoints not intended for robots. Some people have messaged me to let me know that this script doesn't work anymore. Despite this, I'm keeping it here as a reference in case others may find it useful.**

So, if you're not so much like me, you use Tumblr - and you probably have thousands of likes and reblogs. Of course, your taste for material might change over time.

Originally sketched in an IPython Notebook for my partner, the following is a quick Python 2 script to wipe out <em>most</em> of your likes in a way that's pretty difficult for the Tumblr police to detect<!--more-->:

```python
#!/usr/bin/env python
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.common.exceptions import NoSuchElementException
from time import sleep
from sys import argv
find_likes = lambda browser: browser.find_elements_by_css_selector('.post_control.like.liked')
def find_next_page(browser):
    try:
        return browser.find_element_by_id('next_page_link')
    except NoSuchElementException, e:
        return None
def login(browser, username, password):
    # Login to Tumblr
    browser.get('https://www.tumblr.com/login')
    e = browser.find_element_by_name('user[email]')
    e.send_keys(username)
    e = browser.find_element_by_name('user[password]')
    e.send_keys(password + Keys.RETURN)
def unlikr(username, password):
    browser = webdriver.Firefox()
    login(browser, username, password)
    # Go to likes page
    browser.get('https://www.tumblr.com/likes')
    # Destroy those likes!
    likes = find_likes(browser)
    while True:
        for button in likes:
            button.click()
            # You can technically just floor it, but you might look too much like a robot
            sleep(0.1)

        browser.get(browser.current_url) # Faster than refreshes
        likes = find_likes(browser)
        # Every once in a while you have to move to a new page instead of refreshing
        # Tumblr seems like kind of a fuck up in this regard
        next_page = find_next_page(browser)
        while next_page and not likes:
            next_page.click()
            likes = find_likes(browser)
            next_page = find_next_page(browser)
def usage():
    print 'usage: unlikr [username] [password]'
def die(code):
    usage()
    exit(code)
if __name__ == '__main__':
    if len(argv) != 3:
        die(1)
    username, password = argv[1:]
    unlikr(username, password)
```

<h3>To use:</h3>
<ol>
<li><strong>Install <a href="http://www.python.org/download/" title="Python download page" target="_blank">Python 2</a></strong>.</li>
<li><strong>Install <a href="https://www.mozilla.org/firefox" title="Mozilla Firefox site" target="_blank">Mozilla Firefox</a></strong>.</li>
<li><strong>Install <a href="http://www.pip-installer.org/en/latest/installing.html" title="How to install pip" target="_blank">pip</a></strong>, the Python package manager. Windows users see <a href="https://stackoverflow.com/a/12476379" title="How to install pip on Windows" target="_blank">this guide</a>.</li>
<li><strong>Install <a href="https://pypi.python.org/pypi/selenium" title="Selenium PyPI page" target="_blank">Selenium</a> using pip</strong>: run `<strong>pip install selenium</strong>` from a terminal.</li>
<li><strong>Save the above script</strong> as `<strong>unlikr.py</strong>`.</li>
<li><strong>Run the script</strong> by executing `<strong>python unlikr.py [USERNAME] [PASSWORD]</strong>` in a terminal, replacing `<strong>[USERNAME]</strong>` and `<strong>[PASSWORD]</strong>` with your respective Tumblr credentials.</li>
</ol>

<h3>What it does:</h3>
Upon running the script, a new instance of Firefox will open with a blank profile, navigate to Tumblr, login, navigate to your likes page, and proceed to click the unlike buttons for every post at a maximum speed of 5 unlikes per second. You can then proceed to go get some tea or coffee. If you have 10,000 likes, the script will probably take about an hour to clean it all out - 33 minutes for unliking things, and the rest for page refreshes and hitting the `Next Page` button.

<h3>What it doesn't:</h3>
Tumblr is weird. Search around for people complaining about not being able to look through all of their liked content and you'll find many examples.
<strong>This tool can't beat the fact that Tumblr hides things from you</strong>, so you might reach a point where the script has been hitting the `Next Page` hundreds of times without finding a single `like`. At this point, you're likely not going to find any more content to unlike, even if Tumblr's reporting that you still `like` hundreds or thousands of posts.

<h3>Why Selenium?</h3>
I was having a Selenium kind of day and I didn't feel like dancing around any client-side verification. Sure, you might need a display to run it - but if you use Tumblr, you've probably got one. Besides, look at how simple that script is with Firefox doing all the work!


If you'd like to use this and you're having trouble getting it to work, please leave a comment below and I will help you.
