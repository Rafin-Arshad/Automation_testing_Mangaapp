import selenium
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time

# Initialize WebDriver
driver = webdriver.Chrome()

# Open the application
'driver.get("https://myalice-automation-test.netlify.app")'


# store name and password and login url
username = "testuser"
password = "password"
login_url = "https://myalice-automation-test.netlify.app"
driver.get(login_url)
driver.maximize_window()


#find element of username and password
username_field = driver.find_element(By.ID, value="username")
password_field = driver.find_element(By.ID, value="password")

#send the keys
username_field.send_keys(username)
password_field.send_keys(password)

#try to login

login_button = driver.find_element(By.ID, "login-btn")
assert not login_button.get_attribute("disabled")
login_button.click()
time.sleep(200)

search_terms = ["Naruto", "One Piece", "Seven Deadly Sins", "No manga found"]
for term in search_terms:
    search_box = driver.find_element(By.ID, "manga-search")
    search_box.clear()
    search_box.send_keys(term)
    search_box.send_keys(Keys.RETURN)

    time.sleep(20)  # Wait for search results

    if term == "No manga found":
        assert "No manga found" in driver.page_source
    else:
        assert term in driver.page_source

driver.quit()
