from selenium import webdriver
from selenium.webdriver.chrome.options import Options
import time
from discord_webhook import DiscordWebhook
from selenium.webdriver.common.action_chains import ActionChains

options = Options()
options.add_experimental_option("debuggerAddress", "127.0.0.1:9014")
options.add_argument(r"user-data-dir=C:\Users\oweno\AppData\Local\Google\Chrome\User Data")
options.add_argument(r"--profile-directory=Profile 2")
driver = webdriver.Chrome(executable_path=r'C:\Program Files (x86)\chromedriver.exe', options=options)
driver.switch_to.window(driver.window_handles[0])

upTrend = \
    driver.find_element_by_xpath\
        ("/html/body/div[2]/div[5]/div/div[1]/div[1]/div[5]/div/div[2]/div[1]/div[4]/div[2]/div[1]/div[2]")



if(upTrend.text != "n/a"):
    print("up")
    webhook = DiscordWebhook(url='https://discord.com/api/webhooks/894755206179479'
                             '624/hvB3HgxpSBkBh8MjlyDN8FRKXJFKkDSSuWVuN719CsfOl'
                             'rO_G4mbPP-yM4RXxnUouoNC', content= "uptrend")
    response = webhook.execute()

downTrend = \
    driver.find_element_by_xpath \
        ("/html/body/div[2]/div[5]/div/div[1]/div[1]/div[5]/div/div[2]/div[1]/div[4]/div[2]/div[2]/div[2]")

if(downTrend.text != "n/a"):
    print("down")

    webhook = DiscordWebhook(url='https://discord.com/api/webhooks/894755206179479'
                             '624/hvB3HgxpSBkBh8MjlyDN8FRKXJFKkDSSuWVuN719CsfOl'
                             'rO_G4mbPP-yM4RXxnUouoNC', content= "downTrend")
    response = webhook.execute()

driver.switch_to.window(driver.window_handles[1])
time.sleep(5)
timer = driver.find_element_by_xpath\
    ("/html/body/div[1]/div[1]/div[2]/div/div[1]/div/div[1]/div[1]/div/div[1]/div[3]/div/div[1]/div/div[1]/div[1]")
print(timer.text)

def get_sec(time_str):
    """Get Seconds from time."""
    m, s = time_str.split(':')
    return int(m) * 60 + int(s)

total = (get_sec(timer.text))
actions = ActionChains(driver)
print(total)
DownDriver = driver.find_elements_by_xpath("//button[contains(string(), 'Enter DOWN')]")[0]
print(DownDriver.text)
UpDriver = driver.find_elements_by_xpath("//button[contains(string(), 'Enter UP')]")[0]
print(UpDriver.text)
if(total < 1000):
    if(upTrend.text != "n/a"):
        UpDriver.click()
    if(downTrend.text != "n/a"):
        DownDriver.click()
driver.switch_to.window(driver.window_handles[0])
