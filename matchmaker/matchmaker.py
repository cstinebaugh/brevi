import os
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity
import numpy as np

import load_articles

articles = load_articles.load_articles()

article_order = []
article_texts = []
for article in articles:
	article_order.append(article)
	article_texts.append(articles[article]['text'] + ' ' + articles[article]['title'])

stopwords = 'english' # TODO: load stopwords as list

vectorizer = TfidfVectorizer(input='content', strip_accents='unicode',
								stop_words=stopwords)

tfidf = vectorizer.fit_transform(article_texts).toarray()

similarities = cosine_similarity(tfidf)
np.fill_diagonal(similarities, 0)

def is_conservative(site):
	return site == "Fox News" or site == "New York Post" or site == "The Washington Times"

	
for i, v in enumerate(similarities):
	mySite = article_order[i][1]
	for j, v2 in enumerate(v):
		theirSite = article_order[j][1]
		if is_conservative(mySite) == is_conservative(theirSite):
			similarities[i, j] = 0


argmax = np.argmax(similarities, axis=1)
amax = np.amax(similarities, axis=1)
stack = np.stack([np.arange(argmax.shape[0]), argmax, amax], axis=1)
best = stack[np.flip(stack[:, 2].argsort())]

for i in range(20):
	title1, site1 = article_order[int(best[2 * i][0])]
	title2, site2 = article_order[int(best[2 * i][1])]
	
	filename1 = site1 + '_' + title1
	filename1 = "_".join(filename1.split(' '))
	filename1 = "".join(filename1.split('.'))
	
	filename2 = site2 + '_' + title2
	filename2 = "_".join(filename2.split(' '))
	filename2 = "".join(filename2.split('.'))
	
	print("Match:\n" + filename1 + "\n" + filename2 + "\n\n")