from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import WebDriverWait, Select
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By

import time, json, datetime

with open('./accounts.json') as f:
    config = json.load(f)

def waitForClick(xpath, twice=False):
    el = WebDriverWait(chrome, 10).until(
        EC.element_to_be_clickable((By.XPATH, xpath)))
    el.click()
    if twice:
        time.sleep(0.1)
        el.click()


def waitForKey(xpath, payload, summit=False):
    el = WebDriverWait(chrome, 10).until(
        EC.element_to_be_clickable((By.XPATH, xpath)))
    el.send_keys(payload)
    if summit:
        el.submit()


now = datetime.datetime.now()
delta = datetime.timedelta(days=59)
n_days = now+delta
span_idx = n_days.day + 1
print(n_days.month, n_days.day)

options = Options()
options.add_argument("--disable-notifications")
options.add_argument("--window-size=500,1080")
chrome = webdriver.Chrome('./chromedriver', options=options)
chrome.get("https://www.feastogether.com.tw/booking/2")

waitForClick("//*[@id=\"modal-news\"]/div/div/div/div/div[2]/div/a[1]")
waitForClick("//*[@id=\"header\"]/div[3]/div/div[6]/i")

waitForKey("//*[@id=\"form-login-header-mobile\"]/ul/li[1]/input", config['account'])
waitForKey("//*[@id=\"form-login-header-mobile\"]/ul/li[2]/input", config['password'], summit=True)

alert = WebDriverWait(chrome, 10).until(
    EC.alert_is_present()).accept()

# 人數
waitForKey('//*[@id="book_people"]', '8')
# 我知道了
chrome.find_element_by_xpath('//*[@id="book_date"]').click()
waitForClick('//*[@id="modal-default"]/div/div/div/div/div/div/a[1]')
# date select
waitForClick('/html/body/div[4]/div/div/div/ul/li[3]/div/input')
waitForClick('/html/body/div[14]/div[1]/span[2]/span')
for _ in range(n_days.month):
    time.sleep(0.2)
    waitForClick('/html/body/div[14]/div[1]/span[3]')

time.sleep(0.2)
waitForClick(f'/html/body/div[14]/div[2]/div/div[2]/div/span[{span_idx}]')
# 下午
# waitForClick('/html/body/div[4]/div/div/div/ul/li[4]/div/ul/li[2]')
# 晚餐
waitForClick('/html/body/div[4]/div/div/div/ul/li[4]/div/ul/li[3]')


# 選擇table
waitForClick('/html/body/div[4]/div/div/div/div[4]/div[2]/table/tr[4]/td[1]/div/span[1]')

# 第二頁
waitForClick('//*[@id="order_time"]')
waitForClick('//*[@id="order_time"]/option[2]')
waitForClick('/html/body/div[4]/div/div/div/div[2]/ul[2]/li[4]/button')
