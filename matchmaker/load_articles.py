import os
import json

# filter out garbage that was crawled by mistake
def is_garbage(article):
	if article['title'] == '' or len(article['text']) < 500:
		return True

def load_articles():
	current_dir = os.path.dirname(os.path.abspath(__file__))
	article_dir = os.path.join(current_dir, 'articles')
	
	article_filenames = os.listdir(article_dir)
	article_paths = [os.path.join(article_dir, filename) for filename in article_filenames]
	
	articles = {}
	for path in article_paths:
		f = open(path, 'r')
		article = json.load(f)
		f.close()
		uniq_id = (article['title'], article['site'])
		
		if not is_garbage(article):
			articles[uniq_id] = article
			
	return articles