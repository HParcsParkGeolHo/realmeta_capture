import pyautogui
import keyboard
import requests
import time
import threading
from selenium import webdriver
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By

from optparse import OptionParser
from selenium import webdriver
import selenium.webdriver.chrome.service as Service
from selenium.webdriver.chrome.options import Options

import os
from datetime import datetime


def main():
    now = datetime.now()
    while True:
        date_diff = datetime.now() - now
        file_name = datetime.now()
        if date_diff.seconds > 1200:
            print(file_name.strftime("%m%d%H%M%S"))
            print('start')
            chrome_path = os.path.join(os.path.dirname(os.path.realpath(__file__)), 'chromedriver')
            service = Service.Service(chrome_path)
            service.start()

            chrome_options = Options()
            chrome_options.add_argument("--start-maximized")
            desired_capabilities = chrome_options.to_capabilities()
            desired_capabilities['pageLoadStrategy'] = 'none'
            driver = webdriver.Remote(service.service_url, desired_capabilities=desired_capabilities)
            WebDriverWait(driver, 3)
            driver.get('http://noitacifiton-socip.humax-parcs.com:8181/stream/B2F')
            time.sleep(3)
            driver.execute_script("window.stop();")
            driver.save_screenshot('./images/' + file_name.strftime("%m%d%H%M%S") + '_B2F.png')
            driver.quit()
            src = './images/' + file_name.strftime("%m%d%H%M%S") + '_B2F.png'
            print('create : ' + src)

            url = 'http://noitacifiton-socip.humax-parcs.com:8079/v1/camera/B2F.CAM.000?org=0'
            response = requests.get(url, stream=True)
            if response.status_code == 200:
                with open('./images/' + file_name.strftime("%m%d%H%M%S") + '_cam0.jpg', 'wb') as f:
                    f.write(response.content)
                src = './images/' + file_name.strftime("%m%d%H%M%S") + '_cam0.jpg'
                print('create : ' + src)
            else:
                src = './images/' + file_name.strftime("%m%d%H%M%S") + '_cam0.jpg'
                print('error! : ' + src)


            url = 'http://noitacifiton-socip.humax-parcs.com:8079/v1/camera/B2F.CAM.001?org=0'
            response = requests.get(url, stream=True)
            if response.status_code == 200:
                with open('./images/' + file_name.strftime("%m%d%H%M%S") + '_cam1.jpg', 'wb') as f:
                    f.write(response.content)
                src = './images/' + file_name.strftime("%m%d%H%M%S") + '_cam1.jpg'
                print('create : ' + src)
            else:
                src = './images/' + file_name.strftime("%m%d%H%M%S") + '_cam1.jpg'
                print('error! : ' + src)

            url = 'http://noitacifiton-socip.humax-parcs.com:8079/v1/camera/B2F.CAM.002?org=0'
            response = requests.get(url, stream=True)
            if response.status_code == 200:
                with open('./images/' + file_name.strftime("%m%d%H%M%S") + '_cam2.jpg', 'wb') as f:
                    f.write(response.content)
                src = './images/' + file_name.strftime("%m%d%H%M%S") + '_cam2.jpg'
                print('create : ' + src)
            else:
                src = './images/' + file_name.strftime("%m%d%H%M%S") + '_cam2.jpg'
                print('error! : ' + src)

            url = 'http://noitacifiton-socip.humax-parcs.com:8079/v1/camera/B2F.CAM.003?org=0'
            response = requests.get(url, stream=True)
            if response.status_code == 200:
                with open('./images/' + file_name.strftime("%m%d%H%M%S") + '_cam3.jpg', 'wb') as f:
                    f.write(response.content)
                src = './images/' + file_name.strftime("%m%d%H%M%S") + '_cam3.jpg'
                print('create : ' + src)
            else:
                src = './images/' + file_name.strftime("%m%d%H%M%S") + '_cam3.jpg'
                print('error! : ' + src)

            url = 'http://noitacifiton-socip.humax-parcs.com:8079/v1/camera/B2F.CAM.004?org=0'
            response = requests.get(url, stream=True)
            if response.status_code == 200:
                with open('./images/' + file_name.strftime("%m%d%H%M%S") + '_cam4.jpg', 'wb') as f:
                    f.write(response.content)
                src = './images/' + file_name.strftime("%m%d%H%M%S") + '_cam4.jpg'
                print('create : ' + src)
            else:
                src = './images/' + file_name.strftime("%m%d%H%M%S") + '_cam4.jpg'
                print('error! : ' + src)

            url = 'http://noitacifiton-socip.humax-parcs.com:8079/v1/camera/B2F.CAM.005?org=0'
            response = requests.get(url, stream=True)
            if response.status_code == 200:
                with open('./images/' + file_name.strftime("%m%d%H%M%S") + '_cam5.jpg', 'wb') as f:
                    f.write(response.content)
                src = './images/' + file_name.strftime("%m%d%H%M%S") + '_cam5.jpg'
                print('create : ' + src)
            else:
                src = './images/' + file_name.strftime("%m%d%H%M%S") + '_cam5.jpg'
                print('error! : ' + src)

            url = 'http://noitacifiton-socip.humax-parcs.com:8079/v1/camera/B2F.CAM.006?org=0'
            response = requests.get(url, stream=True)
            if response.status_code == 200:
                with open('./images/' + file_name.strftime("%m%d%H%M%S") + '_cam6.jpg', 'wb') as f:
                    f.write(response.content)
                src = './images/' + file_name.strftime("%m%d%H%M%S") + '_cam6.jpg'
                print('create : ' + src)
            else:
                src = './images/' + file_name.strftime("%m%d%H%M%S") + '_cam6.jpg'
                print('error! : ' + src)

            url = 'http://noitacifiton-socip.humax-parcs.com:8079/v1/camera/B2F.CAM.007?org=0'
            response = requests.get(url, stream=True)
            if response.status_code == 200:
                with open('./images/' + file_name.strftime("%m%d%H%M%S") + '_cam7.jpg', 'wb') as f:
                    f.write(response.content)
                src = './images/' + file_name.strftime("%m%d%H%M%S") + '_cam7.jpg'
                print('create : ' + src)
            else:
                src = './images/' + file_name.strftime("%m%d%H%M%S") + '_cam7.jpg'
                print('error! : ' + src)

            url = 'http://noitacifiton-socip.humax-parcs.com:8079/v1/camera/B2F.CAM.008?org=0'
            response = requests.get(url, stream=True)
            if response.status_code == 200:
                with open('./images/' + file_name.strftime("%m%d%H%M%S") + '_cam8.jpg', 'wb') as f:
                    f.write(response.content)
                src = './images/' + file_name.strftime("%m%d%H%M%S") + '_cam8.jpg'
                print('create : ' + src)
            else:
                src = './images/' + file_name.strftime("%m%d%H%M%S") + '_cam8.jpg'
                print('error! : ' + src)

            print("end : " + file_name.strftime("%m%d%H%M%S"))
            now = datetime.now()
            print("wait")


if __name__ == '__main__':
    main()
