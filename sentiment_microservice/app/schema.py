from pydantic import BaseModel

class TextInput(BaseModel):
    text: str

class SentimentOutput(BaseModel):
    sentiment: str
    # sentiment_score: float = None  # Optional field for sentiment score
