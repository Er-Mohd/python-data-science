from bs4 import BeautifulSoup
import requests

url = 'http://www.google.com/search?q=css'
responce = requests.get(url)
if not responce.status_code == 200:
    print('An error has occurred.')
    exiot()
else:
    print('Success!')
    soup = BeautifulSoup(responce.text, 'html5lib')
    print(soup.prettify())
    # get all heading h1
    headings_3 = soup.find_all('h3')
    print("Headings 3:")
    for i in headings_3:
        print(i.text)

        link = soup.find_all('a')
        print("Link:")
        for i in link:
            print(f'{i.text} ✔ {i.get("href")}')