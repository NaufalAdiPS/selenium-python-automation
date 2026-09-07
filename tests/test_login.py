import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


def dismiss_cookie_banner(driver):
    try:
        cookie_btn = WebDriverWait(driver, 3).until(
            EC.element_to_be_clickable((By.ID, "cookie-accept"))
        )
        cookie_btn.click()
    except Exception:
        pass


def do_login(driver, wait, email, password):
    driver.find_element(By.ID, "login-email").send_keys(email)
    driver.find_element(By.ID, "login-password").send_keys(password)

    login_button = wait.until(EC.element_to_be_clickable((By.ID, "login-submit")))
    driver.execute_script("arguments[0].scrollIntoView({block: 'center'});", login_button)
    try:
        login_button.click()
    except Exception:
        driver.execute_script("arguments[0].click();", login_button)


def test_valid_login():
    driver = webdriver.Chrome()
    driver.maximize_window()
    wait = WebDriverWait(driver, 10)

    driver.get("https://www.qapractice.com/practice-login-form")
    dismiss_cookie_banner(driver)
    do_login(driver, wait, "user@premiumbank.com", "Bank@123")

    message = wait.until(
        EC.visibility_of_element_located((By.CSS_SELECTOR, "[data-testid='login-success']"))
    ).text
    driver.quit()

    assert "Login Successful! Welcome to Premium Banking." in message


def test_invalid_credentials():
    """TC05: wrong email + wrong password -> error, no success."""
    driver = webdriver.Chrome()
    driver.maximize_window()
    wait = WebDriverWait(driver, 10)

    driver.get("https://www.qapractice.com/practice-login-form")
    dismiss_cookie_banner(driver)
    do_login(driver, wait, "wrong@example.com", "wrongpassword")

    error = wait.until(
        EC.visibility_of_element_located((By.CSS_SELECTOR, "[data-testid='login-error']"))
    ).text
    driver.quit()

    assert "Invalid email id and password" in error

@pytest.mark.parametrize(
    "email, password, expected_error",
    [
        ("", "", "Email and Password are required"),       # TC02
        ("user@premiumbank.com", "", "Password is required"),  # TC03
        ("", "Bank@123", "Email is required"),              # TC04
    ],
)
def test_missing_fields(email, password, expected_error):
    driver = webdriver.Chrome()
    driver.maximize_window()
    wait = WebDriverWait(driver, 10)

    driver.get("https://www.qapractice.com/practice-login-form")
    dismiss_cookie_banner(driver)
    do_login(driver, wait, email, password)

    error = wait.until(
        EC.visibility_of_element_located((By.CSS_SELECTOR, "[data-testid='login-error']"))
    ).text
    driver.quit()

    assert expected_error in error


def test_forgot_password_navigation(): #TC07
    driver = webdriver.Chrome()
    driver.maximize_window()
    wait = WebDriverWait(driver, 10)

    driver.get("https://www.qapractice.com/practice-login-form")
    dismiss_cookie_banner(driver)

    forgot_password_link = wait.until(
        EC.element_to_be_clickable((By.ID, "login-forgot-password"))
    )
    driver.execute_script("arguments[0].scrollIntoView({block: 'center'});", forgot_password_link)

    try:
        forgot_password_link.click()
    except Exception:
        driver.execute_script("arguments[0].click();", forgot_password_link)

    wait.until(EC.url_contains("/forget-password"))

    current_url = driver.current_url
    driver.quit()

    assert "/forget-password" in current_url