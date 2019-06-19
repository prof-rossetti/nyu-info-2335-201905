# The `selenium` Package

The `selenium` package provides capabilities for automating the process of browsing the web and interacting with elements on any web page.

Reference:

  + [Source Code](https://github.com/SeleniumHQ/selenium/tree/master/py)
  + [Official Docs](https://seleniumhq.github.io/selenium/docs/api/py/api.html)
  + [Unofficial Docs](https://selenium-python.readthedocs.io/index.html)

## Prerequisites

Before proceeding, we need to install a special kind of web browser called a "web driver" which the Selenium package will be able to control.

There are options to use a Firefox-based browser, but the professor recommends you [install the Google Chrome-based "Chromedriver"](/notes/clis/chromedriver.md#installation). Identify the path to where you have installed `chromedriver`. We'll need this value later (see `CHROMEDRIVER_PATH` variable below in the "Usage" example).

## Installation

After installing a web driver, install the package using Pip, as necessary:

```sh
pip install selenium
```

## Usage

First, initialize a new driver object. You can do so in the default mode, which will open a browser window for you to view, or in "headless" mode, which will not open a browser window.

```py
from selenium import webdriver
from selenium.webdriver.common.keys import Keys

#
# INITIALIZE THE DRIVER
#

CHROMEDRIVER_PATH = "/usr/local/bin/chromedriver" # (or wherever yours is installed)

driver = webdriver.Chrome(CHROMEDRIVER_PATH)

# ... OR IN "HEADLESS MODE"...
# options = webdriver.ChromeOptions()
# options.add_argument('--incognito')
# options.add_argument('--headless')
# driver = webdriver.Chrome(CHROMEDRIVER_PATH, chrome_options=options)
```

After initializing a driver, use it to visit and interact with web pages:

```py
#
# NAVIGATE TO GOOGLE.COM...
#

driver.get("https://www.google.com/")
print(driver.title) #> Google
driver.save_screenshot("search_page.png")

#
# FIND AN ELEMENT TO INTERACT WITH...
# a reference to the HTML element:
# <input title="Search">

searchbox_xpath = '//input[@title="Search"]'
searchbox = driver.find_element_by_xpath(searchbox_xpath)

#
# INTERACT WITH THE ELEMENT
#

search_term = "Prof Rossetti GitHub"
searchbox.send_keys(search_term)

searchbox.send_keys(Keys.RETURN)
print(driver.title) #> 'Prof Rossetti GitHub - Google Search'
driver.save_screenshot("search_results.png")

#
# ALWAYS QUIT THE DRIVER
#

driver.quit()
```

Resulting screenshots:

![](/exercises/automated-browsing/search_page.png)

![](/exercises/automated-browsing/search_results.png)


### Parsing Page Contents

We can use [the `beautifulsoup` package](/notes/python/packages/beautifulsoup.md) to parse the HTML contents of any page. When doing so, we can pass the web driver's `page_source` attribute, which contains the page's raw HTML contents.

### Waiting for Page Contents

Sometimes websites employ advanced mechanisms to hide certain page contents during initial load, which makes them more difficult to parse. So in order to access the desired contents, we first need to "wait" for the contents to load:

```py
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException
from bs4 import BeautifulSoup

request_url = "https://www.baseball-reference.com/players/c/cessalu01.shtml" # an example player (pitcher)
print(f"GETTING MLB STATS FROM {request_url}")

driver = webdriver.Chrome("/usr/local/bin/chromedriver") # location where chromedriver is installed
print(type(driver)) #> <class 'selenium.webdriver.chrome.webdriver.WebDriver'>

try:

    driver.get(request_url)
    print(driver.title) #> Luis Cessa Stats | Baseball-Reference.com

    #
    # WAITING FOR ELEMENT: <table id="pitching_value" >
    #

    print("WAITING FOR PAGE CONTENTS TO LOAD...") # this might take a long time
    table_appears = EC.presence_of_element_located((By.ID, "pitching_value")) # double parens here indicate a "tuple" datatype
    wait_duration = 3 # (seconds)
    WebDriverWait(driver, wait_duration).until(table_appears)
    print("PAGE CONTENTS LOADED!")

    #
    # PARSE THE CONTENTS WITH BSOUP
    #

    print("PARSING HTML TABLE...")
    soup = BeautifulSoup(driver.page_source, "html.parser")
    print(type(soup)) #>

    stats_table = soup.find("table", id="pitching_value")
    type(stats_table) #>

except TimeoutException:
    print("TIME OUT!")
finally:
    driver.quit() # always close the web browser to prevent memory issues
```
