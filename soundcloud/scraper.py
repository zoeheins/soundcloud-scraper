from selenium import webdriver

def scrape():
    # temporarily hardcoding url
    url = 'https://soundcloud.com/user774261744/sets/jamz'
    driver = webdriver.PhantomJS()

    # how to determine window size so that all tracks fit
    # could also scroll to bottom
    driver.set_window_size(2000, 2000)
    driver.get(url)
    return driver.page_source
