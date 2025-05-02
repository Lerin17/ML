from fastapi import APIRouter
from app.schema import TextInput, SentimentOutput
from app.service import analyze_sentiment

router = APIRouter(prefix="/sentiment", tags=["sentiment"])

@router.post("/analyze", response_model=SentimentOutput)
def analyze(input: TextInput):
    sentiment_result = analyze_sentiment(input.text)
    return SentimentOutput(sentiment=sentiment_result)
