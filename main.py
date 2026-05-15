import tkinter as tk
import nltk
from textblob import TextBlob
from newspaper import Article
nltk.download('punkt')

url ="https://www.bbc.com/news/live/cvgz8qverzqt"
#creates article object 
article= Article(url)

article.download()
article.parse()
article.nlp()

print("Title:", article.title)
print("Authors:", article.authors)
print("Publication Date:", article.publish_date)
print("Summary:", article.summary)



analysis = TextBlob(article.text)
print(analysis.polarity)
print(f'Sentiment: {"Positive" if analysis.sentiment.polarity > 0 else "Negative" if analysis.sentiment.polarity < 0 else "Neutral"}')




