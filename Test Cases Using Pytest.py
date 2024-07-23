import pytest
from selenium import webdriver

import ImdbSearchPage

@pytest.fixture(scope="module")
def setup():
    driver = webdriver.Chrome()
    driver.get("https://www.imdb.com/search/name/")
    yield driver
    driver.quit()

def test_imdb_search(setup):
    driver = setup
    search_page = ImdbSearchPage(driver)
    
    # Example data for the search
    name = "Tom Hanks"
    birth_month = "July"
    birth_year = "1956"
    death_month = "December"
    death_year = "2023"
    gender = "Male"

    # Fill in the form
    search_page.enter_name(name)
    search_page.select_birth_month(birth_month)
    search_page.enter_birth_year(birth_year)
    search_page.select_death_month(death_month)
    search_page.enter_death_year(death_year)
    search_page.select_gender(gender)
    
    # Perform the search
    search_page.click_search()

    # Verify the results page (this is just an example, you might need a different check)
    assert "Name Matching" in driver.title

