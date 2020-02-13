import requests
from bs4 import BeautifulSoup
import json

Articles = []

r1 = requests.get("https://english.elpais.com/")
coverpage = r1.content
soup1 = BeautifulSoup(coverpage, 'lxml')
coverpage_news = soup1.find_all('h2', class_='headline')

for headline in coverpage_news:
	try:
		title = headline.find('a').get_text()
		link = headline.find('a').get('href')
		if link[0:4] != 'http':
			link = "https://english.elpais.com" + link

		print(link)
			
		article = requests.get(link)
		article_content = article.content
		soup_article = BeautifulSoup(article_content, 'lxml')
		body = soup_article.find_all('div', class_='article')[0]
		paragraph_objs = body.find_all('p')
		paragraph_texts = []
		
		for paragraph_obj in paragraph_objs:
			paragraph = paragraph_obj.get_text()
			paragraph_texts.append(paragraph)
		
		article_text = '\n\n'.join(paragraph_texts)
		
		Articles.append({'site': "elpais", "title": title, "link": link, "text": article_text})
	except:
		print("Encountered an error while parsing article, skipping.")
		
		
f = open("scrape.json", 'x')
json.dump(Articles, f)
f.close()