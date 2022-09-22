from selenium import webdriver
from selenium.webdriver.common.by import By
from time import sleep
import pytest

def test_first():
    driver = webdriver.Chrome('C:\\chromedriver\\chromedriver')
    driver.get("http://www.google.com")
    sleep(5)

    driver.close()


def test_second():
    sleep(5)
    assert True

def test_third():
    sleep(7)
    assert False

def test_fourth():
    sleep(15)
    assert True

def test_five():
    sleep(25)
    assert False

def test_sixth():
    sleep(15)
    assert False


#driver = webdriver.Chrome('C:\\chromedriver\\chromedriver')
#driver.get("http://www.google.com")