from selenium import webdriver

def scrape(url, window_height):
    driver = webdriver.PhantomJS()
    driver.set_window_size(1000, window_height)
    driver.get(url)
    return driver.page_source
