# cookies.py

# Define the cookies as a list of dictionaries
cookies = [
    {
        'name': 'Session ID/name',
        'value': '*** Value to be added ***',
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
