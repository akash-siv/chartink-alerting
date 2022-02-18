from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
import os
import stat
from selenium.webdriver.chrome.options import Options
import time
import telegram_send
# import os
# import wget

# Initializing
# file_path = 'chromedriver'
# driver = webdriver.Chrome(file_path)
# driver.get("https://chartink.com/screener/macd-scan-3012193")

st = os.stat('chromedriver')
os.chmod('chromedriver', st.st_mode | stat.S_IEXEC)
chrome_options = Options()
chrome_options.add_argument("--headless")
chrome_options.add_argument("--disable-gpu")
chrome_options.add_argument("--no-sandbox")
driver = webdriver.Chrome('./chromedriver', options=chrome_options)
driver.get("https://chartink.com/screener/macd-scan-3012193")

time.sleep(3)
stock_list = []
start = False

# Initializing
while True:

    if start:
        break

    a = driver.find_elements(By.CSS_SELECTOR, 'td:nth-child(3) .text-teal-700')
    for i in a:
        if i.text in stock_list:
            start = True
        stock_list.append(i.text)

    print(stock_list)
    print(len(stock_list))

    next_page = WebDriverWait(driver, 2).until(EC.element_to_be_clickable((By.CSS_SELECTOR, "#DataTables_Table_0_next a"))).click()
    time.sleep(3)

telegram_send.send(messages=[stock_list])

