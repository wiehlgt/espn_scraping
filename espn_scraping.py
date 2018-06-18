from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from selenium import webdriver
from bs4 import BeautifulSoup as bs4
import pandas as pd


path_to_chromedriver = 'C:/Users/gwhy5/Desktop/python.py/chromedriver.exe' # change path as needed
driver = webdriver.Chrome(executable_path = path_to_chromedriver)
driver.wait = WebDriverWait(driver, 15)
url = 'http://games.espn.com/ffl/freeagency?teamId=5&leagueId=1032719&seasonId=2017#&seasonId=2017&avail=-1'

driver.get(url)
frm = driver.find_elements_by_id('disneyid-iframe')
driver.switch_to.frame('disneyid-iframe')
email = driver.find_element_by_css_selector('#did-ui > div > div > section > section > form > section > div:nth-child(1) > div > label > span.input-wrapper > input')
email.send_keys('wiehlgt@mymail.vcu.edu')
password = driver.find_element_by_css_selector('#did-ui > div > div > section > section > form > section > div:nth-child(2) > div > label > span.input-wrapper > input')
password.send_keys('H0tdogdude')
button = driver.find_element_by_css_selector('#did-ui > div > div > section > section > form > section > div.btn-group.touch-print-btn-group-wrapper > button')
button.click()
#Wait until last data in last row is loaded just in case:
last_elem = driver.wait.until(EC.visibility_of_element_located(
       (By.XPATH, '//*[@id="plyr16757"]/td[14]/nobr/span'))) 
driver.switch_to_default_content()
#pulls together soup, scrapes tables for text
soup = bs4(driver.page_source, 'lxml')
table = soup.find(id="playertable_0")
rows = table.find_all(class_=["playerTableBgRowSubhead tableSubHead","pncPlayerRow playerTableBgRow0","pncPlayerRow playerTableBgRow1" ])

rows = iter(rows)
header_1 = [td.text for td in next(rows).find_all('td') if td.text]
#remove action from headers as it is unecessary and gets in the way
del header_1[2]
data = []
for row in rows:
    data.append([td.text for td in row.find_all('td') if td.text])

df = pd.DataFrame(data)
print df
