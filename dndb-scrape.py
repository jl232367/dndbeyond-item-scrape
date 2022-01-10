#import urllib, urllib.request, urllib.parse, urllib.error
from bs4 import BeautifulSoup
from urllib.request import Request, urlopen
import re
import ssl



ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

dndb_url = 'https://www.dndbeyond.com/equipment'

dndb_file = Request(dndb_url, headers={'User-Agent': 'Mozilla/5.0'})

webpage = urlopen(dndb_file).read()

soup = BeautifulSoup(webpage, 'html.parser')

#soup_div_items = soup.find_all('div', attrs={"data-url" : True})

#for item in soup_div_items:

link_list = ([item['data-url'] for item in soup.find_all('div', attrs={'data-url' : True})])
count = 0

for page in link_list: 
    item_page = 'https://www.dndbeyond.com' + page
    request_item_page = Request(item_page, headers={'User-Agent': 'Mozilla/5.0'})
    open_item_page = urlopen(request_item_page).read()
    item_soup = BeautifulSoup(open_item_page, 'html.parser')
    for link in item_soup.find_all('a'):
        #filtered_link = link.select('a[href^="/equipment/"]')
        count = count + 1
        print(link.href)
        #print(link.select('a[href^="/equipment/"]'))
        print(count)
#print(link_list)

#print()
#links = re.findall(b'href="(http[s]?://.*?)"', webpage)

#tags = soup('li')

#print(soup.prettify())

#for link in links:
 #   print(link.decode())
#print(webpage)

