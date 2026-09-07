from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


def test_valid_login():
    driver = webdriver.Chrome()
    driver.maximize_window()
    wait = WebDriverWait(driver, 10)

    driver.get("https://www.qapractice.com/practice-login-form")

    try:
        cookie_btn = WebDriverWait(driver, 3).until(
            EC.element_to_be_clickable((By.ID, "cookie-accept"))
        )
        cookie_btn.click()
    except Exception:
        pass

    driver.find_element(By.ID, "login-email").send_keys("user@premiumbank.com")
    driver.find_element(By.ID, "login-password").send_keys("Bank@123")

    login_button = wait.until(
        EC.element_to_be_clickable((By.ID, "login-submit"))
    )
    driver.execute_script("arguments[0].scrollIntoView({block: 'center'});", login_button)

    try:
        login_button.click()
    except Exception:
        driver.execute_script("arguments[0].click();", login_button)

    message = wait.until(
        EC.visibility_of_element_located(
            (By.CSS_SELECTOR, "[data-testid='login-success']")
        )
    ).text

    driver.quit()

    assert "Login Successful" in message, "expected success message"