from textblob import TextBlob
from typing import Dict

def analyze_sentiment(text: str) :
    analysis = TextBlob(text)
    polarity = analysis.sentiment.polarity

    if polarity > 0:
        sentiment = "positive"
    elif polarity == 0:
        sentiment = "neutral"
    else:
        sentiment = "negative"

    word_count = len(text.split())

    return {
        "polarity": polarity,
        "sentiment": sentiment,
        "word_count": word_count
        # "sentiment_score": analysis.sentiment.polarity  # Optional field for sentiment score
      
    }
