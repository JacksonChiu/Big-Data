import requests
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.options import Options

from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from selenium.common.exceptions import TimeoutException

import time
from bs4 import BeautifulSoup

# options = Options()
# options.add_argument("--headless")

driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
driver.implicitly_wait(10)

driver.get("https://covid-19.nchc.org.tw/city_confirmed.php?mycity=%E5%85%A8%E9%83%A8%E7%B8%A3%E5%B8%82")
# now_page_src = driver.page_source
# soup = BeautifulSoup(now_page_src, "lxml")

# element1=driver.find_element(By.XPATH,"//*[@id='myTable03_wrapper']/div[4]/div[3]/div/table/tfoot/tr/th[1]/input")
# element1.click()
# element1.send_keys("2023-03-14")

element2=driver.find_element(By.XPATH,"//*[@id='myTable03_wrapper']/div[4]/div[3]/div/table/tfoot/tr/th[3]/input")
element2.click()
element2.send_keys("全區")

delay=30

try:
    myElement = EC.presence_of_all_elements_located((By.XPATH,"//*[@id='myTable03_wrapper']/div[4]/div[3]/div/table/tfoot/tr/th[3]/input"))
    WebDriverWait(driver, delay).until(myElement)
    print("Loading page is ready!!")
except TimeoutException:
    print("Loading page took too much time!!")

js = "document.getElementsByClassName('dataTables_scrollBody')[1].scrollTop=50000"
driver.execute_script(js)

time.sleep(5)

now_page_src=driver.page_source
soup = BeautifulSoup(now_page_src, "lxml")
#print(driver.page_source)

tag_td = driver.find_elements(By.XPATH, '//*[@id="myTable03"]/tbody')
for tag in tag_td:
    print(tag.text)

time.sleep(10)
driver.quit()


