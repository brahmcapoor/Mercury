import requests
from bs4 import BeautifulSoup


def createHappy():
    with open('emotions/happy.txt', 'wb') as f:
        for i in range(1, 101):
            print(i)
            quotes_page = requests.get(
                ("https://www.goodreads.com/quotes/tag/happiness?page={}").format(i)).text
            soup = BeautifulSoup(
                quotes_page,
                "html.parser")

            for notNeeded in soup(["script", "style", "span", "a"]):
                # remove unnecessary html elements
                notNeeded.extract()

            quotes = [
                quote for quote in soup.find_all(
                    'div',
                    attrs={'class': 'quoteText'})]

            for q in quotes:
                text = q.find_all(text=True)
                for line in text:
                    if line.strip() == "―" or line.strip() == ",":
                        # remove quote attributions
                        continue
                    f.write(line.encode('utf-8'))
