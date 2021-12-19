import time

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time

url = "http://orteil.dashnet.org/experiments/cookie/"
chrome_driver_path = "C:\Programming\Web Driver\chromedriver.exe"
service = Service(chrome_driver_path)
driver = webdriver.Chrome(service=service)
game_over = time.time() + 60 * 5
driver.get(url)

def click_cookie():
    cookie = driver.find_element(By.ID, "cookie")
    timeout = time.time() + 5
    print("clicking")
    while time.time() < timeout:
        cookie.click()
    shop_items()

def shop_items():
    store = driver.find_elements(By.CSS_SELECTOR, "#store b")
    money = int(driver.find_element(By.ID, "money").text.replace(',', ''))
    print(f"money: {money}")
    print('shopping')
    prices = [int(store[item].text.split("-")[1].strip().replace(',', '')) for item in range(len(store) - 1)]
    items = [store[item].text.split("-")[0].strip() for item in range(len(store) - 1)]
    cps = driver.find_element(By.ID, 'cps').text
    high_price = []

    # for price in prices:
    #     if money > price:
    #         print(prices[price])
    for i in range(len(prices)):
        if money > prices[i]:
            high_price = prices[i]
            # high_price.append(prices[i])
            # highest_price = high_price[-1]
            # print(f"price list: {high_price}, highest price: {highest_price}")
            # buy = items[prices.index(prices[i])]
            # print(f"buy{buy}")
            # print(f"money: {money}")
            # if money > highest_price:
            # find_buy = driver.find_element(By.ID, f"buy{buy}")
            # find_buy.click()
            # print(f"buying: {buy}")
            time.sleep(.1)
    print(f"cps: {cps}")
    print(high_price)
    print(prices.index(high_price))
    buy = items[prices.index(high_price)]
    find_buy = driver.find_element(By.ID, f"buy{buy}")
    find_buy.click()

    if time.time() < game_over:
        click_cookie()

click_cookie()


print(f"Your Cookies Per Second was: {driver.find_element(By.ID, 'cps').text}")
# shop_items()

# driver.quit()