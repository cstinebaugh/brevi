from bs4 import BeautifulSoup
import requests
import datetime

import headers

# return a dictionary with site name and url
def get_site_info():
	return {'site': 'The Huffington Post', 'url': 'https://huffpost.com/news/politics'}

# return a list of headline objects. You can choose how to represent headlines
# but make sure your object can have url and title extracted from it by your 
# other helper functions
def get_headlines(soup):
	return soup.find_all('div', class_='card__headlines')

	
# return the url for the article corresponding to this headline
def get_headline_url(headline):
	anchors = headline.find_all('a', class_='card__headline')
	if len(anchors) == 0:
		anchors = headline.find_all('a', class_='card__headline card__headline--long')
	
	url = anchors[0].get('href')
	return url


# return the text of the headline object
def get_headline_text(headline):
	return headline.find_all('h2', class_='card__headline__text')[0].get_text()


# return a dictionary for the article containing:
# {
#   site:  site name (ie Huffington Post),
#   url:   article url,
#   title: article title,
#	time:  article posted date,
#   text:  article content
# }
def process_headline(headline):
	result = {}
	result['site'] = get_site_info()['site']
	result['url'] = get_headline_url(headline)
	result['title'] = get_headline_text(headline)
	
	# download article and parse html to get its text
	article = requests.get(result['url'], headers=headers.header1).content
	soup_article = BeautifulSoup(article, 'lxml')
	paragraphs = soup_article.find_all('div', class_='content-list-component yr-content-list-text text')
	paragraph_texts = [p.get_text() for p in paragraphs]
	
	result['text'] = '\n\n'.join(paragraph_texts)
	
	# get article timestamp
	try:
		timestamp = soup_article.find_all('span', class_='timestamp__date--published')[0].find_all('span')[0].get_text()
	except:
		timestamp = datetime.datetime.now().isoformat()
	
	result['time'] = timestamp
	
	return result
	

# dictionary object for calling functions
functions = {
	'get_site_info' : get_site_info,
	'get_headlines' : get_headlines,
	'get_headline_url': get_headline_url,
	'get_headline_text': get_headline_text,
	'process_headline': process_headline
}