# cookies.py

# Define the cookies as a list of dictionaries
cookies = [
    {
        'name': '.AspNet.ApplicationCookie',
        'value': 'CB1Y-8QyrWmBlMRoD-lT4kQAr57dPrAYNKzrLB_OZLI21LzGWir9l327UDoZjlRYJsV_xWPdc9WTggdth24RTSPGxZ-kQ5TorwSMBo8YF-0CwEdKlfv3YD2cnmI4PblpP_ezj-2lMmq80PWMW1jvK3-vTh7GtHHoEzga5GmlPlB7AQheELltNpxK1oBrVKZHI9FzRaBof_bmDhZ1SMnEdVnwyLm4MmNLsBqKWPrCqOUSNfEpYjJpvo4YUrtnEr1VmlD0ApHhS4FonJKO9qEpELE9915MafEXAhPx_XR_eeEQsDoPLQckgsZrzVyOg8-Pn4FfJ5cXsnwo6d3D9tTvkzBHU30U94RV9pekspkb3oAmWWsTgt91xU4xSqZFKGqpGmjscvEWwOW3IxCC5rYEwmIc3tm5PGA4xyZ2wHyHjlvHDyW1pNoLoHTmmenfj-e-plqemIBuM7D0hsxWVfvRn1sGfKFa0pISZ1ERvRl2W3Y9sh_OpRKQb9Rz_yQKstTSWofmcqO2Usf5zlEszzxEc8iWuhtYpoW3Q2Rdk-VW9jpGOWR8HmvRUGXfHGprGexmeVEuEygYF_jmSdtjFFps3LuwmM1lOLnEIaf_DKaSuXBqIiqWry64qfW3GpnBg__A1AxYDxEkC4Mfn0_JCdHJlhkHzdezUOdAjD_oqiW-7lk2_jOAMxeZiC30OXGX0ZagpUysLOdOVqv-IKF7NO56zGtAcvsbF6qXtIpyZyL_OndMzeheotYY3rCatJdkMWtkf32FZH32DoRrbuUtWtF4M05jZ6xLxJy5Y15AqAZQBiLN8GQzG3zfa1xtdaxcTrKSuOn-k_RfqVeaS4UJjE6QBdPLBeuPlRqTpvXjISVxIfZSXp22sUi73dOnO1FMT17RN4zigQWqadt3et7EOKOncdyA4vvjg6Cqze2iPcBOlysECKFMZSzhjqp5kxAoGsn0gvJd_4kGGyXOSxg8aQs09y8i9rVyHugO3sxlbXF',
        'domain': 'www.usvisascheduling.com',
        'path': '/',
        'secure': True,
        'httponly': False,
        'expires': None
    }
]

# Example usage in a script to set cookies in a request (using requests library)
import requests

# Example URL (replace with the target URL)
url = 'https://www.usvisascheduling.com'

# Create a session
session = requests.Session()

# Set cookies
for cookie in cookies:
    session.cookies.set(
        cookie['name'],
        cookie['value'],
        domain=cookie['domain'],
        path=cookie['path'],
        secure=cookie['secure'],
        httponly=cookie['httponly'],
        expires=cookie['expires']
    )

# Now you can use the session object to make requests with the cookies set
response = session.get(url)
print(response.text)
