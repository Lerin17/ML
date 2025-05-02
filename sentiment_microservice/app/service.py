from textblob import TextBlob

def analyze_sentiment(text: str) -> str:
    analysis = TextBlob(text)
    polarity:any = analysis.sentiment.polarity
    if polarity > 0:
        return {polarity: "positive"}
    elif polarity == 0:
        return {polarity: "neutral"}
    else:
        return {polarity:"negative"}
