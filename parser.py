import requests
from bs4 import BeautifulSoup

URL = "https://ua1xbet.com/en/live/Football/"
HEADERS = {
    "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/85.0.4183.102 Safari/537.36",
    'accept': "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9"}


def get_html(url: str, params=None):
    r = requests.get(url, headers=HEADERS, params=params)
    return r


def get_content(html):
    soup = BeautifulSoup(html, 'html.parser')
    items = soup.find_all("div", class_="c-events__item c-events__item_game c-events-scoreboard__wrap")

    for item in items:
        print(item.find(class_="c-events-scoreboard__item").find(class_="n").text)


def parse():
    html = get_html(URL)
    if html.status_code == 200:
        print("all is ok")
        get_content(html.text)
    else:
        print("ERROR")


parse()
