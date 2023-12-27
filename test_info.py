# Generated by Selenium IDE
import pytest
import time
import json
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities

class TestInfo():
  def setup_method(self, method):
    self.driver = webdriver.Chrome()
    self.vars = {}
  
  def teardown_method(self, method):
    self.driver.quit()
  
  def test_info(self):
    self.driver.get("https://www.saucedemo.com/")
    self.driver.set_window_size(1920, 1201)
    WebDriverWait(self.driver, 5).until(expected_conditions.visibility_of_element_located((By.ID, "user-name")))
    self.driver.find_element(By.ID, "user-name").send_keys("standard_user")
    WebDriverWait(self.driver, 5).until(expected_conditions.visibility_of_element_located((By.ID, "password")))
    self.driver.find_element(By.ID, "password").send_keys("secret_sauce")
    self.driver.find_element(By.ID, "login-button").click()
    self.driver.find_element(By.ID, "add-to-cart-sauce-labs-backpack").click()
    assert self.driver.find_element(By.XPATH, "//*[@id=\'remove-sauce-labs-backpack\']").text == "Remove"
    self.driver.find_element(By.XPATH, "//div[@id=\'shopping_cart_container\']/a/span").click()
    self.driver.find_element(By.ID, "checkout").click()
    self.driver.find_element(By.ID, "first-name").click()
    self.driver.find_element(By.ID, "first-name").send_keys("bürde")
    self.driver.find_element(By.ID, "last-name").click()
    self.driver.find_element(By.ID, "last-name").send_keys("kesikbaş")
    self.driver.find_element(By.ID, "continue").click()
    assert self.driver.find_element(By.XPATH, "//div[@id=\'checkout_info_container\']/div/form/div/div[4]/h3").text == "Error: Postal Code is required"
    self.driver.close()
  