from bs4 import BeautifulSoup
import requests

# return a dictionary with site name and url
def get_site_info():
	return # TODO

# return a list of headline objects. You can choose how to represent headlines
# but make sure your object can have url and title extracted from it by your 
# other helper functions
def get_headlines(soup):
	return # TODO

	
# return the url for the article corresponding to this headline
def get_headline_url(headline):
	return # TODO


# return the text of the headline object
def get_headline_text(headline):
	return # TODO


# return a dictionary for the article containing:
# {
#   site:  site name (ie Huffington Post),
#   url:   article url,
#   title: article title,
#   text:  article content
# }
def process_headline(headline):
	return # TODO


# dictionary object for calling functions
functions = {
	'get_site_info' : get_site_info,
	'get_headlines' : get_headlines,
	'get_headline_url': get_headline_url,
	'get_headline_text': get_headline_text,
	'process_headline': process_headline
}