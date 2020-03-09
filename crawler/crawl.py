import requests
from bs4 import BeautifulSoup
import json
import os

import elpais_frontpage

site_helpers = [
	elpais_frontpage.functions
]

# crawl each site
for functions in site_helpers:
	
	# crawl coverpage
	site_url = functions['get_site_info']()['url']
	site_name = functions['get_site_info']()['site']
	coverpage = requests.get(site_url).content
	
	print("\nCrawling " + site_name + ":")
	
	try:
		coverpage_soup = BeautifulSoup(coverpage, 'lxml')
		headlines = functions['get_headlines'](coverpage_soup)
	except:
		print("Encountered an error while parsing coverpage, skipping.")
		continue
		
	# crawl each article
	for headline in headlines:
		try:
			article_url = functions['get_headline_url'](headline)
			article_title = functions['get_headline_text'](headline)
			filename = (site_name + '_' + article_title)
			filename = "_".join(filename.split(' '))
			filename = "".join(filename.split('.')) # Reporters need to stop using multi-sentence headlines holy fuck
			
			print('Parsing ' + filename + ' ' + article_url)
			
			# omit if this article has already been crawled
			if os.path.exists('articles/' + filename):
				continue
			
			article = functions['process_headline'](headline)
			
			f = open('articles/' + filename, 'w+')
			json.dump(article, f, indent=4)
			f.close()
		
		except:
			print("Encountered an error while parsing article, skipping.")
			continue

# fin

