from bs4 import BeautifulSoup
import requests

# return a dictionary with site name and url
def get_site_info():
	return {'site': 'El Pais', 'url': 'https://english.elpais.com/'}

# return a list of headline objects. You can choose how to represent headlines
# but make sure your object can have url and title extracted from it by your 
# other helper functions
def get_headlines(soup):
	return soup.find_all('h2', class_='headline')

	
# return the url for the article corresponding to this headline
def get_headline_url(headline):
	url = headline.find('a').get('href')
	if url[0:4] != 'http':
		url = 'https://english.elpais.com' + url
	
	return url


# return the text of the headline object
def get_headline_text(headline):
	return headline.find('a').get_text()


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
	article = requests.get(result['url']).content
	soup_article = BeautifulSoup(article, 'lxml')
	body = soup_article.find_all('div', class_='article')[0]
	paragraph_objs = body.find_all('p')
	paragraph_texts = [p.get_text() for p in paragraph_objs]
	
	result['text'] = '\n\n'.join(paragraph_texts)
	
	return result


# dictionary object for calling functions
functions = {
	'get_site_info' : get_site_info,
	'get_headlines' : get_headlines,
	'get_headline_url': get_headline_url,
	'get_headline_text': get_headline_text,
	'process_headline': process_headline
}