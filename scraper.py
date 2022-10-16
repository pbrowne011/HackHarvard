# scraper

import requests

# URL = 'https://realpython.github.io/fake-jobs/'
# URL = 'https://www.lesswrong.com/posts/2rWKkWuPrgTMpLRbp/lesswrong-faq'
# page = requests.get(URL)

# print(page.text)

from selenium import webdriver
import chromedriver_install as cdi

path = cdi.installr'C:\Users\pjbro\AppData\Local\Temp\Temp1_chromedriver_win32.zip\chromedriver.exe'
driver = webdriver.Chrome(executable_path=path)

driver.get('https://www.lesswrong.com/posts/2rWKkWuPrgTMpLRbp/lesswrong-faq')

driver.find_element_by_id('lesswrong').send_keys('.')