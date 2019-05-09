import http.cookiejar
import urllib.request
import requests
import bs4
# Store the cookies and create an opener that will hold them
cj = http.cookiejar.CookieJar()
opener = urllib.request.build_opener(urllib.request.HTTPCookieProcessor(cj))
# Add our headers
opener.addheaders = [('User-agent', 'dfdf')]
urllib.request.install_opener(opener)
authentication_url = 'https://m.facebook.com/login.php'# The action/ target from the form

# Input parameters we are going to send
payload = {
  'email': 'deoduke@gmail.com',
  'pass': 'kothattilanil.'
  }
data = urllib.parse.urlencode(payload).encode("utf-8")
req = urllib.request.Request(authentication_url, data)# Build our Request object (supplying 'data' makes it a POST)
resp = urllib.request.urlopen(req)# Make the request and read the response
contents = resp.read()
#print(contents)

url = "https://m.facebook.com/wanderlusttravellover/friends"
#url = "https://www.facebook.com/chandana.cherotte/about?lst=100035528530958%3A100006384043824%3A1554968014"
data = requests.get(url, cookies=cj)
soup = bs4.BeautifulSoup(data.text, 'html.parser')
print(soup.prettify())
z = 0
for i in soup.find_all('a'):
    print(i.text)
    if z>17:
        if i.text.lower()=="see more friends":
            break
        elif i.text!= "Add Friend":
            print(i.text)
    z = z+1

