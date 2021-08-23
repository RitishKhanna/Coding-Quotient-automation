from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains
import time
import getpass
import pyautogui
import pyperclip


dollar = "$" * 99

# User Inputs

print('\n', dollar)


print('')
print('Welcome to Coding Quotient, lazy people!! ^_^')
print(">>If you've reached here I'm assuming you've read the README.md and have the settings configured")
print(">>Please check all the configurations before proceeding as it may cause this program to crash otherwise")
print("Made With ♥ By RITISH KHANNA")
print("Follow Me on Github ----> https://github.com/RitishKhanna")


print('\n', dollar)

username = input('Enter Your Email: ')
password = getpass.getpass(prompt='Enter Your Password:')


# Importing Chrome Driver

driver_path = "./chromedriver.exe"
chrome_options = Options()
driver = webdriver.Chrome(executable_path=driver_path, options=chrome_options)


# Where the Magic happens function


time.sleep(2)
driver.get("https://codequotient.com/login")
time.sleep(2)
driver.find_element_by_id("email").send_keys(username)
time.sleep(2)
driver.find_element_by_id("password").send_keys(password)
time.sleep(2)
driver.find_element_by_id("btnSubmit").click()
time.sleep(2)


driver.maximize_window()

try:
    driver.get("https://codequotient.com/attempt/attempttutorial/60d991baccde02f820596293/5b372a8af8379219939149f9")
    button = driver.find_elements_by_xpath("//a[text()='run']")
    driver.execute_script("arguments[0].click();",button[0])
    time.sleep(2)
except Exception as e:
    print(e)


try:
    driver.execute_script("arguments[0].click();",button[1])
    time.sleep(2)
    driver.get("https://codequotient.com/attempt/attempttutorial/60d991baccde02f820596293/5b372db4f837921993914a10")
    button = driver.find_elements_by_xpath("//a[text()='run']")
    driver.execute_script("arguments[0].click();",button[0])
    time.sleep(2)
    driver.execute_script("arguments[0].click();",button[1])
    time.sleep(2)
except Exception as e:
    print(e)


try:
    driver.get("https://codequotient.com/attempt/attempttutorial/60d991baccde02f820596293/5b3cdc4cf837921993916934")
    button = driver.find_elements_by_xpath("//a[text()='run']")
    driver.execute_script("arguments[0].click();",button[0])
    time.sleep(2)
    driver.execute_script("arguments[0].click();",button[1])
    time.sleep(2)
    driver.execute_script("arguments[0].click();",button[2])
    time.sleep(2)
    driver.execute_script("arguments[0].click();",button[3])
    time.sleep(2)
except Exception as e:
    print(e)


try:
    driver.get("https://codequotient.com/attempt/attempttutorial/60d991baccde02f820596293/5b4c9d2d2a3f026b0f4f0e21")
    button = driver.find_elements_by_xpath("//a[text()='run']")
    driver.execute_script("arguments[0].click();",button[0])
    time.sleep(2)
    driver.execute_script("arguments[0].click();",button[1])
    time.sleep(2)
    driver.execute_script("arguments[0].click();",button[2])
    time.sleep(2)
except Exception as e:
    print(e)


try:
    driver.get("https://codequotient.com/attempt/attempttutorial/60d991baccde02f820596293/5b3cde35f83792199391693e")
    button = driver.find_elements_by_xpath("//a[text()='run']")
    driver.execute_script("arguments[0].click();",button[0])
    time.sleep(2)
    driver.execute_script("arguments[0].click();",button[1])
    time.sleep(2)
except Exception as e:
    print(e)


try:
    driver.get("https://codequotient.com/attempt/attempttutorial/60d991baccde02f820596293/5b4747a734eb16221f491227")
    button = driver.find_elements_by_xpath("//a[text()='run']")
    driver.execute_script("arguments[0].click();",button[0])
    time.sleep(2)
    driver.execute_script("arguments[0].click();",button[1])
    time.sleep(2)
    driver.execute_script("arguments[0].click();",button[2])
    time.sleep(2)
    driver.execute_script("arguments[0].click();",button[3])
    time.sleep(2)
    driver.execute_script("arguments[0].click();",button[4])
    time.sleep(2)
except Exception as e:
    print(e)


try:
    driver.get("https://codequotient.com/attempt/attempttutorial/60d991baccde02f820596293/5b419ab5f837921993917f93")
    button = driver.find_elements_by_xpath("//a[text()='run']")
    driver.execute_script("arguments[0].click();",button[0])
    time.sleep(2)
    driver.execute_script("arguments[0].click();",button[1])
    time.sleep(2)
    driver.execute_script("arguments[0].click();",button[2])
    time.sleep(2)
    driver.execute_script("arguments[0].click();",button[3])
    time.sleep(2)
    driver.execute_script("arguments[0].click();",button[4])
    time.sleep(2)
    driver.execute_script("arguments[0].click();",button[5])
    time.sleep(2)
except Exception as e:
    print(e)


try:
    driver.get("https://codequotient.com/attempt/attempttutorial/60d991baccde02f820596293/5b38c52fc6a1d0259e728e74")
    button = driver.find_elements_by_xpath("//a[text()='run']")
    driver.execute_script("arguments[0].click();",button[0])
    time.sleep(2)
except Exception as e:
    print(e)


try:
    driver.get("https://codequotient.com/attempt/attempttutorial/60d991baccde02f820596293/5b4a01613714c2304e8557ea")
    button = driver.find_elements_by_xpath("//a[text()='run']")
    driver.execute_script("arguments[0].click();",button[0])
    time.sleep(2)
    driver.execute_script("arguments[0].click();",button[1])
    time.sleep(2)
except Exception as e:
    print(e)


try:
    driver.get("https://codequotient.com/attempt/attempttutorial/60d991baccde02f820596293/5a006a24e63d6b7fd5dec29b")
    button = driver.find_elements_by_xpath("//a[text()='run']")
    driver.execute_script("arguments[0].click();",button[0])
    time.sleep(2)
    driver.execute_script("arguments[0].click();",button[1])
    time.sleep(2)
    driver.execute_script("arguments[0].click();",button[2])
    time.sleep(2)
except Exception as e:
    print(e)


try:
    driver.get("https://codequotient.com/attempt/attempttutorial/60d991baccde02f820596293/5a006b92e63d6b7fd5dec2bb")
    button = driver.find_elements_by_xpath("//a[text()='run']")
    driver.execute_script("arguments[0].click();",button[0])
    time.sleep(2)
except Exception as e:
    print(e)

try:
    driver.get("https://codequotient.com/attempt/attempttutorial/60d991baccde02f820596293/5a006a7de63d6b7fd5dec2a6")
    button = driver.find_elements_by_xpath("//a[text()='run']")
    driver.execute_script("arguments[0].click();",button[0])
    time.sleep(2)
    driver.execute_script("arguments[0].click();",button[1])
    time.sleep(2)
except Exception as e:
    print(e)


try:
    driver.get("https://codequotient.com/attempt/attempttutorial/60d991baccde02f820596293/5a006ac5e63d6b7fd5dec2ae")
    button = driver.find_elements_by_xpath("//a[text()='run']")
    driver.execute_script("arguments[0].click();",button[0])
    time.sleep(2)
except Exception as e:
    print(e)


try:
    driver.get("https://codequotient.com/attempt/attempttutorial/60d991baccde02f820596293/5b419e91f837921993917fb1")
    button = driver.find_elements_by_xpath("//a[text()='run']")
    driver.execute_script("arguments[0].click();",button[0])
    time.sleep(2)
    driver.execute_script("arguments[0].click();",button[1])
    time.sleep(2)
    driver.execute_script("arguments[0].click();",button[2])
    time.sleep(2)
    driver.execute_script("arguments[0].click();",button[3])
    time.sleep(2)
    driver.execute_script("arguments[0].click();",button[4])
    time.sleep(2)
except Exception as e:
    print(e)

try:
    driver.get("https://codequotient.com/attempt/attempttutorial/60d991baccde02f820596293/5b3908e9c6a1d0259e728f8f")
    button = driver.find_elements_by_xpath("//a[text()='run']")
    driver.execute_script("arguments[0].click();",button[0])
    time.sleep(2)
    driver.execute_script("arguments[0].click();",button[1])
    time.sleep(2)
except Exception as e:
    print(e)


try:
    driver.get("https://codequotient.com/attempt/attempttutorial/60d991baccde02f820596293/5b38c12dc6a1d0259e728e56")
    button = driver.find_elements_by_xpath("//a[text()='run']")
    driver.execute_script("arguments[0].click();",button[0])
    time.sleep(2)
    driver.execute_script("arguments[0].click();",button[1])
    time.sleep(2)
except Exception as e:
    print(e)


try:
    driver.get("https://codequotient.com/attempt/attempttutorial/60d991baccde02f820596293/5b38c21fc6a1d0259e728e63")
    button = driver.find_elements_by_xpath("//a[text()='run']")
    driver.execute_script("arguments[0].click();",button[0])
    time.sleep(2)
    driver.execute_script("arguments[0].click();",button[1])
    time.sleep(2)
except Exception as e:
    print(e)


try:
    driver.get("https://codequotient.com/attempt/attempttutorial/60d991baccde02f820596293/5b38c902c6a1d0259e728e9b")
    button = driver.find_elements_by_xpath("//a[text()='run']")
    driver.execute_script("arguments[0].click();",button[0])
    time.sleep(2)
    driver.execute_script("arguments[0].click();",button[1])
    time.sleep(2)
    driver.execute_script("arguments[0].click();",button[2])
    time.sleep(2)
    driver.execute_script("arguments[0].click();",button[3])
    time.sleep(2)
    driver.execute_script("arguments[0].click();",button[4])
    time.sleep(2)
except Exception as e:
    print(e)


try:
    driver.get("https://codequotient.com/attempt/attempttutorial/60d991baccde02f820596293/5b38c9aac6a1d0259e728ea9")
    button = driver.find_elements_by_xpath("//a[text()='run']")
    driver.execute_script("arguments[0].click();",button[0])
    time.sleep(2)
except Exception as e:
    print(e) 


try:
    driver.get("https://codequotient.com/attempt/attempttutorial/60d991baccde02f820596293/5a4a420eb1afa55f38fed780")
    time.sleep(2)
    button = driver.find_elements_by_xpath("//a[text()='run']")
    driver.execute_script("arguments[0].click();",button[0])
    time.sleep(2)
    driver.execute_script("arguments[0].click();",button[1])
    time.sleep(2)
    driver.execute_script("arguments[0].click();",button[2])
    time.sleep(2)
except Exception as e:
    print(e)


try:
    driver.get("https://codequotient.com/attempt/attempttutorial/60d991baccde02f820596293/5a12edf146765b2b63e3476b")
    button = driver.find_elements_by_xpath("//a[text()='run']")
    driver.execute_script("arguments[0].click();",button[0])
    time.sleep(2)
    driver.execute_script("arguments[0].click();",button[1])
    time.sleep(2)
except Exception as e:
    print(e)


try:
    driver.get("https://codequotient.com/attempt/attempttutorial/60d991baccde02f820596293/59fde2a0e63d6b7fd5dec004")
    button = driver.find_elements_by_xpath("//a[text()='run']")
    driver.execute_script("arguments[0].click();",button[0])
    time.sleep(2)
    driver.execute_script("arguments[0].click();",button[1])
    time.sleep(4)
except Exception as e:
    print(e)


try:
    driver.get("https://codequotient.com/attempt/attempttutorial/60d991baccde02f820596293/59fde6f5e63d6b7fd5dec01e")
    button = driver.find_elements_by_xpath("//a[text()='run']")
    driver.execute_script("arguments[0].click();",button[0])
    time.sleep(4)
except Exception as e:
    print(e)

try:
    driver.get("https://codequotient.com/attempt/attempttutorial/60d991baccde02f820596293/5a12ef3746765b2b63e3477e")
    button = driver.find_elements_by_xpath("//a[text()='run']")
    driver.execute_script("arguments[0].click();",button[0])
    time.sleep(2)
    driver.execute_script("arguments[0].click();",button[1])
    time.sleep(2)
except Exception as e:
    print(e)

try:
    driver.get("https://codequotient.com/attempt/attempttutorial/60d991baccde02f820596293/5a59dbc1a4af025f554a0bb2")
    button = driver.find_elements_by_xpath("//a[text()='run']")
    driver.execute_script("arguments[0].click();",button[0])
    time.sleep(2)
except Exception as e:
    print(e)

try:
    driver.get("https://codequotient.com/attempt/attempttutorial/60d991baccde02f820596293/5a59dc57a4af025f554a0bbd")
    button = driver.find_elements_by_xpath("//a[text()='run']")
    driver.execute_script("arguments[0].click();",button[0])
    time.sleep(2)
except Exception as e:
    print(e)

try:
    driver.get("https://codequotient.com/attempt/attempttutorial/60d991baccde02f820596293/5a59de12a4af025f554a0bcb")
    button = driver.find_elements_by_xpath("//a[text()='run']")
    driver.execute_script("arguments[0].click();",button[0])
    time.sleep(2)
    driver.execute_script("arguments[0].click();",button[1])
    time.sleep(2)
    driver.execute_script("arguments[0].click();",button[2])
    time.sleep(2)
    driver.execute_script("arguments[0].click();",button[3])
    time.sleep(2)
except Exception as e:
    print(e)

try:
    driver.get("https://codequotient.com/attempt/attempttutorial/60d991baccde02f820596293/5a59dcb5a4af025f554a0bc1")
    button = driver.find_elements_by_xpath("//a[text()='run']")
    driver.execute_script("arguments[0].click();",button[0])
    time.sleep(2)
except Exception as e:
    print(e)

try:
    driver.get("https://codequotient.com/attempt/attempttutorial/60d991baccde02f820596293/5a59df31a4af025f554a0be8")
    button = driver.find_elements_by_xpath("//a[text()='run']")
    driver.execute_script("arguments[0].click();",button[0])
    time.sleep(2)
except Exception as e:
    print(e)

try:
    driver.get("https://codequotient.com/attempt/attempttutorial/60d991baccde02f820596293/5a6342b4e2509a3288171d66")
    button = driver.find_elements_by_xpath("//a[text()='run']")
    driver.execute_script("arguments[0].click();",button[0])
    time.sleep(2)
except Exception as e:
    print(e)

try:
    driver.get("https://codequotient.com/attempt/attempttutorial/60d991baccde02f820596293/5a634522e2509a3288171d76")
    button = driver.find_elements_by_xpath("//a[text()='run']")
    driver.execute_script("arguments[0].click();",button[0])
    time.sleep(2)
except Exception as e:
    print(e)

try:
    driver.get("https://codequotient.com/attempt/attempttutorial/60d991baccde02f820596293/5a634448e2509a3288171d72")
    button = driver.find_elements_by_xpath("//a[text()='run']")
    driver.execute_script("arguments[0].click();",button[0])
    time.sleep(2)
except Exception as e:
    print(e)

try:
    driver.get("https://codequotient.com/attempt/attempttutorial/60d991baccde02f820596293/5a6345c6e2509a3288171d7c")
    button = driver.find_elements_by_xpath("//a[text()='run']")
    driver.execute_script("arguments[0].click();",button[0])
    time.sleep(2)
except Exception as e:
    print(e)

try:
    driver.get("https://codequotient.com/attempt/attempttutorial/60d991baccde02f820596293/5a6346f9e2509a3288171d86")
    button = driver.find_elements_by_xpath("//a[text()='run']")
    driver.execute_script("arguments[0].click();",button[0])
    time.sleep(2)
    driver.execute_script("arguments[0].click();",button[1])
    time.sleep(2)
except Exception as e:
    print(e)

try:
    driver.get("https://codequotient.com/attempt/attempttutorial/60d991baccde02f820596293/5a12f3ec46765b2b63e347fe")
    button = driver.find_elements_by_xpath("//a[text()='run']")
    driver.execute_script("arguments[0].click();",button[0])
    time.sleep(2)
except Exception as e:
    print(e)

try:
    driver.get("https://codequotient.com/attempt/attempttutorial/60d991baccde02f820596293/5a12f48346765b2b63e34805")
    button = driver.find_elements_by_xpath("//a[text()='run']")
    driver.execute_script("arguments[0].click();",button[0])
    time.sleep(2)
except Exception as e:
    print(e)

try:
    driver.get("https://codequotient.com/attempt/attempttutorial/60d991baccde02f820596293/5a706b9c89496f09677d755f")
    button = driver.find_elements_by_xpath("//a[text()='run']")
    driver.execute_script("arguments[0].click();",button[0])
    time.sleep(2)
except Exception as e:
    print(e)

try:
    driver.get("https://codequotient.com/attempt/attempttutorial/60d991baccde02f820596293/5a706cd489496f09677d7578")
    button = driver.find_elements_by_xpath("//a[text()='run']")
    driver.execute_script("arguments[0].click();",button[0])
    time.sleep(2)
except Exception as e:
    print(e)

try:
    driver.get("https://codequotient.com/attempt/attempttutorial/60d991baccde02f820596293/5a706ebd89496f09677d75cd")
    button = driver.find_elements_by_xpath("//a[text()='run']")
    driver.execute_script("arguments[0].click();",button[0])
    time.sleep(2)
except Exception as e:
    print(e)

try:
    driver.get("https://codequotient.com/attempt/attempttutorial/60d991baccde02f820596293/5a563aa5c83e417a5c00dbf3")
    button = driver.find_elements_by_xpath("//a[text()='run']")
    driver.execute_script("arguments[0].click();",button[0])
    time.sleep(2)
except Exception as e:
    print(e)

try:
    driver.get("https://codequotient.com/attempt/attempttutorial/60d991baccde02f820596293/5a563c20c83e417a5c00dc13")
    button = driver.find_elements_by_xpath("//a[text()='run']")
    driver.execute_script("arguments[0].click();",button[0])
    time.sleep(2)
except Exception as e:
    print(e)

try:
    driver.get("https://codequotient.com/attempt/attempttutorial/60d991baccde02f820596293/5a563b1fc83e417a5c00dc06")
    button = driver.find_elements_by_xpath("//a[text()='run']")
    driver.execute_script("arguments[0].click();",button[0])
    time.sleep(2)
except Exception as e:
    print(e)

try:
    driver.get("https://codequotient.com/attempt/attempttutorial/60d991baccde02f820596293/5a634bade2509a3288171dae")
    button = driver.find_elements_by_xpath("//a[text()='run']")
    driver.execute_script("arguments[0].click();",button[0])
    time.sleep(2)
    driver.execute_script("arguments[0].click();",button[1])
    time.sleep(2)
    driver.execute_script("arguments[0].click();",button[2])
    time.sleep(2)
except Exception as e:
    print(e)

try:
    driver.get("https://codequotient.com/attempt/attempttutorial/60d991baccde02f820596293/5a12e7f046765b2b63e34748")
    button = driver.find_elements_by_xpath("//a[text()='run']")
    driver.execute_script("arguments[0].click();",button[0])
    time.sleep(2)
    driver.execute_script("arguments[0].click();",button[1])
    time.sleep(2)
except Exception as e:
    print(e)

try:
    driver.get("https://codequotient.com/attempt/attempttutorial/60d991baccde02f820596293/5a12e94346765b2b63e34754")
    button = driver.find_elements_by_xpath("//a[text()='run']")
    driver.execute_script("arguments[0].click();",button[0])
    time.sleep(2)
except Exception as e:
    print(e)

try:
    driver.get("https://codequotient.com/attempt/attempttutorial/60d991baccde02f820596293/5a12e8a046765b2b63e3474e")
    button = driver.find_elements_by_xpath("//a[text()='run']")
    driver.execute_script("arguments[0].click();",button[0])
    time.sleep(4)
except Exception as e:
    print(e)

try:
    driver.get("https://codequotient.com/attempt/attempttutorial/60d991baccde02f820596293/5a12ec9446765b2b63e34761")
    button = driver.find_elements_by_xpath("//a[text()='run']")
    driver.execute_script("arguments[0].click();",button[0])
    time.sleep(4)
except Exception as e:
    print(e)

try:
    driver.get("https://codequotient.com/attempt/attempttutorial/60d991baccde02f820596293/5a12ea7a46765b2b63e3475a")
    button = driver.find_elements_by_xpath("//a[text()='run']")
    driver.execute_script("arguments[0].click();",button[0])
    time.sleep(4)
except Exception as e:
    print(e)

try:
    driver.get("https://codequotient.com/attempt/attempttutorial/60d991baccde02f820596293/5a76cbeea0bdb04eb16c4867")
    button = driver.find_elements_by_xpath("//a[text()='run']")
    driver.execute_script("arguments[0].click();",button[0])
    time.sleep(2)
except Exception as e:
    print(e)

try:
    driver.get("https://codequotient.com/attempt/attempttutorial/60d991baccde02f820596293/5a76cc84a0bdb04eb16c487d")
    button = driver.find_elements_by_xpath("//a[text()='run']")
    driver.execute_script("arguments[0].click();",button[0])
    time.sleep(2)
except Exception as e:
    print(e)

try:
    driver.get("https://codequotient.com/attempt/attempttutorial/60d991baccde02f820596293/5a76e2f2a0bdb04eb16c4970")
    button = driver.find_elements_by_xpath("//a[text()='run']")
    driver.execute_script("arguments[0].click();",button[0])
    time.sleep(2)
except Exception as e:
    print(e)

try:
    driver.get("https://codequotient.com/attempt/attempttutorial/60d991baccde02f820596293/5a76e46fa0bdb04eb16c4985")
    button = driver.find_elements_by_xpath("//a[text()='run']")
    driver.execute_script("arguments[0].click();",button[0])
    time.sleep(2)
    driver.execute_script("arguments[0].click();",button[1])
    time.sleep(2)
    driver.execute_script("arguments[0].click();",button[2])
    time.sleep(2)
except Exception as e:
    print(e)

try:
    driver.get("https://codequotient.com/attempt/attempttutorial/60d991baccde02f820596293/5a76e6cca0bdb04eb16c49b9")
    button = driver.find_elements_by_xpath("//a[text()='run']")
    driver.execute_script("arguments[0].click();",button[0])
    time.sleep(2)
    driver.execute_script("arguments[0].click();",button[1])
    time.sleep(2)
except Exception as e:
    print(e)

try:
    driver.get("https://codequotient.com/attempt/attempttutorial/60d991baccde02f820596293/5a76e7f7a0bdb04eb16c49e5")
    button = driver.find_elements_by_xpath("//a[text()='run']")
    driver.execute_script("arguments[0].click();",button[0])
    time.sleep(2)
except Exception as e:
    print(e)

try:
    driver.get("https://codequotient.com/attempt/attempttutorial/60d991baccde02f820596293/5a76e775a0bdb04eb16c49d8")
    button = driver.find_elements_by_xpath("//a[text()='run']")
    driver.execute_script("arguments[0].click();",button[0])
    time.sleep(2)
except Exception as e:
    print(e)

try:
    driver.get("https://codequotient.com/attempt/attempttutorial/60d991baccde02f820596293/5a7dc61ad287a634f8535f39")
    button = driver.find_elements_by_xpath("//a[text()='run']")
    driver.execute_script("arguments[0].click();",button[0])
    time.sleep(2)
except Exception as e:
    print(e)

try:
    driver.get("https://codequotient.com/attempt/attempttutorial/60d991baccde02f820596293/5a7ece1fd287a634f85367fd")
    button = driver.find_elements_by_xpath("//a[text()='run']")
    driver.execute_script("arguments[0].click();",button[0])
    time.sleep(2)
    driver.execute_script("arguments[0].click();",button[1])
    time.sleep(2)
except Exception as e:
    print(e)

try:
    driver.get("https://codequotient.com/attempt/attempttutorial/60d991baccde02f820596293/5a7eced4d287a634f8536807")
    button = driver.find_elements_by_xpath("//a[text()='run']")
    driver.execute_script("arguments[0].click();",button[0])
    time.sleep(2)
except Exception as e:
    print(e)

try:
    driver.get("https://codequotient.com/attempt/attempttutorial/60d991baccde02f820596293/5a7ecfd2d287a634f853680d")
    button = driver.find_elements_by_xpath("//a[text()='run']")
    driver.execute_script("arguments[0].click();",button[0])
    time.sleep(2)
except Exception as e:
    print(e)

try:
    driver.get("https://codequotient.com/attempt/attempttutorial/60d991baccde02f820596293/6086873424ca04b987c99446")
    button = driver.find_elements_by_xpath("//a[text()='run']")
    driver.execute_script("arguments[0].click();",button[0])
    time.sleep(2)
    driver.execute_script("arguments[0].click();",button[1])
    time.sleep(2)
except Exception as e:
    print(e)

try:
    driver.get("https://codequotient.com/attempt/attempttutorial/60d991baccde02f820596293/6086713324ca04b987c9940f")
    button = driver.find_elements_by_xpath("//a[text()='run']")
    driver.execute_script("arguments[0].click();",button[0])
    time.sleep(2)
except Exception as e:
    print(e)

try:
    driver.get("https://codequotient.com/attempt/attempttutorial/60d991baccde02f820596293/60868c7f24ca04b987c9947f")
    button = driver.find_elements_by_xpath("//a[text()='run']")
    driver.execute_script("arguments[0].click();",button[0])
    time.sleep(2)
except Exception as e:
    print(e)

try:
    driver.get("https://codequotient.com/attempt/attempttutorial/60d991baccde02f820596293/60dc6fa7ccde02f8205964c8")
    button = driver.find_elements_by_xpath("//a[text()='run']")
    driver.execute_script("arguments[0].click();",button[0])
    time.sleep(2)
except Exception as e:
    print(e)