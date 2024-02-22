import requests
from bs4 import BeautifulSoup
from urllib.request import urlopen
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By


# 크롤링
url = 'https://www.koreabaseball.com/Record/Player/HitterDetail/Total.aspx?playerId=67449'
url = 'https://www.koreabaseball.com/Record/Player/Runner/Basic.aspx'

driver = webdriver.Chrome()
driver.get(url)

html = driver.page_source
soup = BeautifulSoup(html, 'html.parser')
# summary = 통산기록에서 td를 찾기
records = soup.find_all('td',)
cnt = 0
for record in records:
    cnt += 1
    print(record.text, end=' ')
    if cnt % 22:
        print()

driver.close()
driver.quit()