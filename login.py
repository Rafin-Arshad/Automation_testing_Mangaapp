from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
# Initialize WebDriver
driver = webdriver.Chrome()

try:
    # Navigate to the website and log in
    driver.get("https://myalice-automation-test.netlify.app")
    wait = WebDriverWait(driver, 1000)

    # Assuming login is required first
    username = driver.find_element(By.ID, "username")
    password = driver.find_element(By.ID, "password")
    username.send_keys("testuser")
    password.send_keys("password")
    login_button = driver.find_element(By.ID, "login-btn")
    assert not login_button.get_attribute("disabled")
    login_button.click()
    time.sleep(200)

    # Wait until manga search page loads
    wait.until(EC.presence_of_element_located((By.ID, "manga-search")))


    def search_and_verify(term, expected_result):
        search_box = driver.find_element(By.ID, "manga-search")
        search_box.clear()
        search_box.send_keys(term)
        search_button = driver.find_element(By.CLASS_NAME, "bg-green-500 text-white py-2 px-4 rounded mr-2")
        search_button.click()

        # Verify results
        wait.until(EC.presence_of_element_located((By.ID, "manga-name")))
        manga_cards = driver.find_elements(By.ID, "manga-name")

        if expected_result == "No manga found":
            assert "No manga found" in driver.page_source, f"Expected 'No manga found' message, but it wasn't found."
        else:
            assert any(expected_result in card.text for card in
                       manga_cards), f"Expected '{expected_result}' but it wasn't found."


    # Perform searches and verifications
    search_and_verify("Naruto", "Naruto")
    search_and_verify("One Piece", "One Piece")
    search_and_verify("Seven Deadly Sins", "Seven Deadly Sins")
    search_and_verify("No manga found", "No manga found")

finally:
    # Close the browser
    driver.quit()
