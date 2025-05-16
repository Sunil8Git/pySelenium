import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By

@pytest.mark.smoke
def test_sort():
    driver = webdriver.Firefox()
    driver.implicitly_wait(5)
    driver.get("https://rahulshettyacademy.com/seleniumPractise/#/offers")

    # Collect all the contents of table to list
    driver.find_element(By.XPATH, "//span[text()='Veg/fruit name']").click()

    # collect all the veggie name
    vegBrowElements = driver.find_elements(By.XPATH, "//tr/td[1]")
    browserSorted = []
    for veg in vegBrowElements:
        browserSorted.append(veg.text)

    # sort and store in local var
    localSortedVeggie = browserSorted.copy()
    browserSorted.sort()

    assert localSortedVeggie == browserSorted
    driver.close()




