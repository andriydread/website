import requests
from bs4 import BeautifulSoup


def scraper():
    hn = []
    page = 0
    num_of_articles = 25

    while True:
        if len(hn) >= num_of_articles:
            return sorted(hn, key= lambda k:k['Votes'], reverse=True)[:num_of_articles]
        else:
            page += 1
            req = requests.get(f'https://news.ycombinator.com/news?p={page}')
            soup = BeautifulSoup(req.text, 'html.parser')
            
            links = soup.select('.titlelink')
            subtext = soup.select('.subtext')


            for idx, item in enumerate(links):
                title = links[idx].getText()
                link = links[idx].get('href', 'Link not available')
                vote = subtext[idx].select('.score')

                if len(vote):
                    points = int(vote[0].getText().replace(' points', ''))
                else:
                    points = 0

                if points > 99:
                    hn.append({
                                'Title' : title,
                                'Link' : link,
                                'Votes' : points
                                })




