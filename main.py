import splinter.driver.webdriver.chrome
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
import time
from discord_webhook import DiscordWebhook
import pyautogui
from selenium.common.exceptions import NoSuchElementException
from selenium.common.exceptions import StaleElementReferenceException
from pynput.mouse import Button, Controller

def findtrend():
    i = 1
    while i < 2:
        options = Options()
        options.add_experimental_option("debuggerAddress", "127.0.0.1:9014")
        options.add_argument(r"user-data-dir=C:\Users\oweno\AppData\Local\Google\Chrome\User Data")
        options.add_argument(r"--profile-directory=Profile 2")
        driver = webdriver.Chrome(executable_path=r'C:\Program Files (x86)\chromedriver.exe', options=options)
        driver.switch_to.window(driver.window_handles[0])
        mouse = Controller()
        pyautogui.size()  # current screen resolution width and height
        (1920, 1080)
        upTrend = \
            driver.find_element_by_xpath \
                ("/html/body/div[2]/div[5]/div/div[1]/div[1]/div[5]/div/div[2]/div[1]/div[4]/div[2]/div[1]/div[2]")

        downTrend = \
            driver.find_element_by_xpath \
                ("/html/body/div[2]/div[5]/div/div[1]/div[1]/div[5]/div/div[2]/div[1]/div[4]/div[2]/div[2]/div[2]")

        if(upTrend.text != "n/a"):
            print("up")




        if(downTrend.text != "n/a"):
            print("down")




        driver.switch_to.window(driver.window_handles[1])

        time.sleep(1)

        timer = driver.find_element_by_xpath\
            ("/html/body/div[1]/div[1]/div[2]/div/div[1]/div/div[1]/div[1]/div/div[1]/div[3]/div/div[1]/div/div[1]/div[1]")
        print(timer.text)

        def get_sec(time_str):
            """Get Seconds from time."""
            m, s = time_str.split(':')
            return int(m) * 60 + int(s)

        total = (get_sec(timer.text))

        if(total < 1000):
            pyautogui.moveTo(952, 407)
            mouse.click(Button.left, 1)
            if(downTrend.text != "n/a"):
                pyautogui.moveTo(297, 710)
                mouse.click(Button.left, 1)
            if (upTrend.text != "n/a"):
                pyautogui.moveTo(1278, 74)
                mouse.click(Button.left, 1)
        print(total)
        driver.switch_to.window(driver.window_handles[0])
        time.sleep(5)




if __name__ == '__main__':
    findtrend()

