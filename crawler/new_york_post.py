from bs4 import BeautifulSoup
import requests

# return a dictionary with site name and url
def get_site_info():
	return {'site': 'New York Post', 'url': 'https://nypost.com/tag/politics/'}

# return a list of headline objects. You can choose how to represent headlines
# but make sure your object can have url and title extracted from it by your 
# other helper functions
def get_headlines(soup):
	return soup.find_all('h3', class_='entry-heading')

	
# return the url for the article corresponding to this headline
def get_headline_url(headline):
	return headline.find_all('a')[0].get('href')


# return the text of the headline object
def get_headline_text(headline):
	return headline.get_text().strip()


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
	body = soup_article.find_all('div', class_='entry-content entry-content-read-more')[0]
	paragraphs = body.find_all('p')
	paragraph_texts = [p.get_text() for p in paragraphs]
	
	result['text'] = '\n\n'.join(paragraph_texts)
	
	# get article timestamp
	try:
		timestamp = soup_article.find('p', class_='byline-date').get_text()
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