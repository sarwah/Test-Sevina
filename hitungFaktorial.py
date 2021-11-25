from config import *
import time as t
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC


driver = webdriver.Chrome(lokasi_chrome_diver)
driver.maximize_window()

def hitungFaktorialInputInteger():
    print("TC : Perhitungan Faktorial dengan menginputkan integer \n")
    input = 3
    faktorial = 1

    for i in range(1, input + 1):
        faktorial *= i

    try:
        driver.get(target_server)
        t.sleep(3)
        driver.find_element_by_id("input").send_keys(input)
        WebDriverWait(driver, 20).until(EC.element_to_be_clickable((By.XPATH,"//button[@id='hitung']"))).click()
        t.sleep(3)
        assert f'Faktorial dari {input} adalah: {faktorial}' in driver.find_element_by_id("result").text
        t.sleep(3)
    except Exception as e:
        print(e)
        return("Result: Gagal \n")
    else:
        return("Result :Sukses \n")

def hitungFaktorialInputChar():
    print("TC : Perhitungan Faktorial dengan menginputkan char \n")
    input = 'a'

    try:
        driver.get(target_server)
        t.sleep(3)
        driver.find_element_by_id("input").send_keys(input)
        WebDriverWait(driver, 20).until(EC.element_to_be_clickable((By.XPATH,"//button[@id='hitung']"))).click()
        t.sleep(3)
        assert 'Please enter an integer' in driver.find_element_by_id("result").text
        t.sleep(3)
    except Exception as e:
        print(e)
        return("Result: Gagal \n")
    else:
        return("Result: Sukses \n")

def hitungFaktorialTanpaInputField():
    print("TC : Perhitungan Faktorial tanpa menginputkan field \n")

    try:
        driver.get(target_server)
        t.sleep(3)
        WebDriverWait(driver, 20).until(EC.element_to_be_clickable((By.XPATH,"//button[@id='hitung']"))).click()
        t.sleep(3)
        assert 'Please enter an integer' in driver.find_element_by_id("result").text
        t.sleep(3)
    except Exception as e:
        print(e)
        return("Result: Gagal \n")
    else:
        return("Result: Sukses \n")

def hitungFaktorialInputInteger4Digit():
    print("TC : Perhitungan Faktorial dengan menginputkan 4 digit integer \n")
    input = 1000
    faktorial = 1

    for i in range(1, input + 1):
        faktorial *= i

    try:
        driver.get(target_server)
        t.sleep(3)
        driver.find_element_by_id("input").send_keys(input)
        WebDriverWait(driver, 20).until(EC.element_to_be_clickable((By.XPATH,"//button[@id='hitung']"))).click()
        t.sleep(3)
        assert f'Faktorial dari {input} adalah: {faktorial}' in driver.find_element_by_id("result").text
        t.sleep(3)
    except Exception as e:
        print(e)
        return("Result: Gagal \n")
    else:
        return("Result: Sukses \n")

if __name__=="__main__":
    print(hitungFaktorialInputInteger())
    print(hitungFaktorialInputChar())
    print(hitungFaktorialTanpaInputField())
    print(hitungFaktorialInputInteger4Digit())
    driver.quit()