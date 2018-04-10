from selenium import webdriver

def scrape(url, window_height):
    driver = webdriver.PhantomJS()
    # TODO set window_size dynamically based on # of songs
    # or ideally just auto scroll to bottom of page
    driver.set_window_size(1000, window_height)
    driver.get(url)
    return driver.page_source
