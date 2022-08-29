from selenium import webdriver
from time import sleep


email = '<Your Email>'
password = '<Your Password>'

browser = webdriver.Chrome()

browser.get("https://tinder.com/")

browser.implicitly_wait(5)

cookie_acpt_btn = browser.find_element('xpath', '/html/body/div[1]/div/div[2]/div/div/div[1]/div[1]/button').click()

sleep(2)

login = browser.find_element('xpath', '/html/body/div[1]/div/div[1]/div/main/div[1]/div/div/div/div/header/div/div[2]/div[2]/a').click()

sleep(2)

try:
    google_login_btn = browser.find_element('xpath', "//button[@aria-label='Log in with Google']")
    google_login_btn.click()
except:
    
    google_login_btn = browser.find_element('xpath', '/html/body/div[2]/main/div/div[1]/div/div/div[3]/span/div[1]/div/button/span[2]').click()    # span xpath
    google_login_btn.click()


# google_login_btn = browser.find_element('xpath', '/html/body/div[2]/main/div/div[1]/div/div/div[3]/span/div/div/button').click()   # div xpath
browser.implicitly_wait(4)
try:
    sleep(3)
    base_window = browser.window_handles[0]
    google_popup_page = browser.window_handles[1]

    browser.switch_to.window(google_popup_page)
except:
    sleep(3)
    base_window = browser.window_handles[0]
    google_popup_page = browser.window_handles[1]
    
    browser.switch_to.window(google_popup_page)

email_box = browser.find_element('xpath', '//input[@name= "identifier"]')
email_box.send_keys(email)

nxt_btn = browser.find_element('xpath', "//*[@id='identifierNext']/div/button/span").click()

pass_box = browser.find_element('xpath', '//input[@name= "password"]')
pass_box.send_keys(password)

nxt_btn = browser.find_element('xpath', '//*[@id="passwordNext"]/div/button/span').click()

try:
    loc_box = browser.find_element('xpath', '//*[@id="t-1917074667"]/main/div/div/div/div[3]/button[1]').click()
except:
    print("did not work")

try:
    accept_notification_box = browser.find_element('xpath', '/html/body/div[2]/main/div/div/div/div[3]/button[1]/span')
except:
    print("did not work")


