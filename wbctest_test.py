from selenium.webdriver import Chrome
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from  selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


import time
from airtest.core.api import *


# 基本上傳完成
driver = Chrome(executable_path = 'D:\Chrome\chromedriver_win32\chromedriver.exe') #提供chromedriver路徑

to_FlipClass = 'https://flipclass.stust.edu.tw/'  # flipclass網址
to_google = 'https://www.google.com/'

FlipAccount = ''
FlipPassword = ''
driver.get(to_FlipClass)  # 使用瀏覽器開啟網址

login_Account = driver.find_element_by_name("account")  # 找到帳號標籤
login_Account.send_keys("5A8G0001")  # 輸入帳號
login_Password = driver.find_element_by_name("password")  # 找到密碼標籤
login_Password.send_keys("a0973720803") # 輸入密碼
login_Password.send_keys(Keys.ENTER)  # 在密碼輸入盒按Enter


# /course/homework/課程編號(29396) span[text()='作業名稱']
WebDriverWait(driver, 20).until(EC.element_to_be_clickable((By.XPATH, "//div[@class='text']//span[text()='AddProj']"))).click() # 可以省略到只有span  # 點取作業名稱的作業
WebDriverWait(driver, 20).until(EC.element_to_be_clickable((By.XPATH, "//div[@class='text-center fs-margin-default']//span[text()='交作業']"))).click()  # 進入交作業畫面



driver.switch_to.frame(driver.find_element_by_class_name('fs-modal-iframe')) # 交作業畫面為一個內嵌的iframe 要 switch到裡面


path1 = r'D:\led12.py' # 要上傳的檔案的絕對路徑

#tt1 = driver.find_element_by_css_selector('.close').click()
WebDriverWait(driver, 5).until(EC.element_to_be_clickable((By.XPATH, '//span[text()="上傳檔案"]'))).click()  # 點擊上傳檔案按鈕

time.sleep(2)

text1 = driver.find_element_by_name('files[]').send_keys(path1)  # 因為學校上傳檔案的方式是input，故可以直接send_keys(路徑)
time.sleep(5) # 不可在上傳過程中做其他事
WebDriverWait(driver, 7).until(EC.element_to_be_clickable((By.CLASS_NAME, 'close'))).click()  # 關閉上傳畫面
WebDriverWait(driver, 7).until(EC.element_to_be_clickable((By.XPATH, '//*[@id="media-edit-form"]/div[7]/div/button[1]/span'))).click()  # 繳交 ， 同時可能會離開iframe






























#bt = driver.find_element_by_css_selector('button.btn btn-default')

#te1 = driver.find_element_by_xpath('//*[@id="action"]')
#print(te1)

#WebDriverWait(driver, 5).until(EC.element_to_be_clickable((By.XPATH, "//*[@id='page-main']"))).click()
#WebDriverWait(driver, 20).until(EC.element_to_be_clickable((By.XPATH, "//div[@class='btn btn-default']//span[text()='上傳檔案']"))).click()
#WebDriverWait(driver, 20).until(EC.element_to_be_clickable((By.XPATH, "//div[@class='fs-list']//span[text()='上傳檔案']"))).click()

#driver.find_element_by_xpath('/html/body/div[2]/div/div/div/div/div/div/div[2]/div/form/div[5]/div/div/button').click()
#driver.find_element_by_xpath('//*[@id="__button61924bceb5527_1"]').click()
#driver.find_element_by_xpath('//*[@aria-controls="上傳檔案"]').click()

#inputbox = driver.find_element_by_xpath('/html/body')  # 文字輸入處
#inputbox.click()
#time.sleep(2)
#inputbox.send_keys(Keys.ENTER)
#driver.find_element_by_xpath('//*[@value="葉啟源_HW8"]').click()

#WebDriverWait(driver, 5).until(EC.element_to_be_clickable((By.XPATH, "/html"))).click()


#upbt = driver.find_element_by_xpath("//*[@id=__button61923b0c9ec3a_1]/span")



