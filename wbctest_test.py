#from selenium import  webdriver
import selenium.webdriver.common.devtools.v85.css
from selenium.webdriver import Chrome
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from  selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
driver = Chrome(executable_path = 'D:\Chrome\chromedriver_win32\chromedriver.exe') #提供chromedriver路徑

to_FlipClass = 'https://flipclass.stust.edu.tw/'
to_google = 'https://www.google.com/'
driver.get(to_FlipClass)  # 開啟網址
'''search = driver.find_element_by_name("q")
search.send_keys('靈夢')
search.send_keys(Keys.ENTER)'''
login_Account = driver.find_element_by_name("account")  # 找到標籤
login_Account.send_keys("5A8G0001")
login_Password = driver.find_element_by_name("password")  # 找到標籤
login_Password.send_keys("a0973720803")
login_Password.send_keys(Keys.ENTER)
#WebDriverWait(driver, 20).until(EC.element_to_be_clickable((By.XPATH, "//html/body/div[2]/div/div[3]/div[2]/div/div[2]/div/div[3]/div/div/div[2]/div[1]/div[1]/div[1]/div/ul/li[2]/div[3]/div/div[2]/a/span[2]"))).click()


# /course/homework/課程編號(29396) span[text()='作業名稱']
WebDriverWait(driver, 20).until(EC.element_to_be_clickable((By.XPATH, "//div[@class='text']//a[contains(@href, '/course/homework/28386')]/span[text()='作業6：小畫家']"))).click()
#cls.send_keys(Keys.ENTER)
#class_name = driver.find_element_by_name("text")
#print(driver)
#driver.close()//*[@id="xbox-inline"]/div[7]/div/a/span