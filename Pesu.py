from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import pickle
import signal
import sys
import time

# Set Variables Here
cookies_file = "cookies.pkl"  # File to save/load cookies
myuser = "your_username"      # Replace with your username
mypwd = "your_password"       # Replace with your password

def init_website():
    global browser
    service = ChromeService(executable_path=ChromeDriverManager().install())
    browser = webdriver.Chrome(service=service)
    browser.maximize_window()
    browser.get("https://www.usvisascheduling.com/en-US/")

def save_cookies():
    """Save cookies after login."""
    with open(cookies_file, 'wb') as file:
        pickle.dump(browser.get_cookies(), file)
    print("Cookies saved.")

def load_cookies():
    """Load cookies from a file and add them to the browser."""
    try:
        with open(cookies_file, 'rb') as file:
            cookies = pickle.load(file)
            # Add a delay to ensure the page is fully loaded
            time.sleep(5)
            for cookie in cookies:
                # Ensure cookie has necessary fields
                if 'name' in cookie and 'value' in cookie and 'domain' in cookie:
                    # Remove leading dot from domain names if necessary
                    if cookie['domain'].startswith('.'):
                        cookie['domain'] = cookie['domain'][1:]
                    # Add the cookie to the browser
                    browser.add_cookie(cookie)
            print("Cookies loaded.")
    except FileNotFoundError:
        print("No cookies file found. Please log in.")

def update_application_cookie(new_value):
    """Update the .AspNet.ApplicationCookie value and clean up domain names in the browser."""
    existing_cookies = browser.get_cookies()
    cookies_to_update = []

    # Remove leading dot from domain names and collect cookies to update
    for cookie in existing_cookies:
        if cookie['name'] == '.AspNet.ApplicationCookie':
            # Prepare the cookie for update
            if 'domain' in cookie and cookie['domain'].startswith('.'):
                cookie['domain'] = cookie['domain'][1:]  # Remove leading dot
            cookie['value'] = new_value
            cookies_to_update.append(cookie)

    # Delete existing cookies with the same name
    for cookie in existing_cookies:
        if cookie['name'] == '.AspNet.ApplicationCookie':
            browser.delete_cookie(cookie['name'])

    # Add updated cookies
    for cookie in cookies_to_update:
        browser.add_cookie(cookie)
        print(f"Updated .AspNet.ApplicationCookie with new value: {new_value}")

    if not cookies_to_update:
        print(".AspNet.ApplicationCookie not found in existing cookies.")

def login():
    """Perform login and save cookies."""
    try:
        # Replace these selectors with the actual ones from your page
        WebDriverWait(browser, 10).until(EC.visibility_of_element_located((By.CSS_SELECTOR, "#j_scriptusername"))).send_keys(myuser)
        WebDriverWait(browser, 10).until(EC.visibility_of_element_located((By.CSS_SELECTOR, "#password"))).send_keys(mypwd)
        WebDriverWait(browser, 10).until(EC.element_to_be_clickable((By.CSS_SELECTOR, "#loginButton"))).click()
        save_cookies()  # Save cookies after login
    except Exception as e:
        print(f"Login failed: {e}")

def signal_handler(signal, frame):
    print('Closing browser...')
    browser.quit()
    sys.exit(0)

signal.signal(signal.SIGINT, signal_handler)

# Main process
init_website()

# Allow some time for the page to load
time.sleep(5)

load_cookies()  # Load cookies before applying them

# Apply cookies and refresh the page
browser.get("https://www.usvisascheduling.com/en-US/")  # Reload page to apply cookies

# Uncomment the following line if you need to update the .AspNet.ApplicationCookie
# update_application_cookie('CB1Y-8QyrWmBlMRoD-lT4kQAr57dPrAYNKzrLB_OZLI21LzGWir9l327UDoZjlRYJsV_xWPdc9WTggdth24RTSPGxZ-kQ5TorwSMBo8YF-0CwEdKlfv3YD2cnmI4PblpP_ezj-2lMmq80PWMW1jvK3-vTh7GtHHoEzga5GmlPlB7AQheELltNpxK1oBrVKZHI9FzRaBof_bmDhZ1SMnEdVnwyLm4MmNLsBqKWPrCqOUSNfEpYjJpvo4YUrtnEr1VmlD0ApHhS4FonJKO9qEpELE9915MafEXAhPx_XR_eeEQsDoPLQckgsZrzVyOg8-Pn4FfJ5cXsnwo6d3D9tTvkzBHU30U94RV9pekspkb3oAmWWsTgt91xU4xSqZFKGqpGmjscvEWwOW3IxCC5rYEwmIc3tm5PGA4xyZ2wHyHjlvHDyW1pNoLoHTmmenfj-e-plqemIBuM7D0hsxWVfvRn1sGfKFa0pISZ1ERvRl2W3Y9sh_OpRKQb9Rz_yQKstTSWofmcqO2Usf5zlEszzxEc8iWuhtYpoW3Q2Rdk-VW9jpGOWR8HmvRUGXfHGprGexmeVEuEygYF_jmSdtjFFps3LuwmM1lOLnEIaf_DKaSuXBqIiqWry64qfW3GpnBg__A1AxYDxEkC4Mfn0_JCdHJlhkHzdezUOdAjD_oqiW-7lk2_jOAMxeZiC30OXGX0ZagpUysLOdOVqv-IKF7NO56zGtAcvsbF6qXtIpyZyL_OndMzeheotYY3rCatJdkMWtkf32FZH32DoRrbuUtWtF4M05jZ6xLxJy5Y15AqAZQBiLN8GQzG3zfa1xtdaxcTrKSuOn-k_RfqVeaS4UJjE6QBdPLBeuPlRqTpvXjISVxIfZSXp22sUi73dOnO1FMT17RN4zigQWqadt3et7EOKOncdyA4vvjg6Cqze2iPcBOlysECKFMZSzhjqp5kxAoGsn0gvJd_4kGGyXOSxg8aQs09y8i9rVyHugO3sxlbXF')

# Refresh the page to apply updated cookies
# browser.refresh()

# Keep the browser open indefinitely
print("Browser is now open. Press Ctrl+C to exit.")
try:
    while True:
        time.sleep(60)  # Check every minute (or adjust as needed)
except KeyboardInterrupt:
    print('Script stopped by user.')
