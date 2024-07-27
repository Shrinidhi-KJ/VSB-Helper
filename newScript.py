from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
import time

# Full path to the ChromeDriver executable
chrome_driver_path = 'Z:\\Downloads\\chromedriver-win64\\chromedriver.exe'

# Create a Service object
service = Service(executable_path=chrome_driver_path)

# Create Chrome options
chrome_options = Options()

# Initialize the Chrome WebDriver with the Service object
driver = webdriver.Chrome(service=service, options=chrome_options)

# Open the login page URL
driver.get('https://atlasauth.b2clogin.com/f50ebcfb-eadd-41d8-9099-a7049d073f5c/b2c_1a_atoproduction_atlas_susi/oauth2/v2.0/authorize?client_id=607d08d6-b63b-4735-ad82-05dfcff7efa4&redirect_uri=https%3A%2F%2Fwww.usvisascheduling.com%2Fsignin-aad-b2c_1&response_type=code%20id_token&scope=openid&state=OpenIdConnect.AuthenticationProperties%3Dd7SNPttnDh039Uf8bPUUHTmyE-iYokeDBpqF8DYtWU0Vb4LIhBgnxsm15zGErXpvyNP1WsmyZMiGmfM0cSUZoM36YKbGkpxXPTj-eHL5zzFbhF4BMKd8MMumykiYZPdMLauTDFVrFqn-fWzcdZbPnHX851MFPDUaMO4daYOpkrLGDLBNZsCqIfg7xzafVak0qfwxrPMf6czPw0PX7BNeKP1UsgVGbkpxhACDiiHgBYb6YrV1_zb1eq9SbqlZUkyjIfexABzNH6Axh-m2BSrR4RZy5OAmhFG8--fBn9zKi4oVbbU-tfVtQ8ZDD5ysGZUJZ5vYl3ecxW62FU5rwU3vs1-HF3pt892MHkCHAbIluf4swBEM4kTN9_iplQMaTmaYbeCDd0ZiHpxdNojoo8H5XrM0dzqwAu3yanbnkfVTIgrw5_DROQU7oGu2vKGbCSymxWyx0L5gBJ5R7eWq5yPRD3IOptl8r7Qw09qW1dcvFSlaNsBlRDAmE0ts0YhzNYV7xRwtP7KBcUBJ2bERCZtNSDe8tCq7kYhVMYA_MqeN5j8yl_2Y8kS2kQdW6V-sLoQJczvNqJ9Kq6KCgWC2raVlFjx0L9pAOfOvWhoEo1sQ_wGv1WB-r0nwJnEje78bviqw&response_mode=form_post&nonce=638577197581106130.Y2UzMTlkNDMtNGIxOS00YTYzLWJmZTktNDRlOGYyZGNmZGNkZDNhMzIxOWUtMDkyYS00YTIyLWI0MmYtMjMwMzA2MDE5MTAw&ui_locales=en-US&x-client-SKU=ID_NET472&x-client-ver=6.35.0.0')

# Wait for the page to fully load
time.sleep(5)  # Adjust the sleep time as needed

# Define cookies to be added
cookies = [
    {
        'name': 'AspNet.ApplicationCookie',
        'value': '9NtSQ-8i20qZd3u_s35A4cpOSH_Vkq0GtVV2e4NFYMiSDzbh7cuajrOSUTowNPbeCi6BQVUB7-_7y8LwXrQWGeuikMMUcSpuiFSiy256HbYEDXYNwmRaWjGUQiHx5f12RpHS3y55DiEtWM9ryY8rHhg3wM7N_HMntXgRWbRa_k5OO7wR7XUcmAzhjaVSeRs4y48TP3CoCYkrgCC3r0kxkrDNLaezrnmNLzh0b8Q4AUMnapV1TADUZSWYAT4KOiU9T03EckW1Nz6Ry2T20u3GKBSqVR5EST9UszPOYBUry2tZ9wQk1CDz9NhsKGCe0Lm0mwHQGsadrMaBLHjxYCwptTf_vhBC1-Q1xZJxoR0RyQsTgnbQLxqF751p0T9Jg4-woU0i46WMSUZIT0JxXisC-8bXtdMNPBGfiMlQa0ALF2VqFGIBkKwOzvPO_sjr-TXDNTzjYoOlQxKUUcgvhOWBQJFHlyWafKTdmbFV4WaRLJTIwwSsojejYXWTSo2UQDlK9KGYi2ou72dsAJ7ffQiOSzh50i-Iun7Fn_iL52K5Knj88YKG4hN8zF6_vMHWAm-wKHH0jbic5KOOCRS9-bW7EG5c3tIel1ffzYaBgfEnNPeLtSPY_y3t69dfYYADTJCrQYbrKytC73hvbQ175DTdXnavRlomxcdAzGLP8Y3Pcq_Qw3HtFICyKaFGl7jUwDm50nv4RtgY-dVVFuiAfQNh5co7FaqnVkR3UXVCyw8tcB3342c9i9Wpp9Z0ZLKRyGj8mmQsrA1p29JLwAtsjMteqUrBfNJm_B9u5OUAO2v_aa32NWw82u-O25E4h4LTsPs01SjQ7QCr0Yaf_3zOpDKdvMzCKjmV-ODrzCP4NjsP1oFXXMyLG8BRJ6_csWmDEnFnsbejAz6rBfpFgz2ujKmz9KJkfEQqZArgjrrdW_ceQATfiqv4Cv7Bbvnchav7Ypg1XU7km_QAVbBnCHe3wBVtRnEq7jdvgG-2NEf3SAN',
        'domain': 'www.usvisascheduling.com',
        'path': '/'
    },
    {
        'name': 'ARRAffinity',
        'value': '73867955628765074a805734dbd88d01cf55c67e6db7f2381cb3501c6cdb19a4',
        'domain': 'www.usvisascheduling.com',
        'path': '/'
    },
    {
        'name': 'ARRAffinitySameSite',
        'value': '73867955628765074a805734dbd88d01cf55c67e6db7f2381cb3501c6cdb19a4',
        'domain': 'www.usvisascheduling.com',
        'path': '/'
    },
    {
        'name': 'ASP.NET_SessionId',
        'value': 'bl4oei1xm2ldazgxokqvirdm',
        'domain': 'www.usvisascheduling.com',
        'path': '/'
    },
    {
        'name': 'ContextLanguageCode',
        'value': 'en-US',
        'domain': 'www.usvisascheduling.com',
        'path': '/'
    },
    {
        'name': 'Dynamics365PortalAnalytics',
        'value': '8ducDt84GtzNIERelIM52Cd-V9ydUasq1VKRHmkuxJLpiI3V5ZP1sjeKajA_UoCxLzz_8R7K7y8vBbY1XAkfDQlkb2f_Crf9nrRf8FA0DtSjRXb6u9yzV2qWDgxyW-N4NeHJxgg1Ml4UGpDUtbXO5w2',
        'domain': 'www.usvisascheduling.com',
        'path': '/',
        'expiry': 1722121391  # UNIX timestamp (seconds since epoch)
    },
    {
        'name': '__cf_bm',
        'value': 're2kgGtHB2JftkCEzuBwVksiYqAOB5oxTFL3_j2fRA4-1722121169-1.0.1.1-GSuDXPjP9SsEsUo6AJ3PJbqnsgeoQe6k7.uNdEDQsMsqWz4diGa4U2LNhV031DzIQgkCAHKiNcRVcyGg9RpuJw',
        'domain': 'www.usvisascheduling.com',
        'path': '/'
    },
    {
        'name': 'ai_session',
        'value': '7Z2xYR8N7MweqXRhI4y47r|1722113652301|1722121309568',
        'domain': 'www.usvisascheduling.com',
        'path': '/'
    },
    {
        'name': 'ai_user',
        'value': 'F6FjcV3tnKKqtjDBuXvjfx|2024-07-17T12:23:32.160Z',
        'domain': 'www.usvisascheduling.com',
        'path': '/',
        'expiry': 1722121391  # UNIX timestamp (seconds since epoch)
    },
    {
        'name': 'cf_clearance',
        'value': 'vMvukLOX9B6zYAfR4hAM4usimAngnEmgHgwTx_K8DIQ-1722114189-1.0.1.1-ArgRtOcX.GLbqshOQJFvuMRQ5YQioDvYDAaJWDCqkeIRme7rjEOfPcmltt1gy_.oZZVUcJoccn_3zlNir6k8Jw',
        'domain': 'www.usvisascheduling.com',
        'path': '/',
        'expiry': 1722121391  # UNIX timestamp (seconds since epoch)
    },
    {
        'name': 'isDSTObserved',
        'value': 'false',
        'domain': 'www.usvisascheduling.com',
        'path': '/'
    },
    {
        'name': 'isDSTSupport',
        'value': 'false',
        'domain': 'www.usvisascheduling.com',
        'path': '/'
    },
    {
        'name': 'timeZoneCode',
        'value': '190',
        'domain': 'www.usvisascheduling.com',
        'path': '/'
    },
    {
        'name': 'timezoneoffset',
        'value': '-330',
        'domain': 'www.usvisascheduling.com',
        'path': '/'
    }
]

# Add cookies to the current domain
for cookie in cookies:
    try:
        driver.add_cookie(cookie)
    except Exception as e:
        print(f"Error adding cookie {cookie['name']}: {e}")

# Navigate to the target URL directly
driver.get('https://www.usvisascheduling.com/en-US/ofc-schedule/')

# Wait for the page to fully load
time.sleep(5)

# Optional: Add further interactions here
# For example, you could find elements and interact with them:
# element = driver.find_element(By.ID, "element_id")
# element.click()

print("Browser is running...")

# Keep the browser open
while True:
    time.sleep(10)
