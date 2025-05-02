from pydantic import BaseModel

class TextInput(BaseModel):
    text: str

class Sentiment(BaseModel):
    polarity: float
    sentiment: str
    word_count: int
    
class SentimentOutput(BaseModel):
    sentiment: Sentiment

    # sentiment_score: float = None  # Optional field for sentiment score
