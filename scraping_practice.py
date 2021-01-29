import requests
from bs4 import BeautifulSoup
import pprint

res = requests.get('https://news.ycombinator.com/')
soup = BeautifulSoup(res.text, 'html.parser')
links = soup.select('.storylink')
subtext = soup.select('.subtext')

def sort_stories_by_votes(hn_list):
    return sorted(hn_list, key=lambda k: k['votes'], reverse=True)

def create_custom_hn(links, subtext):
    hn = []
    for idx, title in enumerate(links):
        title = links[idx].getText()
        href = links[idx].get('href', None)
        if subtext[idx].select('.score'):
            votes = subtext[idx].select_one('.score').getText()
            votes = int(votes.split()[0])
            if votes > 99:
                hn.append({'title': title, 'link': href, 'votes': votes})
    return sort_stories_by_votes(hn)

hn_list = create_custom_hn(links, subtext)

pprint.pprint(hn_list)
