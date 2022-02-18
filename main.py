from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.chrome.options import Options
import time
import telegram_send
from scaping_links import chartink_links_swing
import os
# import wget

file_path = 'chromedriver.exe'
chrome_options = Options()
chrome_options.add_argument("--headless")
driver = webdriver.Chrome(file_path, options=chrome_options)
swing_keys = list(chartink_links_swing.keys())
# intraday_keys = list(chartink_links_intraday.keys())


for i in swing_keys:
    driver.get(chartink_links_swing[i])
    time.sleep(2)
    semd_message = True
    stock_list = []
    # tg_send = []
    start = False
    # now_time = int(time.time())

    # Scraping the content
    while True:
        if start:
            break
        a = driver.find_elements(By.CSS_SELECTOR, 'td:nth-child(3) .text-teal-700')
        for j in a:
            if j.text in stock_list:
                start = True
            stock_list.append(j.text)
        next_page = WebDriverWait(driver, 2).until(EC.element_to_be_clickable((By.CSS_SELECTOR, "#DataTables_Table_0_next a"))).click()
        if len(stock_list) == 0:
            semd_message = False
            break
        time.sleep(2)

    # create link and send
    telegram_send.send(messages=[f"---------------------------------{i}------------------------------------"])
    for stock in set(stock_list):
        telegram_send.send(messages=[f"https://in.tradingview.com/chart/?symbol={stock}"])
        time.sleep(0.1)


# Todo: for swing send the stock list at 7.00am
# Todo: Send premarket data link in nifty.
