from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import Select
from selenium import webdriver

class ImdbSearchPage:
    def __init__(self, driver):
        self.driver = driver
        self.name_input = (By.ID, "name")
        self.birth_month_select = (By.ID, "birth_month")
        self.birth_year_input = (By.ID, "birth_year")
        self.death_month_select = (By.ID, "death_month")
        self.death_year_input = (By.ID, "death_year")
        self.gender_select = (By.ID, "gender")
        self.search_button = (By.XPATH, "//button[@type='submit']")

    def enter_name(self, name):
        WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located(self.name_input)).send_keys(name)

    def select_birth_month(self, month):
        select = Select(WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable(self.birth_month_select)))
        select.select_by_visible_text(month)

    def enter_birth_year(self, year):
        WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located(self.birth_year_input)).send_keys(year)

    def select_death_month(self, month):
        select = Select(WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable(self.death_month_select)))
        select.select_by_visible_text(month)

    def enter_death_year(self, year):
        WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located(self.death_year_input)).send_keys(year)

    def select_gender(self, gender):
        select = Select(WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable(self.gender_select)))
        select.select_by_visible_text(gender)

    def click_search(self):
        WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable(self.search_button)).click()
