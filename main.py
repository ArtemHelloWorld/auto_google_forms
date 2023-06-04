import os
import pathlib
import random
import time

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By

import settings

base_dir = pathlib.Path(__file__).resolve().parent

service = Service(executable_path=os.path.join(base_dir, 'chromedriver.exe'))

driver = webdriver.Chrome(
    service=service,
    options=webdriver.ChromeOptions()
)
driver.maximize_window()

url = settings.google_form_url
count = settings.answers_count
done = 0

while done < count:
    try:
        driver.get(url=url)
        time.sleep(1)

        questions = driver.find_elements(By.CLASS_NAME, 'Qr7Oae')
        for question in questions:
            answers = question.find_elements(By.CLASS_NAME, 'AB7Lab')
            choice = random.randint(0, len(answers) - 1)
            answers[choice].click()

        submit = driver.find_element(By.XPATH, "//*[text()='Отправить']")
        submit.click()
        done += 1
        print(f'{done}/{count}')

    except Exception as e:
        print(e)
