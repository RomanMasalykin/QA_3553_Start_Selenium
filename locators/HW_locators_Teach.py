from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()

try:
    driver.get("https://telranedu.web.app/login")
#By tag name
    div = driver.find_element(By.TAG_NAME, "div")
    div_1 = driver.find_element(By.CSS_SELECTOR, "div")
    div_xPath = driver.find_element(By.XPATH, "//div")

    h1 = driver.find_element(By.TAG_NAME, "h1")
    h1_1 = driver.find_element(By.CSS_SELECTOR, "h1")
    h1_xPath = driver.find_element(By.XPATH, "//h1")

    input = driver.find_element(By.TAG_NAME, "input")
    input_1 = driver.find_element(By.CSS_SELECTOR, "input")
    input_xPath = driver.find_element(By.XPATH, "//input")

    a_list = driver.find_elements(By.TAG_NAME, "a")
    a_list_1 = driver.find_elements(By.CSS_SELECTOR, "a")
    print(len(a_list))
    a_list_xPath = driver.find_element(By.XPATH, "//a")
#By class
    container = driver.find_element(By.CLASS_NAME, "container")
    container_1 = driver.find_element(By.CSS_SELECTOR, ".container")
    container_xPath = driver.find_element(By.XPATH, "//*[@class = 'container']")

    navbar = driver.find_element(By.CLASS_NAME, "navbar-component_nav__1X_4m")
    navbar_1 = driver.find_element(By.CSS_SELECTOR, ".navbar-component_nav__1X_4m")
    nabvar_xPath = driver.find_element(By.XPATH, "//*[@class = 'container']")

    login_login = driver.find_element(By.CLASS_NAME, "login_login__3EHKB")
    login_login_1 = driver.find_element(By.CSS_SELECTOR, ".login_login__3EHKB")
    login_login_xPath = driver.find_element(By.XPATH, "//*[@class = 'login_login__3EHKB']")
#By ID
    root = driver.find_element(By.ID, "root")
    root_1 = driver.find_element(By.CSS_SELECTOR, "#root")
    root_xPath = driver.find_element(By.XPATH, "//*[@id = 'root']")
#By attribute
    home = driver.find_element(By.CSS_SELECTOR, "[href = '/home']")
    home_xPath = driver.find_element(By.XPATH, "//*[@href = '/home']")
#by Link_text
    about = driver.find_element(By.LINK_TEXT, "ABOUT")
    about_1 = driver.find_element(By.PARTIAL_LINK_TEXT, "BOU")

#PHONEBOOK
    phonebook = driver.find_element(By.CSS_SELECTOR, "h1")
    phonebook_1 = driver.find_element(By.CSS_SELECTOR, "#root > div > h1:first-child")
    phonebook_xPath = driver.find_element(By.XPATH, "//*[text() = 'PHONEBOOK']")
finally:
    driver.quit()