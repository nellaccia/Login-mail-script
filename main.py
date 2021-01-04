import requests

# Fill in your details here to be posted to the login form.
payload = {
'Email': '',
'Passwd': ''
}

# Use 'with' to ensure the session context is closed after use.
with requests.Session() as s:
    p = s.post('https://accounts.google.com/signin/challenge/sl/password', data=payload)
# print the html returned or something more intelligent to see if it's a successful login page.
print(p.text)