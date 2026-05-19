from newspaper import Article
from textblob import TextBlob
#textblob analyzes emotion of text, newspaper3k is data extractor


def get_news_data(url):
    article= Article(url)

    article.download()
    article.parse()
    article.nlp()
    analysis = TextBlob(article.text)
    sentiment = analysis.sentiment
    
    if sentiment.polarity > 0:
        sentiment_label = "Positive"
    elif sentiment.polarity < 0:
        sentiment_label = "Negative"
    else:
        sentiment_label = "Neutral"

    return {
        "title": article.title,
        "authors": ', '.join(article.authors) if article.authors else "Unknown",
        "publish_date": str(article.publish_date),
        "summary": article.summary,
        "sentiment": f'Polarity: {sentiment.polarity}, Sentiment: {sentiment_label}'
    }