from fake_useragent import UserAgent
from selenium import webdriver
import random
from ..settings import PROXIES
import time

# headers = {
# 'User - Agent': UserAgent().random,
# }

# PROXIES=[
#     {"ipaddr":"182.101.207.11:8080"},
#     {"ipaddr":"114.230.120.42:9999"},
#     {"ipaddr":"121.231.216.23:8118"},
#     {"ipaddr":"49.75.59.242:3128"},
#     {"ipaddr":"114.233.131.216:9999"},
#     {"ipaddr":"183.157.172.77:8118"},
#     {"ipaddr":"122.237.83.112:9000"}
# ]

def sleep(seconds):
    time.sleep(seconds)

def create_chrome_driver():
    proxy = random.choice(PROXIES)
    print("******proxy"+proxy["ipaddr"])
    options = webdriver.FirefoxOptions()
    options.add_argument('--proxy-server='+proxy['ipaddr'])
    # options.add_argument('--proxy-server=182.101.207.11:8080')
    driver = webdriver.Firefox(executable_path='/usr/local/bin/geckodriver',firefox_options=options)
    # 浏览器开着方便调试
    # options.add_argument('--headless')
    # options.add_argument('--disable-gpu')
    # driver.add_argument('--ignore-certificate-errors')
    # driver.add_argument('--ignore-ssl-errors')
    # driver.add_argument('--proxy-server=http://190.171.158.109:999')
    driver.maximize_window()
    return driver

def find_element_by_css_selector(driver, selector):
    try:
        return driver.find_element_by_css_selector(selector)
    except:
        return None

def find_elements_by_css_selector(driver, selector):
    try:
        return driver.find_elements_by_css_selector(selector)
    except:
        return []