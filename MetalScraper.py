
from bs4 import BeautifulSoup
from requests_html import HTMLSession


s = HTMLSession()

url = 'https://pmsalesinc.com/todays-metal-prices/'


def getdata(url):
    dict = {}
    metals = []
    price = []
    r = s.get(url)
    soup = BeautifulSoup(r.text, 'html.parser')
    # div_table = soup.find_all("div", {'class': "fl-row fl-row-full-width fl-row-bg-photo fl-node-5d80bc7beaeff fl-row-bg-overlay"})
    #inner_table = soup.find_all("div", {"class": "pp-table-wrap"} )
    table = soup.find('table', class_="pp-table-5d5ad24d73de5")
    metal = table.find_all("td")
    for i in metal:
        if len(i.string.split('$')) != 2:
            metals.append(i.string)
        else:
            if len(i.string.split('$')[1]) != 0:
                price.append(float(''.join(i.string.split('$')[1].split(','))))
            else:
                price.append(0)

    if len(metals) != len(price):
        return False
        
    for i in range(len(metals)):
        dict[metals[i]] = price[i]


    return dict
    



print(getdata(url))